# TRMesh Skill 契约同步与维护

本仓库只公开可安装 Skill、实际绑定的接口契约、调用器与离线校验工具。原始来源地址、完整来源目录、外部场景采集记录和系统导入记录由维护者保留在私有维护仓库，不随公开资产发布。

## 契约与场景

- 发布者审查的契约版本、日期与原始文件 SHA-256：`catalog/source.json`。
- Skill 实际绑定的101个方法/路径索引：`catalog/operations.json`，不是网关全部可用接口列表。
- 每个 Skill 的完整请求/响应契约：`references/contracts.json`。
- 已审查工作流：`tools/recipes.py`；TRMesh场景目录：`catalog/reference-scenarios.json`。
- 历史目录标识：`catalog/seed-definitions.json`，用于可复现生成及兼容迁移。

## 更新步骤

1. 从私有维护流程取得已审查的原始UTF-8契约文件，核对其版本和SHA-256。不要从HTML标题猜测方法或字段。
2. 比较method/path、operationId、query/body、required、枚举、分页和响应说明。方法变化视为契约变化，旧入口不能继续调用。
3. 系统注册、价格、权限、限流及上线状态在内部维护流程中审查；公开仓库不能自动上线接口或修改生产配置。
4. 审查任务配方和场景目录。缺少能力时明确不支持，不虚构接口或生成结果。
5. 生成到暂存目录，检查差异后再发布：

```shell
python tools/build_skills.py --spec /path/to/contract-openapi.json --scenarios catalog/reference-scenarios.json --seed-json catalog/seed-definitions.json --output /path/to/staging
python tools/validate_skills.py /path/to/staging --spec /path/to/contract-openapi.json
python tools/validate_skills.py .
```

6. 同步目录、独立调用器、接口索引、覆盖报告和README统计。原始来源目录中未绑定的管理接口不进入公开索引。
7. 执行离线校验和公开资料边界检查。校验会拒绝内部来源名称，避免生成后再次泄露；调用器仍防止Token误发给非网关服务。
8. 真实付费调用由部署方按预算另行验证，仅发布脱敏结论；未验证时保留`liveDataVerified:false`。

## 自动化

`validate.yml`在Linux/Windows离线校验全部Skill、请求示例及公开资料边界，不需要密钥。

`source-drift.yml`使用仓库Secret `CONTRACT_SOURCE_URL`指定的审查来源进行漂移检查，地址不写进公开文件或日志。未配置时明确跳过来源检查；离线检查仍正常执行。此工作流不会自动上线接口、发布生成资产或调用付费接口。

## 历史验证摘要

`sync-diff.json`和`runtime-sync.json`仅保留脱敏的历史维护摘要，不能用历史导入数量推断当前运营状态。原始溯源资料和导入明细由维护者私有保存。
