# 契约同步与维护

## 事实来源

- 官方OpenAPI：`https://api.tikhub.io/openapi.json`。
- 当前来源版本、日期与SHA-256：`catalog/source.json`。
- 1,050条操作索引：`catalog/operations.json`。
- 完整绑定契约：各Skill的`references/contracts.json`。
- 已审查的工作流与路由角色：`tools/recipes.py`。

参考广场的场景索引保存在`catalog/reference-scenarios.json`，只保留名称与标识，不复制其Skill正文。原有目录标识保存在`catalog/seed-definitions.json`，用于可复现生成和兼容迁移。

## 更新步骤

1. 从官方地址下载原始UTF-8文件，保留字节以计算SHA-256。不要从HTML标题猜测请求方法或字段。
2. 比较method/path、operationId、query/body字段、required、枚举、分页和响应说明。一个路径从GET变为POST须看作契约变化；旧入口不能继续调用。
3. 更新TRMesh系统注册表与请求/响应文档。运行时导入新接口保持草稿；保留既有价格、限流、免费额度、折扣与权限。没有当前官方来源的旧路径下线；历史别名不能自动视为可用。
4. 人工检查`recipes.py`，确认每个任务所需的身份解析、内容获取与分析能力。不支持场景放入UNSUPPORTED，部分支持放入覆盖报告并明确限制。
5. 更新生成器的日期与已审查版本后执行生成，写到暂存目录审查差异，不直接覆盖已运营资产。

```shell
python tools/build_skills.py --spec /path/to/tikhub-openapi.json --redfox catalog/reference-scenarios.json --seed-json catalog/seed-definitions.json --output /path/to/staging
python tools/validate_skills.py /path/to/staging --spec /path/to/tikhub-openapi.json
```

6. 同步生成目录、独立调用器、目录manifest、覆盖报告与README统计；后台Skill种子绑定也要使用同一manifest。不要将自然语言goal/target字段直接传给平台数据接口。
7. 执行离线校验、系统构建和回归。部署方另做小预算真实请求，并记录实际返回能力；未做真实调用必须保留`liveDataVerified:false`。
8. 更新同步报告、迁移说明与版本，再提交发布。

## 自动化

`validate.yml`在Linux与Windows运行离线检查，不需要密钥。`source-drift.yml`每周及手动下载官方OpenAPI，只检查来源漂移，失败要求人工审查；不会自动上线接口、推送生成资产或调用付费数据接口。

不要因为源码版本变化自动把全部新增接口上线。一个Skill的契约匹配成功，也不等于其所有工作流结论都可通过单次响应支持。

## 2026-10-04 同步证据

官方接口从985增至1,050，GET从918变为825，POST从67变为225；method/path新增375、移除310，其中包含方法更正。详细差异见`sync-diff.json`。

本地系统导入367项新目录记录，将310项过期官方入口下线，核验原有有效接口的价格、限流与运营设置保持一致。最终1,050项官方接口全部注册；本地总目录仍保留历史记录和兼容项，不能拿总记录数当作当前可执行接口数。运行时证据见`runtime-sync.json`。
