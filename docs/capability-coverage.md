# Redfox场景逐项能力映射

参考公开Skills广场的使用场景，独立编写TRMesh执行流程，不复制其正文或调用第三方工具。共121项。

direct=对应数据直接获取；composed=数据+本地分析/创作；partial=仅满足部分功能，必须看限制；unsupported=没有注册能力，不发布假实现。下载类为媒体链接提取，增长类需真实趋势或两次快照。

| 参考场景 | 状态 | TRMesh Skill | 边界 |
| --- | --- | --- | --- |
| `tiktok-topic-aweme-list` | direct | [`tiktok-topic-aweme-list`](../agent-skills/tiktok-topic-aweme-list/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `twitter-work-search` | direct | [`twitter-work-search`](../agent-skills/twitter-work-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `x-subscribe` | composed | [`x-account-brief`](../agent-skills/x-account-brief/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `x-entrepreneur-rank` | partial | [`x-candidate-research`](../agent-skills/x-candidate-research/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `x-top-account` | partial | [`x-candidate-research`](../agent-skills/x-candidate-research/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `gzh-toutiao-growth-rank` | partial | [`wechat-fastest-growing`](../agent-skills/wechat-fastest-growing/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-account-diagnosis` | composed | [`douyin-account-diagnosis`](../agent-skills/douyin-account-diagnosis/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-fastest-growing` | partial | [`wechat-fastest-growing`](../agent-skills/wechat-fastest-growing/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-video-downloader` | partial | [`xiaohongshu-video-downloader`](../agent-skills/xiaohongshu-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `image-gen` | unsupported | — | 未注册 GPT-image2 图片生成接口。 |
| `visual-ops-writer` | unsupported | — | 图文创作中的图片生成功能没有注册接口；文字创作可用各平台写作 Skill。 |
| `douyin-search` | direct | [`douyin-search`](../agent-skills/douyin-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-search` | direct | [`wechat-search`](../agent-skills/wechat-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-search` | direct | [`xiaohongshu-search`](../agent-skills/xiaohongshu-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `pdf-image-text-extractor` | unsupported | — | 未注册 PDF 解析或 OCR 接口。 |
| `gzh-astock-top` | unsupported | — | 没有可信 A 股大 V 榜单来源；公众号搜索不等于股票权威排名。 |
| `stock-analysis` | unsupported | — | 没有行情、交易与财报接口，无法完成该股票分析契约。 |
| `investor-distiller` | unsupported | — | 缺少投资策略与历史收益验证数据；不能把文章风格分析包装为策略验证。 |
| `gzh-search-crawler` | direct | [`gzh-search`](../agent-skills/gzh-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-inspiration` | composed | [`xiaohongshu-inspiration`](../agent-skills/xiaohongshu-inspiration/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-creator` | composed | [`xiaohongshu-write`](../agent-skills/xiaohongshu-write/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-creator` | composed | [`wechat-write`](../agent-skills/wechat-write/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-account-analyzer` | composed | [`wechat-account-analyzer`](../agent-skills/wechat-account-analyzer/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-works-crawler` | direct | [`douyin-works-crawler`](../agent-skills/douyin-works-crawler/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-original-hot` | partial | [`wechat-original-hot`](../agent-skills/wechat-original-hot/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-10w-hot` | partial | [`wechat-10w-hot`](../agent-skills/wechat-10w-hot/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `global-ai-news-brief` | composed | [`multi-content-feed`](../agent-skills/multi-content-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `playlet-douyin-feed` | composed | [`playlet-douyin-feed`](../agent-skills/playlet-douyin-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `playlet-wechat-feed` | composed | [`playlet-wechat-feed`](../agent-skills/playlet-wechat-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `playlet-bili-feed` | composed | [`playlet-bili-feed`](../agent-skills/playlet-bili-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `weibo-comment-search` | direct | [`weibo-comment`](../agent-skills/weibo-comment/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `weibo-realtime-search` | direct | [`weibo-search`](../agent-skills/weibo-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `weibo-hot-search` | direct | [`weibo-hot-topic-radar`](../agent-skills/weibo-hot-topic-radar/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `weibo-post-search` | composed | [`weibo-account-monitor`](../agent-skills/weibo-account-monitor/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `kuaishou-video-extract` | partial | [`kuaishou-caption-extract`](../agent-skills/kuaishou-caption-extract/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `kuaishou-search` | direct | [`kuaishou-search`](../agent-skills/kuaishou-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-account-analyzer` | composed | [`xiaohongshu-account-analyzer`](../agent-skills/xiaohongshu-account-analyzer/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `gzh-subscribe` | composed | [`gzh-subscribe`](../agent-skills/gzh-subscribe/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-similar-account` | partial | [`douyin-similar-account`](../agent-skills/douyin-similar-account/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `tiktok-home-downloader` | partial | [`tiktok-video-downloader`](../agent-skills/tiktok-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-channels-crawler` | composed | [`wechat-channel-brief`](../agent-skills/wechat-channel-brief/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-similar-account` | partial | [`wechat-similar-account`](../agent-skills/wechat-similar-account/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-subscribe` | composed | [`douyin-subscribe`](../agent-skills/douyin-subscribe/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-similar-account` | partial | [`xiaohongshu-similar-account`](../agent-skills/xiaohongshu-similar-account/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `account-video-downloader` | partial | [`account-video-downloader`](../agent-skills/account-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `bilibili-search-download` | direct | [`bilibili-search-download`](../agent-skills/bilibili-search-download/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `overseas-trending-search` | direct | [`overseas-trending-search`](../agent-skills/overseas-trending-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `youtube-comment` | direct | [`youtube-comment`](../agent-skills/youtube-comment/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-video-downloader` | partial | [`douyin-video-downloader`](../agent-skills/douyin-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `twitter-comment` | direct | [`twitter-comment`](../agent-skills/twitter-comment/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `geo-analyzer` | unsupported | — | 没有多模型答案采样、搜索引擎排名或品牌引用评估接口。 |
| `video-downloader` | partial | [`video-downloader`](../agent-skills/video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-cover` | unsupported | — | 未注册图片生成接口；不能生成实际封面文件。 |
| `wechat-write` | composed | [`wechat-write`](../agent-skills/wechat-write/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-top-account` | partial | [`xiaohongshu-top-account`](../agent-skills/xiaohongshu-top-account/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `bilibili-video-downloader` | partial | [`bilibili-video-downloader`](../agent-skills/bilibili-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `tiktok-video-downloader` | partial | [`tiktok-video-downloader`](../agent-skills/tiktok-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `youtube-video-downloader` | partial | [`youtube-video-downloader`](../agent-skills/youtube-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `instagram-video-downloader` | partial | [`instagram-video-downloader`](../agent-skills/instagram-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-video-downloader` | partial | [`wechat-video-downloader`](../agent-skills/wechat-video-downloader/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `twitter-video-downloader` | partial | [`x-video-extract`](../agent-skills/x-video-extract/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `kuaishou-comment` | direct | [`kuaishou-comment`](../agent-skills/kuaishou-comment/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-channels-ai-feed` | composed | [`wechat-channels-ai-feed`](../agent-skills/wechat-channels-ai-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `youtube-digest` | partial | [`youtube-digest`](../agent-skills/youtube-digest/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `gzh-ai-feed` | composed | [`gzh-ai-feed`](../agent-skills/gzh-ai-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-ai-feed` | composed | [`xiaohongshu-ai-feed`](../agent-skills/xiaohongshu-ai-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-ai-feed` | composed | [`douyin-ai-feed`](../agent-skills/douyin-ai-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `cultural-tourism-xiaohongshu-feed` | composed | [`cultural-tourism-xiaohongshu-feed`](../agent-skills/cultural-tourism-xiaohongshu-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `cultural-tourism-wechat-feed` | composed | [`cultural-tourism-wechat-feed`](../agent-skills/cultural-tourism-wechat-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `cultural-tourism-douyin-feed` | composed | [`cultural-tourism-douyin-feed`](../agent-skills/cultural-tourism-douyin-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `cultural-tourism-bilibili-feed` | composed | [`cultural-tourism-bilibili-feed`](../agent-skills/cultural-tourism-bilibili-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `bilibili-portfolio-search` | direct | [`bilibili-portfolio-search`](../agent-skills/bilibili-portfolio-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `bilibili-comment` | direct | [`bilibili-comment`](../agent-skills/bilibili-comment/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wecht-copywrite-alchemy` | composed | [`wechat-reference-rewrite`](../agent-skills/wechat-reference-rewrite/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `multi-copywrite-alchemy` | composed | [`multi-reference-rewrite`](../agent-skills/multi-reference-rewrite/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-copywrite-alchemy` | composed | [`douyin-reference-rewrite`](../agent-skills/douyin-reference-rewrite/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `ai-intelligence-investigator` | unsupported | — | 缺少行情、上市公司公告与金融数据核验接口。 |
| `redfox-skill-generator` | unsupported | — | 第三方平台的 Skill 生成服务未注册；本仓库提供本地生成维护工具。 |
| `kimi-websearch` | unsupported | — | 未注册 Kimi 搜索接口。 |
| `xiaohongshu-title-score` | composed | [`xiaohongshu-title-score`](../agent-skills/xiaohongshu-title-score/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `video-prompt-expert` | unsupported | — | 没有 Seedance 提示词验证与生成接口；模型专用效果无法验证。 |
| `playlet-xiaohongshu-feed` | composed | [`playlet-xiaohongshu-feed`](../agent-skills/playlet-xiaohongshu-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `multi-wordcheck` | unsupported | — | 没有平台权威违禁词库或审核接口，不能提供该检测能力。 |
| `multi-content-feed` | composed | [`multi-content-feed`](../agent-skills/multi-content-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `deepseek-websearch` | unsupported | — | 未注册 Deepseek 搜索接口。 |
| `kuaishou-ai-feed` | composed | [`ks-ai-feed`](../agent-skills/ks-ai-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `bilibili-ai-feed` | composed | [`bili-ai-feed`](../agent-skills/bili-ai-feed/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `toutiao-search` | unsupported | — | 最新版 TikHub 的今日头条没有关键词搜索接口；保留链接文章解析替代项。 |
| `stock-feed` | unsupported | — | 没有股市行情及官方公告数据源；社交帖子不等于金融新闻核验。 |
| `doubao-websearch` | unsupported | — | 未注册豆包搜索接口。 |
| `xiaohongshu-cover` | unsupported | — | 未注册图片生成接口；该旧入口下线，文字选题不等于封面生成。 |
| `cn-last30days` | composed | [`cn-last30days`](../agent-skills/cn-last30days/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `seedream-5-lite` | unsupported | — | 未注册 Seedream 图片生成接口。 |
| `seedance-video-gen` | unsupported | — | 未注册 Seedance 视频生成接口。 |
| `optimize-skill-md` | unsupported | — | 不属于已注册数据 API 能力，本仓库维护指南覆盖静态校验。 |
| `douyin-daily-hot` | partial | [`douyin-daily-hot`](../agent-skills/douyin-daily-hot/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-write` | composed | [`xiaohongshu-write`](../agent-skills/xiaohongshu-write/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-weeklytop` | partial | [`xiaohongshu-weeklytop`](../agent-skills/xiaohongshu-weeklytop/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `trending-hub-top10` | direct | [`trending-hub-top10`](../agent-skills/trending-hub-top10/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-top-account` | partial | [`douyin-top-account`](../agent-skills/douyin-top-account/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `trending-hub` | direct | [`trending-hub`](../agent-skills/trending-hub/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-top-account` | partial | [`wechat-top-account`](../agent-skills/wechat-top-account/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-hot-trend` | direct | [`douyin-hot-trend`](../agent-skills/douyin-hot-trend/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-dailytop` | partial | [`xiaohongshu-dailytop`](../agent-skills/xiaohongshu-dailytop/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-prohibited-word` | unsupported | — | 没有抖音官方词库或内容审核接口。 |
| `wechat-prohibited-word` | unsupported | — | 没有微信官方词库或内容审核接口。 |
| `xiaohongshu-prohibited-word` | unsupported | — | 没有小红书官方词库或内容审核接口。 |
| `multi-rewrite` | composed | [`multi-reference-rewrite`](../agent-skills/multi-reference-rewrite/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-rewrite` | composed | [`wechat-reference-rewrite`](../agent-skills/wechat-reference-rewrite/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xhs-title-scorer` | composed | [`xiaohongshu-title-score`](../agent-skills/xiaohongshu-title-score/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-note-analyzer` | composed | [`xiaohongshu-note-analyzer`](../agent-skills/xiaohongshu-note-analyzer/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-rewrite` | composed | [`xiaohongshu-reference-rewrite`](../agent-skills/xiaohongshu-reference-rewrite/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `zhihu-rewrite` | composed | [`zhihu-reference-rewrite`](../agent-skills/zhihu-reference-rewrite/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `wechat-title` | composed | [`wechat-title`](../agent-skills/wechat-title/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-content-surge` | partial | [`douyin-content-surge`](../agent-skills/douyin-content-surge/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-weekly-surge` | partial | [`douyin-weekly-surge`](../agent-skills/douyin-weekly-surge/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `douyin-rise-ranking` | partial | [`douyin-rise-ranking`](../agent-skills/douyin-rise-ranking/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-crawler` | direct | [`xiaohongshu-crawler`](../agent-skills/xiaohongshu-crawler/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `xiaohongshu-lowtop` | partial | [`xiaohongshu-lowtop`](../agent-skills/xiaohongshu-lowtop/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `bilibili-keywords-search` | direct | [`bilibili-keywords-search`](../agent-skills/bilibili-keywords-search/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
| `bilibili-keyword-account` | composed | [`bilibili-keywords-accounts`](../agent-skills/bilibili-keywords-accounts/SKILL.md) | 支持数据获取与本地分析；按目标Skill的采样、快照、媒体或模型分析边界执行。 |
