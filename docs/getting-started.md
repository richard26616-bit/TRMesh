# 安装与调用指南

## 1. 选择并完整安装

从 `agent-skills/README.md` 选择可安装 Skill，将整个目录复制至 Agent 支持的 Skill 目录。安装路径由客户端决定；目录内的调用器不依赖仓库根目录。Python最低版本3.10。

不要安装 `toutiao-search` 和 `xiaohongshu-cover`，它们是迁移说明。

## 2. 准备网关

部署TRMesh服务端，在后台核对需要的接口已注册、active、online；当前开发者Token有访问权限和足够额度。公开市场可见性由运营控制，不因安装Skill自动改变。

本仓库不提供网关服务器，不会把官方1,050接口自动上线。新增接口导入保持草稿，先审查价格、限流和权限，再上线。

## 3. 配置环境

PowerShell：

```powershell
$env:TRMESH_BASE_URL = 'https://your-gateway.example'
$env:TRMESH_API_TOKEN = '<developer-token>'
$env:PYTHONIOENCODING = 'utf-8'
```

macOS／Linux：

```shell
export TRMESH_BASE_URL='https://your-gateway.example'
export TRMESH_API_TOKEN='<developer-token>'
export PYTHONIOENCODING='utf-8'
```

不要将变量值粘贴到Skill、请求JSON或提交记录。调用器不会读取TikHub密钥、GitHub PAT、后台登录会话或支付密钥。

## 4. 了解真实参数

进入Skill目录，执行 `python scripts/client.py --describe`，或阅读 `references/api.md`。每个操作有唯一的endpoint key。GET填query文件；POST填body文件；字段名、类型、枚举不能用其他版本的接口替代。

示例文件是格式说明，不是实时验证结果。将示例中的目标ID、用户名和链接改为用户实际目标；如果标识符需要从搜索结果获得，先检索并核验对象。

## 5. 先预览再执行

```shell
python scripts/client.py --endpoint <key> --query-file query.json --dry-run
python scripts/client.py --endpoint <key> --body-file body.json --dry-run
```

预览只构造请求，不读取Token、不联网、不计费。真实执行时去掉`--dry-run`。若同时存在query和body参数，两个文件都传入；没有该位置参数时不提供文件。

脚本从环境读取网关根地址并拼接`/openapi/api/v1/...`，Token仅放在Authorization请求头。脚本不接受任意路径或外部URL参数。

## 6. 让Agent完成分析

例如：“使用 `$wechat-search` 查询新能源行业文章，最多三次请求，输出样本链接和发布时间。”“使用 `$douyin-account-diagnosis` 分析这个账号近20条作品，不计算缺少分母的互动率。”

输出应包含采集时间、样本范围、原始证据和缺失字段。当前数据与模型建议分开；不能将样本趋势扩展为平台全体结论。

## 常见故障

| 现象 | 处理 |
| --- | --- |
| required / unknown field | 对照该endpoint的querySchema/bodySchema，避免通用target字段或错误版本 |
| 必须提供某个ID | 用户提供唯一标识，或从真实搜索结果解析；不能伪造 |
| 401 / 403 | 核验开发者Token、权限、账号状态及接口上线状态 |
| 404 | 核对路径、HTTP方法与对象ID；GET/POST变更见同步报告 |
| 429 | 检查限流与Usage；按部署策略决定下次执行时间 |
| 5xx / 超时 | 先查Usage和请求状态，确认是否已调用与计费，再决定重试 |
| 没有字幕／媒体URL | 如实说明能力缺口；不编造文本或下载文件 |
| HTTPS地址错误 | 根地址不含/openapi、凭据、query或fragment；HTTP仅支持loopback |

即使HTTP成功，也要依据该接口参考检查业务状态和返回结构。源契约未给出业务字段时，只解释实际收到的字段，不套用另一接口的响应字段。
