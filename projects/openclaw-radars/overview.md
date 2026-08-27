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
| **Level 2 资本承诺** | Capital Signals（dormant，被 AICapitalFlow 取代） | 聪明资本是否开始用 CapEx、订单和 Backlog 抢筹？ | SEC EDGAR + 卖铲人定向监控 + LLM | 判断资本方向和领先时间，不等同市场入口已开放 |
| **Level 2 资本承诺 · AI 专版** | AICapitalFlow | AI ~14 子领域的聪明钱处在资本信号 8 阶段曲线的哪一段？大企业行为路径反推出什么势差？ | SEC EDGAR Form D + DataForSEO Google News + lab RSS（Apify-free）+ Claude Code | 只标资本方向、阶段与领先时间；资本信号 ≠ 机会 ≠ 开发授权 |
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

这是**原始数据快照**而非最终评分雷达。每天固定发信，不以评分门槛决定是否发送；保留榜单现场，降低算法过滤漏报。

源（前三个走 Apify，后四个 2026-08-27 新增，全部 Apify-free，带「相对昨日 baseline 的新增高亮」）：

| 源 | 取法 | 状态 |
|---|---|---|
| Chrome Web Store Top Charts 30 | Apify `crawlerbros/chrome-extensions-scraper-pro` | ok |
| Shopify App Store `selling-products` 分类页 | Apify `website-content-crawler` | ok |
| Product Hunt Daily Top 10 | Apify `muzafferkadir/product-hunt-leaderboard` | ok |
| **VS Code 扩展市场**（搜 `ai`，安装量 Top 30） | 官方 Gallery API `extensionquery`，无 auth | 实测 30 条 |
| **MCP servers** Top 40 | PulseMCP `api.pulsemcp.com/v0beta/servers` | 实测 40 条 |
| **Raycast** 最近 30 | GitHub commits API `raycast/extensions`（无稳定 Store API，取仓库近况） | 实测 30 条 |
| **GPT Store** | 无官方 API + ChatGPT 登录墙，保留 stub | 待接入第三方稳定源 |

baseline 存 `data/band3_baseline_<src>.json`，逐源 diff 出 `🆕` 新增行。

### 3. Band4Vacuum-*（原 RadarBand2Parasite-*）

四个 subreddit 拆为独立任务避免超时拖垮整批。**2026-08-27：subreddit 由电商组切到 AI 组 `SaaS / LocalLLaMA / AI_Agents / OpenAI`；抓取预算 300s；SERP 核验上限 Top 20；cron 更名 `Band4Vacuum-*`（ID 不变）。**

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

### 6. GPTBusinessOpportunityWeekly —— 已退役（2026-08-27）

品类（独立计算器 / 转换器 / micro tool）正被 LLM 内联回答吞没，且它是综合器、与 ODRW 角色重复。task 目录移入 `deleted-radars/`。`Opportunity Value = D × A × G × P × S × L ÷ C` 这个工具机会打分法保留为 ODRW 的可选 lens。

### 7. Tech Discontinuity（每天 05:10）

- 数据源：arXiv 最新 30 篇 + Hacker News Top 50 中保留前 25；
- 评分：Breakthrough Magnitude、Credibility、Spillover Potential；
- 硬门槛：成本暴跌 `>=80%` 或性能提升 `>=10x`；缺少数字时以严肃圈层的异常讨论热度做代理；
- 调度：每天 05:10（Asia/Shanghai），只对去重后的新增候选调用 Codex；任务超时 30 分钟；
- 当前缺口：GitHub Trending 与硬件成本历史快照尚未接入。

### 8. Capital Signals（未定时）

- 全市场：SEC EDGAR 全文检索 8-K/10-Q，关注 CapEx、data center、billion investment、capacity expansion；
- 定向“卖铲人”：NVIDIA、ASML、TSMC 最新 filings；
- 评分：Capital Conviction、Directional Clarity、Lead Time；
- 状态：dormant，已被 `AICapitalFlow` 取代，待退役。

### 9. AICapitalFlow（每日 05:05，Claude Code 执行）

- **数据源（Apify-free）**：`collect.py` = DataForSEO Google News（融资 / M&A / lab 发布 / 巨头 AI 组织 12 组查询）+ SEC EDGAR Form D（每笔美国私募轮 15 天内必报）+ lab 博客 RSS（Sherlocking 检测）；md5 去重、跨日 `state/seen.json`、硬上限 140 条。
- **研判**：一次隔离的 Claude Code turn 跑 `collect.py` → 把每条事件归入 14 子领域、定位资本信号 8 阶段（①窗口前聪明钱 ②首笔大退出 ③洪水 ④轮动到 infra ⑤平台征税/Sherlocking ⑥并购整合+洗牌 ⑦结构性冲击 ⑧后增长）→ 对实质事件写「新闻 → 反推大企业行为路径 → 势差判断（给谁 / 在位者反身位 / 具体 wedge / 风险）」。
- **实质事件阈值**：≥$100M 轮 / 任何 M&A / hyperscaler 或 lab 的 AI 组织或 capex 公告 / 可能 sherlock 某子领域的 lab 发布 / 主权或战略资本出手 / 近 7 日某子领域关停 ≥3 / 任一子领域跨阶段。
- **发信策略**：有实质事件才发；无事件的非周一静默；周一必发 14 子领域全量阶段表。`delivery.mode=none`，`run-claude.sh` 注入确定性逻辑 Footer 后经共享 `send-email.py` 走 QQ SMTP。
- **成本**：Apify 0；DataForSEO ≈12 credits/天；Claude Code token 静默日 ~3–8K、发信日 ~30–80K。
- **决策边界**：资本信号 ≠ 机会 ≠ 开发授权；只标资本方向、阶段与领先时间。

### 10. Band2MediumShift（波段二 · 周三 11:00 周报 + 每日 05:20 规则哨，Claude Code 执行）

- **目的**：搜索介质多快从 Google 蓝链迁到答案引擎，谁在新介质里拿引用位；聚焦 AI 工具 / 互联网注意力场。
- **数据源（Apify-free）**：`collect.py weekly` = DataForSEO SERP `organic/live/advanced`（80 词 · `load_async_ai_overview` · 组 1–6 战场 + 组 7 消费科技校准锚）+ 引用域名 churn（vs `state/citation_baseline.json`）+ DataForSEO AI Optimization/LLM Responses（答案引擎引用，~15 词）+ DataForSEO News + RSS（Google Search Central / Bing Webmaster / OpenAI / Google / seroundtable）。`collect.py sniff` 只跑 News + RSS。
- **头条读数**：组 1–6 AI Overview 覆盖率环比（pt）+ 组 1–6 减组 7 的覆盖率差 + 引用源 entered/exited/集中度。
- **发信**：周报每周三固定发；日哨仅在出现实质 AI 搜索规则变化时发。
- **成本**：Apify 0；DataForSEO ~$2–2.5/月；token 周报 ~30–60K、日哨 ~3–5K。

### 11. Band4RegBreak（波段四 · 每日 05:25 规则断裂哨，Claude Code 执行）

- **目的**：AI / 科技 / 平台的监管与规则变化——一条规则让某种新打法从不可行变可行或反之。跨境关税 / VAT / EPR 留波段一。
- **数据源（Apify-free）**：`collect.py` = RSS（Federal Register · AI rules（RULE/PRORULE + 引号短语）、FTC press、US Copyright Office、EU digital policy）+ DataForSEO News（EU AI Act / 州级 AI 法 / FTC 执法 / 应用商店政策 / ToS / AI 版权判例 / 责任 / 数据本地化 / reverse acqui-hire / chatbot 监管，10 组）。md5 去重。
- **每条**：已确认事实 / 开了什么关了什么 / 窗口（立即 / 过渡期 / 观察）/ 链接。
- **发信**：有 ≥1 条实质规则断裂才发，否则静默。

## 四波段优化清单（未决，2026-08-27 review）

1. **Band1↔AICapitalFlow 边界**写进两者 prompt：能让小玩家插进去的分发面 → 波段一；纯资本配置信号 → AICapitalFlow。
2. **Band3**：~~市场清单补 VS Code 扩展市场 / MCP / Raycast + 加日 diff~~ **已做（2026-08-27，Apify-free，见 §2）**；剩：GPT Store 待接入第三方稳定源；「原始榜单不研判」→ 可再加一层「新进榜的品类聚类」。
3. **Band4 Parasite**：subreddit 偏电商 → 加 r/LocalLLaMA、r/AI_Agents、r/OpenAI、r/artificial；新增真空类型「ChatGPT 回答任务型 query 时不推荐任何产品」。
4. **新词检测**：加搜索量环比突增词（DataForSEO trends/volume delta）——目前 Pseo 抓冷长尾、Parasite 抓 UGC 霸屏，都不是「三个月前不存在的新术语」。
5. **共享 `signals/` feed**（`~/.openclaw/workspace/signals/`，已建空目录）：各波段命中写 append-only JSONL，ODRW（或新周综合器）读——需放开 ODRW 的「禁读其它雷达」。
6. **邮件前缀**：ODRW（`Opportunity Distribution Radar｜` → `【综合·机会排序】`）、TechDiscontinuity（→ `【波段〇·技术断裂】`）待改。

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
