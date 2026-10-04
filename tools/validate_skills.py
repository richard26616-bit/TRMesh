"""Validate portability, exact endpoint contracts, examples and credential boundaries offline."""
import argparse
import hashlib
import importlib.util
import json
import pathlib
import re
import threading
import unittest
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from client import NoRedirect, base_url, prepare, validate


class ClientBoundaryTests(unittest.TestCase):
    def test_gateway_origin(self):
        for bad in ('https://api.tikhub.io', 'https://redfox.hk', 'http://public.example',
                    'https://secret@example.com', 'https://example.com?token=secret',
                    'https://example.com/openapi', 'ftp://example.com', 'https://example.com#x'):
            with self.assertRaises(ValueError):
                base_url(bad)
        self.assertEqual('http://127.0.0.1:5207', base_url('http://127.0.0.1:5207/'))
        self.assertEqual('https://gateway.example', base_url('https://gateway.example'))

    def test_nested_schema_and_unions(self):
        item_schema = {'type': 'object', 'required': ['score'], 'additionalProperties': False,
                       'properties': {'score': {'anyOf': [{'type': 'integer', 'minimum': 1, 'maximum': 5}, {'type': 'null'}]}}}
        schema = {'type': 'object', 'required': ['items'], 'additionalProperties': False,
                  'properties': {'items': {'type': 'array', 'minItems': 1, 'items': item_schema}}}
        validate({'items': [{'score': 3}, {'score': None}]}, schema)
        for bad in ({}, {'items': []}, {'items': [{'score': True}]},
                    {'items': [{'score': 6}]}, {'items': [{'score': 3, 'token': 'x'}]},
                    {'items': [{'score': 3}], 'target': 'generic-field'}):
            with self.assertRaises(ValueError):
                validate(bad, schema)
        with self.assertRaises(ValueError):
            validate(float('nan'), {'type': 'number'})

    def test_allowlist_and_get_body(self):
        entry = {'method': 'GET', 'path': '/api/v1/test/read', 'querySchema': {
            'type': 'object', 'required': ['id'], 'properties': {'id': {'type': 'string'}}, 'additionalProperties': False},
            'bodySchema': {'type': 'object', 'additionalProperties': False, 'properties': {}}}
        contract = {'endpoints': {'read': entry}}
        _, url, _ = prepare(contract, 'read', {'id': 'a&b'}, None, 'https://gateway.example')
        self.assertTrue(url.endswith('?id=a%26b'))
        for key, query, body in [('unknown', {'id': 'x'}, None), ('read', {}, None),
                                 ('read', {'id': 'x', 'target': 'x'}, None), ('read', {'id': 'x'}, {})]:
            with self.assertRaises(ValueError):
                prepare(contract, key, query, body, 'https://gateway.example')
        entry['querySchema']['properties']['search_type'] = {'type': 'string'}
        entry['documentedEnums'] = {'query': {'search_type': ['video', 'user']}}
        with self.assertRaises(ValueError):
            prepare(contract, 'read', {'id': 'x', 'search_type': 'bili_user'}, None, 'https://gateway.example')
        prepare(contract, 'read', {'id': 'x', 'search_type': 'user'}, None, 'https://gateway.example')

    def test_redirect_does_not_forward_token(self):
        received = []
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                received.append((self.path, self.headers.get('Authorization')))
                self.send_response(302 if self.path == '/start' else 200)
                if self.path == '/start':
                    self.send_header('Location', '/destination')
                self.end_headers()
            def log_message(self, *args):
                pass
        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            request = urllib.request.Request('http://127.0.0.1:' + str(server.server_port) + '/start', headers={'Authorization': 'Bearer fixture-token'})
            with self.assertRaises(ValueError):
                urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect()).open(request)
            self.assertEqual([('/start', 'Bearer fixture-token')], received)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


def check_repo(root, spec_path=None):
    metadata = json.loads((root / 'catalog/source.json').read_text(encoding='utf-8'))
    operations = json.loads((root / 'catalog/operations.json').read_text(encoding='utf-8'))
    official = {(o['method'], o['path']): o for o in operations}
    if len(official) != metadata['officialOperationCount']:
        raise ValueError('Operation inventory count mismatch')
    spec = json.loads(spec_path.read_bytes()) if spec_path else None
    if spec_path and hashlib.sha256(spec_path.read_bytes()).hexdigest() != metadata['sourceSha256']:
        raise ValueError('Official source changed: review the upstream diff before regenerating')
    catalog = json.loads((root / 'catalog/skills.json').read_text(encoding='utf-8'))
    paths = list((root / 'agent-skills').glob('*/SKILL.md'))
    if len(paths) != len(catalog) or len(catalog) != metadata['skillCount']:
        raise ValueError('Skill directory/catalog count mismatch')
    if len({s['slug'] for s in catalog}) != len(catalog):
        raise ValueError('Duplicate slug')
    bindings, examples = set(), 0
    template = pathlib.Path(__file__).with_name('client.py').read_bytes()
    for item in catalog:
        folder = root / 'agent-skills' / item['slug']
        text = (folder / 'SKILL.md').read_text(encoding='utf-8')
        if not re.fullmatch('[a-z0-9-]{1,64}', item['slug']):
            raise ValueError('Invalid portable skill name: ' + item['slug'])
        if not text.startswith('---\nname: ' + item['slug'] + '\n') or 'description: ' not in text:
            raise ValueError('Invalid frontmatter: ' + item['slug'])
        if (folder / 'scripts/client.py').read_bytes() != template:
            raise ValueError('Client template drift: ' + item['slug'])
        for link in re.findall(r'\]\(([^)#]+)\)', text):
            if not link.startswith(('http:', 'https:')) and not (folder / link).exists():
                raise ValueError('Broken local reference: ' + item['slug'] + ':' + link)
        contract = json.loads((folder / 'references/contracts.json').read_text(encoding='utf-8'))
        expected = [e['method'] + ' ' + e['path'] for e in contract['endpoints'].values()]
        if expected != item['tools']:
            raise ValueError('Catalog binding mismatch: ' + item['slug'])
        if bool(contract['endpoints']) != item['enabled']:
            raise ValueError('Enabled flag mismatch: ' + item['slug'])
        for key, endpoint in contract['endpoints'].items():
            pair = (endpoint['method'], endpoint['path'])
            if pair not in official or official[pair]['operationId'] != endpoint['operationId']:
                raise ValueError('Unknown official binding: ' + str(pair))
            bindings.add(pair)
            if endpoint['method'] + ' ' + endpoint['path'] not in text or '/openapi' + endpoint['path'] not in text:
                raise ValueError('Missing explicit gateway binding: ' + item['slug'])
            if spec:
                from build_skills import contract as from_source
                if endpoint != from_source(endpoint['path'], spec):
                    raise ValueError('Schema does not match source: ' + item['slug'] + ':' + key)
            example = endpoint['example']
            prepare(contract, key, example['query'], example['body'], 'https://gateway.example.invalid')
            examples += 1
        for place in (folder / 'references', folder / 'examples'):
            for file in place.glob('*.json'):
                json.loads(file.read_text(encoding='utf-8'))
    coverage = json.loads((root / 'catalog/coverage.json').read_text(encoding='utf-8'))
    if len(coverage) != metadata['referenceScenarioCount']:
        raise ValueError('Coverage count mismatch')
    enabled = {s['slug'] for s in catalog if s['enabled']}
    for item in coverage:
        if item['status'] != 'unsupported' and item['targetSkill'] not in enabled:
            raise ValueError('Missing capability mapping: ' + item['sourceSkill'])
    return {'skills': len(catalog), 'enabled': len(enabled), 'uniqueBoundEndpoints': len(bindings),
            'requestExamplesValidated': examples, 'referenceScenarios': len(coverage),
            'officialSchemaCompared': bool(spec), 'liveDataVerified': False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=pathlib.Path)
    parser.add_argument('--spec', type=pathlib.Path)
    parser.add_argument('--report', type=pathlib.Path)
    args = parser.parse_args()
    report = check_repo(args.root, args.spec)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ClientBoundaryTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
    report['clientBoundaryTests'] = result.testsRun
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()
