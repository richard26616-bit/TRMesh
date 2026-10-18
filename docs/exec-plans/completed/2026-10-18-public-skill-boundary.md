# 公开 Skill 资料边界修复

状态：完成代码清理和离线验证，随本次提交发布。

## 范围和原因

公开仓库此前将内部契约来源、外部场景标识与源同步记录混入维护资料和生成资产。公开内容应仅包含 TRMesh Skill 的用法、实际绑定契约及脱敏维护摘要。

## 修改文件与行为

- `docs/maintenance.md`、`docs/getting-started.md`、`docs/capability-coverage.md`、`README.md`：按公开 Skill 维护流程整理说明。
- `NOTICE`：保留第三方资料、商标和服务的权利边界声明；原始溯源记录由维护者私有保存。
- `tools/build_skills.py`、`tools/recipes.py`：使用通用场景输入参数 `--scenarios`，仅生成实际绑定接口的公开索引，避免再次输出内部来源标签。
- `catalog/source.json`、`catalog/operations.json`、`catalog/reference-scenarios.json`、`catalog/skills.json`、`catalog/coverage.json`：同步生成的公开元数据及能力边界。公开操作索引为101项（GET 86 / POST 15），源契约总数量单独记录，二者不能混用。
- `docs/sync-diff.json`、`docs/runtime-sync.json`：仅保留脱敏历史摘要，原始来源、未绑定管理路径和导入细节不随公开资产发布。
- `tools/client.py`与122份`agent-skills/*/scripts/client.py`：保持原有地址误发防护、拒绝重定向及请求边界；受限域名策略采用摘要匹配，不公开服务名称。
- `tools/validate_skills.py`、`docs/validation.json`：增加公开文本边界与受限域名策略回归。
- `.github/workflows/source-drift.yml`：来源地址改为仓库Secret `CONTRACT_SOURCE_URL`，不写入公开文件或错误日志；未配置时明确跳过来源漂移检查。

## 验证

- 当前公开文本扫描无内部来源标签；校验器在清理前复现失败，清理后通过。
- 122份执行契约逐字节摘要不变；120个可安装Skill、101个实际绑定接口、460组请求示例、121项场景映射校验通过。
- 6项客户端/发布边界测试通过。另在私有维护环境核对原有3个受限域名仍被拒绝。
- 与原始源契约逐项比对通过；没有调用付费数据接口或操作生产环境。

## 影响和风险

- Skill调用方法、路径、参数、契约、计费/权限要求及Token处理不变；无UI变更。
- 维护生成命令从特定来源命名改用`--scenarios`，旧维护脚本需按当前文档更新。
- 公开接口索引收敛到实际绑定的101项，不再用它表示网关全部接口。
- 来源漂移检查需维护者配置Secret；不影响默认离线验证。历史提交不改写。

## 独立复核

复核发现场景名称仍含中文来源别名，已同步修正场景输入与生成元数据。发布检查现在对中文与英文片段做摘要匹配，覆盖简繁中文别名及拼接英文标识；新增失败断言经修复转为通过。其余契约、域名策略及工作流未发现重要问题。
