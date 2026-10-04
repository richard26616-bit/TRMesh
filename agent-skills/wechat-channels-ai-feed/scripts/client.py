"""Single-request TRMesh client. Standard library only; no automatic paid retries."""
import argparse
import ipaddress
import json
import math
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


def validate(value, schema, label='request'):
    """Validate supplied JSON against the bundled, resolved endpoint schema."""
    for choice in ('anyOf', 'oneOf'):
        if choice in schema:
            successes = 0
            for item in schema[choice]:
                try:
                    validate(value, item, label)
                    successes += 1
                except ValueError:
                    pass
            if not successes or (choice == 'oneOf' and successes != 1):
                raise ValueError(label + ': no matching schema alternative')
            return
    for child in schema.get('allOf', []):
        validate(value, child, label)
    kind = schema.get('type')
    checks = {'object': isinstance(value, dict), 'array': isinstance(value, list),
              'string': isinstance(value, str), 'integer': type(value) is int,
              'number': type(value) in (int, float), 'boolean': type(value) is bool,
              'null': value is None}
    if kind and not checks.get(kind, False):
        raise ValueError(label + ': expected ' + kind)
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(label + ': invalid enum value')
    if 'const' in schema and value != schema['const']:
        raise ValueError(label + ': invalid constant')
    if isinstance(value, dict):
        props = schema.get('properties', {})
        for key in schema.get('required', []):
            if key not in value:
                raise ValueError(label + '.' + key + ': required')
        for key, val in value.items():
            if key in props:
                validate(val, props[key], label + '.' + key)
            elif schema.get('additionalProperties') is False:
                raise ValueError(label + '.' + key + ': unknown field')
            elif isinstance(schema.get('additionalProperties'), dict):
                validate(val, schema['additionalProperties'], label + '.' + key)
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0) or len(value) > schema.get('maxItems', float('inf')):
            raise ValueError(label + ': array length out of range')
        for i, item in enumerate(value):
            validate(item, schema.get('items', {}), label + '[' + str(i) + ']')
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0) or len(value) > schema.get('maxLength', float('inf')):
            raise ValueError(label + ': string length out of range')
        if schema.get('pattern') and not re.search(schema['pattern'], value):
            raise ValueError(label + ': pattern mismatch')
    if type(value) in (int, float):
        if not math.isfinite(value):
            raise ValueError(label + ': number must be finite')
        if value < schema.get('minimum', -float('inf')) or value > schema.get('maximum', float('inf')):
            raise ValueError(label + ': number out of range')
        if 'exclusiveMinimum' in schema and value <= schema['exclusiveMinimum']:
            raise ValueError(label + ': below exclusive minimum')
        if 'exclusiveMaximum' in schema and value >= schema['exclusiveMaximum']:
            raise ValueError(label + ': above exclusive maximum')


def base_url(raw):
    """Accept HTTPS gateway roots and local HTTP roots; disallow credential-bearing URLs."""
    parsed = urllib.parse.urlsplit(raw)
    if parsed.username or parsed.password or parsed.query or parsed.fragment or not parsed.hostname:
        raise ValueError('TRMESH_BASE_URL must be a gateway origin without credentials, query or fragment')
    if parsed.path not in ('', '/'):
        raise ValueError('TRMESH_BASE_URL must not include /openapi or another path')
    local = parsed.hostname.lower() == 'localhost'
    try:
        local = local or ipaddress.ip_address(parsed.hostname).is_loopback
    except ValueError:
        pass
    if parsed.scheme != 'https' and not (parsed.scheme == 'http' and local):
        raise ValueError('HTTPS is required except for a loopback development server')
    if parsed.hostname.lower() in ('api.tikhub.io', 'redfox.hk', 'api.redfox.hk'):
        raise ValueError('Configure your TRMesh gateway, not the data provider')
    return raw.rstrip('/')


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Redirect refused; verify the gateway origin')


def prepare(contract, endpoint, query, body, origin):
    """Build only an allowlisted request after schema and semantic validation."""
    entry = contract['endpoints'].get(endpoint)
    if not entry:
        raise ValueError('Unknown endpoint; use --describe')
    validate(query, entry['querySchema'], 'query')
    if entry['method'] == 'GET' and body is not None:
        raise ValueError('GET requests must not include a JSON body')
    if body is not None:
        validate(body, entry['bodySchema'], 'body')
    elif entry.get('bodyRequired'):
        raise ValueError('JSON body is required')
    elif entry['method'] == 'GET':
        body = None
    for place, supplied in [('query', query), ('body', body or {})]:
        for key, allowed in entry.get('documentedEnums', {}).get(place, {}).items():
            if key in supplied and supplied[key] not in allowed:
                raise ValueError(place + '.' + key + ': not a source-documented value')
    for group in entry.get('requiresAny', []):
        supplied = body if entry['method'] == 'POST' else query
        if not any((supplied or {}).get(key) not in (None, '', []) for key in group):
            raise ValueError('Provide at least one of: ' + ', '.join(group))
    path = entry['path']
    if not path.startswith('/api/v1/') or any(x in path for x in ('?', '#', '..', '\\')):
        raise ValueError('Invalid bundled endpoint path')
    query_pairs = []
    for key, val in query.items():
        if val is None:
            continue
        # OpenAPI form/explode arrays are repeated parameters; booleans use JSON spelling.
        values = val if isinstance(val, list) else [val]
        for item in values:
            if isinstance(item, (dict, list)):
                raise ValueError('Object query encoding is not supported: ' + key)
            query_pairs.append((key, str(item).lower() if isinstance(item, bool) else str(item)))
    encoded = urllib.parse.urlencode(query_pairs)
    url = base_url(origin) + '/openapi' + path + ('?' + encoded if encoded else '')
    return entry, url, body


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--endpoint')
    parser.add_argument('--query-file', type=pathlib.Path)
    parser.add_argument('--body-file', type=pathlib.Path)
    parser.add_argument('--describe', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--timeout', type=int, default=30)
    args = parser.parse_args()
    skill_root = pathlib.Path(__file__).resolve().parents[1]
    contract = json.loads((skill_root / 'references/contracts.json').read_text(encoding='utf-8-sig'))
    if args.describe:
        print(json.dumps(contract, ensure_ascii=False, indent=2))
        return
    if not args.endpoint:
        raise ValueError('--endpoint is required')
    query = json.loads(args.query_file.read_text(encoding='utf-8-sig')) if args.query_file else {}
    body = json.loads(args.body_file.read_text(encoding='utf-8-sig')) if args.body_file else None
    origin = os.environ.get('TRMESH_BASE_URL', '')
    if args.dry_run and not origin:
        origin = 'https://gateway.example.invalid'
    entry, url, body = prepare(contract, args.endpoint, query, body, origin)
    if args.dry_run:
        print(json.dumps({'mode': 'dry-run', 'method': entry['method'], 'url': url,
                          'body': body, 'authorization': '<redacted>', 'networkRequests': 0},
                         ensure_ascii=False, indent=2))
        return
    token = os.environ.get('TRMESH_API_TOKEN', '')
    if not token or any(c in token for c in '\r\n'):
        raise ValueError('Set a valid TRMESH_API_TOKEN developer token')
    if not 1 <= args.timeout <= 120:
        raise ValueError('--timeout must be between 1 and 120 seconds')
    payload = json.dumps(body, ensure_ascii=False, allow_nan=False).encode('utf-8') if body is not None else None
    headers = {'Authorization': 'Bearer ' + token, 'Accept': 'application/json'}
    if payload is not None:
        headers['Content-Type'] = 'application/json'
    request = urllib.request.Request(url, data=payload, headers=headers, method=entry['method'])
    # Disable environment proxies: no accidental credentials exposure to inherited proxy config.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(request, timeout=args.timeout) as response:
            raw = response.read(16 * 1024 * 1024 + 1)
            if len(raw) > 16 * 1024 * 1024:
                raise ValueError('Response exceeds 16 MiB; request a smaller page')
            result = json.loads(raw)
    except urllib.error.HTTPError as error:
        raise ValueError('Gateway HTTP ' + str(error.code) + '; no automatic retry. Check Usage and request status.') from None
    except (urllib.error.URLError, TimeoutError):
        raise ValueError('Network request failed; check Usage before retrying a potentially billable request') from None
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(2)
