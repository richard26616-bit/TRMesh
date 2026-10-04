# 从旧版目录迁移

## 路径

旧仓库有34个路径把反斜杠当作文件名字符，例如`agent-skills/example\SKILL.md`，Windows不能检出。现统一为`agent-skills/example/SKILL.md`，保留Git历史。重新拉取后安装标准目录，不继续复制旧文件。

## 请求

旧说明把target、objective、timeRange、filters等自然语言字段通用地传入接口。新版将这些字段用于Agent计划，真实请求只使用对应endpoint声明的query/body字段。

例如抖音搜索V5必须POST JSON；公众号、视频号v2的接口也使用POST JSON。旧的GET调用不能靠添加参数修复，必须使用新版契约与网关绑定。

## Skill目录

保留历史slug以减少链接失效，新增可支持的参考场景；每个目录新增参数参考、独立调用器和示例。版本从1.0.0更新为2.0.0。

- `toutiao-search`：停用。最新版官方没有头条关键词搜索；使用`toutiao-article-analysis`分析用户指定文章。
- `xiaohongshu-cover`：停用。没有图片生成接口；笔记写作和标题评分可用对应Skill，但不替代封面生成。
- `*-downloader`：slug兼容保留，名称与说明改为媒体链接提取；脚本不下载、解密或合并视频文件。
- “每日”“七日”“热门”“低粉”“相似”类：注明样本窗口与判断依据；没有全量官方榜单时不声称全平台排名。
- 订阅类：一次采样，需外部调度；增长类：历史接口或两次快照，首次只建基线。

完整参考场景别名映射在`catalog/coverage.json`。安装者应先检查自己修改过的旧Skill，避免直接覆盖本地定制工作流。
