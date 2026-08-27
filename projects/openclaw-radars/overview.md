# OpenClaw 雷达体系总览

## 目标

把服务器雷达从分散脚本收敛为一套可解释的机会发现系统：

`先导信号 → 分发结构变化 → 高意图需求/供给真空 → 商业机会排序 → 付款验证`

它只负责发现、证据聚合和实验优先级，不以高分直接授权开发。

## 总体处理链

```text
官方源 / SEC / Marketplace / Reddit / SERP / 公开网络
                         ↓
                  去重与规则预筛
                         ↓
          纯规则打分 或 Codex 语义研判
                         ↓
          门槛判定与 TEST/WATCH/REJECT
                         ↓
               JSON + HTML + SMTP
                         ↓
      Fake-door / 人工交付 / 不可退款可抵扣 Deposit
```

## 雷达分层与职责

| 层级 | 雷达 | 回答的问题 | 方法 | 输出边界 |
|---|---|---|---|---|
| **Level 1 生产函数** | Tech Discontinuity | 底层成本/性能是否发生数量级断裂？ | arXiv + HN + LLM；成本 `>=80%` 下降或性能 `>=10x` 提升 | 只标记“值得长期追踪”，不判断当下变现 |
| **Level 2 资本承诺** | Capital Signals | 聪明资本是否开始用 CapEx、订单和 Backlog 抢筹？ | SEC EDGAR + 卖铲人定向监控 + LLM | 判断资本方向和领先时间，不等同市场入口已开放 |
| **Level 3 平台开闸** | Band 1 Daily Sniff | 巨头、政策或平台是否刚释放新流量/新成本结构？ | RSS、Apify、DataForSEO、SEC；关键词矩阵 + LLM | `score >= 7.5` 且可行动才发预警 |
| **分发供给真空** | Band 2 Parasite SEO | 高意图需求是否由 Reddit/Quora 占据 SERP，而没有独立产品承接？ | Apify + DataForSEO，纯规则 | Top 3 全为 UGC 域名即黄金命中 |
| **搜索长尾资产** | Band 2 pSEO | 是否存在低 KD、有 CPC、可规模化交付的极冷长尾？ | Keyword Suggestions + Search Volume + KD + SERP | 月度词包，不等于产品需求已付款验证 |
| **宿主生态原始层** | Band 3 Raw Snapshot | 应用/插件市场今天出现了什么新供给和榜单样本？ | Chrome/Shopify/Product Hunt 原始抓取 | 不做最终机会审批，作为观察与后续研判输入 |
| **分发商业机会层** | Opportunity Distribution Weekly | 哪个“新增分发 × 新行为 × 新需求”最值得本周测试？ | 独立公开研究 + `DIS/SOS/ACR` | `TEST/WATCH/REJECT`；必须给 Asset Capture 与 Escape Path |
| **泛工具机会层** | GPT Business Opportunity Weekly | 哪个工具型任务具备需求、分发、付费与标准化交付的乘积优势？ | 独立公开研究 + 七因子机会值 | `BUILD_TEST/OBSERVE/REJECT`；当前只允许手动运行 |

## 各雷达核心逻辑

### 1. RadarBand1DailySniff

**监控对象**：TikTok、Amazon、Google、Meta、Shopify 等巨头的新地区、新入口、补贴，以及关税、VAT、EPR 等主权合规断裂。

**主要数据源**：

- Google Search Central、Shopify Changelog、US Federal Register、EU Trade Policy RSS；
- Amazon Global Selling Announcements（Apify JS 渲染）；
- DataForSEO News 的 10 组扩张/补贴/合规查询；
- Amazon、Meta、Alphabet、Shopify、PDD Holdings 的 SEC EDGAR filings；
- Chrome Web Store、Shopify App Store、Product Hunt 的应用市场候选。

**判定链**：

1. `md5(link + title)` 去重；
2. 命中“扩张词 + 补贴词”，或单独命中主权/合规词，才进入研判；
3. Codex 判断触发类别、窗口半衰期、可行动性与 0–10 分；
4. `score >= 7.5`、`is_actionable=true` 且类别有效时发邮件；否则静默。

### 2. RadarBand3RawSnapshotEmail

这是**原始数据快照**而非最终评分雷达：

- Chrome Web Store Top Charts：30 条；
- Shopify App Store：`selling-products` 分类页；
- Product Hunt Daily：Top 10。

价值在于保留榜单现场，降低后续算法过滤导致的漏报；因此每天固定发信，不以评分门槛决定是否发送。

### 3. RadarBand2Parasite-*

四个 subreddit 被拆为独立任务，避免大社区抓取超时拖垮整批流程。

**规则**：

1. 抓取含 `How to`、`Best tool for`、`Alternative to`、`Is there an app that` 的近期帖子；
2. 正则提取任务型 query，不调用 LLM；
3. 查询 Google SERP；
4. 如果 Top 3 全部属于 Reddit/Quora，判定“有意图、无专业产品承接”；
5. 补齐 Search Volume 与 KD，计算套利指数并排序；
6. 单社区结束即落 checkpoint，有命中立即发信，失败也独立告警。

**套利指数**：

`Search Volume × Intent Weight ÷ (KD × SERP Competitor Strength) × Growth Rate`

- `buy/pricing/software/alternative`：Intent Weight = `2.0`；其他 = `0.5`；
- Top 3 全为 Reddit/Quora：竞争强度 = `0.5`；含 G2/Forbes 等强站 = `3.0`；其他 = `1.5`；
- 当前未接 Trends，Growth Rate 固定为 `1.0`。

### 4. RadarBand2PseoMonthly

从 `convert / download / format / vs / generator / calculator` 六个种子扩展关键词，严格过滤：

```text
30 <= Search Volume <= 500
KD <= 15
CPC > 0.5
keyword 包含 vs / alternative / tool
```

Top 25 再做 SERP 竞争强度核验。其作用是沉淀可复用的 Search Intent 与 pSEO 资产，不承担付款验证。

### 5. OpportunityDistributionRadarWeekly

**机会表达单元**：

`分发市场新增量 × 渠道用户 × 触发行为 × 新配套需求 × Channel-native Solution × 首个入口 × 变现 × 自有资产`

**评分**：

- `DIS`：用户/入口增量、聚集度、自然曝光、商业意图、交易设施、资产导出，除以拥挤与平台风险；
- `SOS`：需求、付费、新工作流缺口、入口精度、标准化、复利，除以竞争成本；
- `ACR`：直接触达、第一方数据、品牌、跨渠道迁移、客户/伙伴关系的资产捕获率；
- `Distribution Opportunity Index = DIS × SOS × ACR / 100`。

`TEST` 至少要求：Confidence `>=70%`、近期新增分发证据、两条独立需求证据、明确入口、付费证据和可执行 Asset Capture。

### 6. GPTBusinessOpportunityWeekly

**覆盖工具形态**：Calculator、Generator、Converter、Auditor、Analyzer、Micro AI Tool、Business Document Tool、Workflow Utility、Chrome Extension、轻量 API。

**排除**：Career/Resume/Recruiting、通用无差异 Converter、重后台 SaaS、灰产、侵权、隐私高风险及强监管决策工具。

**机会值**：

`Opportunity Value = D × A × G × P × S × L ÷ C`

- `D` 需求强度；`A` 需求聚集度；`G` 分发可获得性；
- `P` 付费能力；`S` 交付标准化；`L` 复利潜力；`C` 竞争成本；
- Evidence Confidence 独立计算：来源质量、独立覆盖、时效性、七因子证据完整度各占 25%。

`BUILD_TEST` 只代表应测试 Offer/Fake-door/Deposit，不代表批准开发；`PRODUCTIZE` 必须已有真实付款与重复交付。

### 7. Tech Discontinuity（未定时）

- 数据源：arXiv 最新 30 篇 + Hacker News Top 50 中保留前 25；
- 评分：Breakthrough Magnitude、Credibility、Spillover Potential；
- 硬门槛：成本暴跌 `>=80%` 或性能提升 `>=10x`；缺少数字时以严肃圈层的异常讨论热度做代理；
- 当前缺口：GitHub Trending 与硬件成本历史快照尚未接入。

### 8. Capital Signals（未定时）

- 全市场：SEC EDGAR 全文检索 8-K/10-Q，关注 CapEx、data center、billion investment、capacity expansion；
- 定向“卖铲人”：NVIDIA、ASML、TSMC 最新 filings；
- 评分：Capital Conviction、Directional Clarity、Lead Time；
- 当前缺口：S-1 未盈利上市、并购溢价、Payoneer/PingPong 资金通路尚未接入。

## 决策与资产边界

1. **信号不等于机会**：Level 1/2 高分只能进入观察清单。
2. **机会不等于开发授权**：`TEST` 或 `BUILD_TEST` 的下一步是付费验证。
3. **付款是 Gate**：真实付款或不可退款、可抵扣 Deposit 才能推动重开发。
4. **必须可逃逸**：优先能把平台流量转成 Email、第一方数据、品牌、客户或伙伴关系的机会。
5. **任务间保持独立**：两个周报不得读取其他雷达输出，避免同源偏差和循环强化。

## 邮件可解释性规范

所有雷达邮件必须在**最底部**显示“本雷达的判断逻辑”，固定说明：目标、数据源、筛选/评分、触发条件、运行时间与决策边界。

- Python 直跑雷达在 HTML 构建函数中追加确定性 Footer；
- Opportunity Distribution Weekly 与 GPT Business Opportunity Weekly 由外层 runner 在发信前注入 Footer，并用固定 ID 防止重复；
- Band 2 Parasite SEO 的正常命中邮件和失败告警邮件使用同一逻辑说明；
- Footer 只解释规则，不暴露 SMTP、API、SSH 或收件配置。

## 相关方法论文档

- `thinking/business/distribution-radar-framework.md`：四波段概念框架；
- `thinking/business/distribution-radar-engineering-sop.md`：DataForSEO + Apify 工程 SOP；
- `thinking/business/radar-band-one-data-sources-and-ops.md`：波段一数据源与运行策略；
- `thinking/business/radar-band-one-engineering-spec.md`：波段一研判规则与实现规范；
- `thinking/business/leading-indicators-of-emerging-opportunities.md`：技术 → 资本 → 边缘行为 → 平台开闸 → 大众相变的先导指标级联模型；
- `thinking/business/detecting-level-1-technological-discontinuity.md`：Level 1 技术断裂识别方法。

## 隐私与同步边界

GitHub 只保存名称、逻辑、时间、状态、非敏感脚本定位和决策规则；服务器地址、SSH 私钥、SMTP 授权码、API Token、Cookie、完整收件配置均不得提交。
