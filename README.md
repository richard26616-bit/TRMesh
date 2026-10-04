# TRMesh Agent Skills

面向社交媒体研究、账号运营与内容创作的可安装 Agent Skill。所有数据请求通过自己的 **TRMesh OpenAPI 网关**执行，使用开发者 Token；计费、权限、限流和请求记录由网关统一处理。

[![Validate skills](https://github.com/richard26616-bit/TRMesh/actions/workflows/validate.yml/badge.svg)](https://github.com/richard26616-bit/TRMesh/actions/workflows/validate.yml)

## 当前版本

| 项目 | 结果 |
| --- | --- |
| 契约校验日期 | 2026-10-04 |
| TRMesh 注册接口快照 | 1,050 个接口：GET 825 / POST 225 |
| 可安装 Skill | **120** |
| 停用旧入口 | 2：今日头条关键词搜索、小红书图片封面生成 |
| Skill 实际绑定接口 | **101** 个不同的方法／路径 |
| 离线请求示例校验 | **460** 组 |
| 场景覆盖评估 | **121** 项：直接支持 23、组合实现 42、部分支持 32、不支持 24 |

这是一份 Skill 与接口契约仓库，不包含 TRMesh 服务端或密钥。静态契约、请求构造与本地系统目录已核对；**没有进行真实付费数据调用**。能否在线执行，还取决于你部署的网关版本、接口上线状态、开发者权限、余额以及数据服务状态。

## 快速选择

| 想完成的任务 | 从这里开始 |
| --- | --- |
| 抖音作品关键词搜索 | [douyin-search](agent-skills/douyin-search/SKILL.md) |
| 小红书笔记搜索 | [xiaohongshu-search](agent-skills/xiaohongshu-search/SKILL.md) |
| 公众号文章搜索 | [wechat-search](agent-skills/wechat-search/SKILL.md) |
| TikTok 指定话题作品 | [tiktok-topic-aweme-list](agent-skills/tiktok-topic-aweme-list/SKILL.md) |
| 多平台热榜 | [trending-hub](agent-skills/trending-hub/SKILL.md) |
| 账号诊断 | [douyin-account-diagnosis](agent-skills/douyin-account-diagnosis/SKILL.md)、[wechat-account-analyzer](agent-skills/wechat-account-analyzer/SKILL.md) |
| 评论与需求洞察 | [bilibili-comment](agent-skills/bilibili-comment/SKILL.md)、[reddit-voice-of-customer](agent-skills/reddit-voice-of-customer/SKILL.md) |
| 标题评分与原创写作 | [xiaohongshu-title-score](agent-skills/xiaohongshu-title-score/SKILL.md)、[wechat-write](agent-skills/wechat-write/SKILL.md) |
| 媒体链接提取 | [video-downloader](agent-skills/video-downloader/SKILL.md)、[wechat-video-downloader](agent-skills/wechat-video-downloader/SKILL.md) |
| 已有字幕摘要 | [youtube-digest](agent-skills/youtube-digest/SKILL.md) |

[查看全部 Skill](agent-skills/README.md) · [121 项能力映射](docs/capability-coverage.md) · [安装与调用](docs/getting-started.md) · [成本与运行限制](docs/operations.md)

## 平台覆盖

| 平台 | 可安装目录数 |
| --- | --- |
| bilibili | 12 |
| douyin | 19 |
| instagram | 4 |
| kuaishou | 7 |
| multi | 9 |
| reddit | 3 |
| tiktok | 5 |
| toutiao | 1 |
| wechat | 20 |
| weibo | 5 |
| x | 7 |
| xiaohongshu | 18 |
| youtube | 6 |
| zhihu | 4 |

每个平台的完整名称、分类、绑定和状态见 [catalog/skills.json](catalog/skills.json)。公众号和视频号统一归属 WeChat 产品平台，使用不同的接口路径和标识符。

## 安装

环境要求：Python **3.10+**；调用器只依赖标准库。Agent 客户端需要支持包含 `SKILL.md` 的目录式 Skill。

```shell
git clone https://github.com/richard26616-bit/TRMesh.git
cd TRMesh
```

将选中的 **整个 Skill 目录**复制到客户端的技能目录，保留 `references/`、`scripts/` 和 `examples/`。不要只复制 `SKILL.md`。例如在 Codex 的个人 Skill 目录安装：

```powershell
Copy-Item -LiteralPath .\agent-skills\douyin-search `
  -Destination (Join-Path $HOME '.codex\skills\douyin-search') -Recurse
```

如果该目录已存在，先对照版本并保留自己的改动。其他 Agent 客户端请使用其文档规定的 Skill 路径。安装后在对话中指定 `$douyin-search` 或直接描述“查询抖音指定关键词的作品”。

Skill 为独立目录，不依赖根目录的 Python 模块，单独安装也能调用。停用的两个旧目录不要安装。

## 配置与第一次运行

在执行 Agent 的进程中设置：

```powershell
$env:TRMESH_BASE_URL = 'https://your-trmesh-gateway.example'
$env:TRMESH_API_TOKEN = '<your-developer-token>'
$env:PYTHONIOENCODING = 'utf-8'
```

`TRMESH_BASE_URL` 是 TRMesh 网关**根地址**，不含 `/openapi`、查询串或凭据。公开服务器必须使用 HTTPS；本地开发允许 `http://127.0.0.1:5207`。认证使用 TRMesh 开发者 Token。环境变量由运行进程读取，不提交到 Git。

以抖音搜索为例：

```powershell
Set-Location .\agent-skills\douyin-search
Copy-Item -LiteralPath .\examples\body.json -Destination .\body.json
python scripts/client.py --describe
python scripts/client.py --endpoint douyin-search-fetch_video_search_v5 --body-file body.json --dry-run
```

修改 `body.json` 中的关键词后，确认计划和请求预算，去掉 `--dry-run` 才会执行数据请求：

```shell
python scripts/client.py --endpoint douyin-search-fetch_video_search_v5 --body-file body.json
```

当前抖音搜索 V5 是 **POST JSON**；固定每页 10 条。下一页需要回传真实响应的 `offset`、`search_id`、`backtrace` 并递增 `page`，不能添加通用 `limit`。每个 Skill 的参考文件都记录对应接口的真实参数与分页规则。

## 每个 Skill 包含什么

```text
agent-skills/<name>/
├── SKILL.md                  # 触发条件、执行流程、预算、输出与边界
├── references/
│   ├── api.md                # 方法、参数表、分页、响应 Schema 与官方说明
│   └── contracts.json        # 精确 query/body Schema、枚举与标识符要求
├── scripts/client.py         # 独立调用器；白名单路径；不自动重试
└── examples/                 # 按 endpoint key 区分的请求格式示例
```

根目录还提供：

- `catalog/`：Skill 目录、1,050 个注册接口索引、逐项场景映射及契约快照哈希。
- `tools/`：可复现生成器、经过审查的任务配方、离线校验器与调用器模板。
- `docs/`：安装、成本、能力边界、接口同步、迁移与验证结果。
- `.github/workflows/`：跨平台静态检查，以及手动／每周执行的契约快照变化检测。

## 能力边界

- **搜索与榜单**：搜索结果排名是当前样本排序；平台官方榜单保留原榜名、指标单位与原排名。跨平台 Top10 为注明选择规则的编辑聚合。
- **增长与订阅**：增长必须有真实趋势数据或两个同口径快照。首次执行只建立基线；持续订阅需要另外配置调度器。
- **媒体**：历史 `*-downloader` 名称兼容保留，实际能力为媒体链接／元数据提取。调用器不下载 CDN 文件、不解密、不合并音视频；地址缺失或过期时明确报告。
- **创作与评分**：文字创作由 Agent 根据用户事实和参考样本完成；分数是编辑规则下的分析，不是平台流量预测。没有内容发布能力。
- **不支持**：图片／视频生成、OCR、Kimi／Deepseek／豆包搜索、金融分析、权威违禁词检测等均没有对应注册接口，见完整 [映射报告](docs/capability-coverage.md)。

## 校验与维护

```shell
python tools/validate_skills.py . --report docs/validation.json
```

校验所有 Skill 的目录、触发声明、引用、白名单、契约、请求示例和场景映射，并测试参数拒绝、嵌套 Schema、网关地址限制及重定向凭据保护。此命令不会调用数据服务。

带原始契约快照的完整对照：

```shell
python tools/validate_skills.py . --spec /path/to/contract-snapshot.json
```

当前快照哈希见 [catalog/source.json](catalog/source.json)。契约变化时校验会报错，要求人工审查差异；不自动修改接口价格、上线状态或 Skill。

按 [维护指南](docs/maintenance.md) 更新接口与配方，按 [贡献指南](CONTRIBUTING.md) 提交改动。生成结果、可读说明和后台绑定必须来自同一契约版本。

## 许可

所有 Skill 统一调用 TRMesh 网关的已注册接口，使用 TRMesh 开发者 Token。

本项目原创代码与说明使用 [MIT License](LICENSE)。接口访问权限、额度、计费和限流以 TRMesh 网关配置为准。
