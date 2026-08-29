# 分发雷达实施草稿：四波段整合方案（DataForSEO + Apify）

- Date: 2026-08-22
- Status: DRAFT —— 未落地实施，等待确认后再动手写代码
- Scope: 整合 `thinking/business/distribution-radar/distribution-radar-framework.md`（四波段理论）与 `thinking/business/distribution-radar/distribution-radar-engineering-sop.md`（工程方案），结合服务器实测结果，给出可直接实施的分波段设计。取代原 `opportunity-distribution-radar` 的 DIS×SOS×ACR 评分体系，本版本暂不处理留底/资产沉淀维度。

---

## 本轮的关键决策（与前序文档的差异）

1. **停用 seo-radar，全部并入 distribution-radar** —— 不再拆分"战略/战术"两个雷达，四个波段统一在一个系统里跑。
2. **弃用 DIS×SOS×ACR，改用 Arbitrage Score 体系** —— 原三层评分依赖 LLM 主观 1-5 打分，无真实数据支撑；新方案改为纯 API 数据驱动的量化公式，四个波段各自适配。
3. **本版本不处理留底/复利（Asset Capture）** —— 五步法里的"留底"维度本次不纳入评分，雷达只负责识别套利窗口，不评估长期资产沉淀价值。这是有意的范围收窄，不是遗漏。
4. **`thinking/business/distribution-radar/distribution-radar-engineering-sop.md` 里点名的 Apify Actor 有两个不存在**，已用实测替代方案覆盖（见下方"Actor 验证结果"）。

---

## Actor 验证结果（2026-08-22 实测，只读查询未产生费用）

| 工程 SOP 原始点名 | 实际情况 | 替代方案 |
|---|---|---|
| `apify/chrome-web-store-scraper` | ❌ 不存在 | `vujeen/chrome-web-store-scraper`（99次运行）或 `tugelbay/chrome-web-store-intelligence`（PAY_PER_EVENT计价，405次运行，社区口碑更好）——**具体单价待进一步核实事件定价表** |
| `apify/shopify-app-store-scraper` | ❌ 不存在 | `scoutlayer/shopify-appstore-scraper`（23,543次运行，社区最活跃，PAY_PER_EVENT计价）——**具体单价待核实** |
| `trudax/reddit-scraper` | ✅ 存在，但计价是 **$45/月 FLAT_PRICE_PER_MONTH**（固定月费，非按量计费） | 改用 `trudax/reddit-scraper-lite`（同作者，PAY_PER_EVENT，$0.004/条结果 + $0.02/GB 启动费，已实测可用，见下方定价详情） |

`reddit-scraper-lite` 实测定价（DataForSEO 账户等级对应的阶梯价）：
```
FREE 等级：$0.004/条结果
+ $0.02/GB 内存启动费（一次性，每次 run 收一次）
```

按目前 $10 预算（原$5 + 关注社媒活动奖励$5），Reddit 抓取部分每周成本约 $0.3-0.5，完全在预算内；Chrome Web Store / Shopify App Store 两个 actor 的精确单价还需要再查一次事件定价表，属于**待办事项**，写代码前应先确认，避免预算失控。

---

## 架构总览

```
                     【分发雷达整合架构】
                                  │
     ┌────────────────────────────┴────────────────────────────┐
     │                                                         │
【数据采集端：Apify Actors】                                【数据量化端：DataForSEO API】
↳ Reddit 社区痛点帖抓取（reddit-scraper-lite）              ↳ Keywords Data API（搜索量/KD/CPC）
↳ Chrome Web Store / Shopify App Store 新榜抓取             ↳ SERP API（前排对手/借壳权重判断）
↳ 官方 Newsroom/Blog 抓取（website-content-crawler）        ↳ Google Trends API（增长率量化）
     │                                                         │
     └────────────────────────────┬────────────────────────────┘
                                  │
                       GitHub API（免费，复用已有 gh token）
                       HN Algolia API（免费，无需注册）
                                  │
                                  ▼
                【四波段独立打分引擎（Python，纯数据驱动）】
                                  │
                                  ▼
                【输出：每周主报（波段1+2+3）+ 每日轻讯（波段4）】
```

---

## 波段 1：巨头拓荒与新阵地（Platform Expansions）

- **数据源**：Apify `apify/website-content-crawler`（定向抓官方 Newsroom/Blog）+ DataForSEO Trends API（交叉验证搜索量增长）
- **抓取逻辑**：
  1. 维护 Tier-1 官方信源清单（TikTok Newsroom、Shopify Changelog、Amazon News 等，**具体 URL 清单待补充**）
  2. 关键词模式匹配："now available in" / "launches in" / "opens to" / "正式上线" / "新开放"
  3. 命中候选事件后，把提到的地区/功能词回传 DataForSEO Trends 查真实搜索量增长率
- **打分公式**：
  ```
  Platform Expansion Score (PES) = 官方信号强度 × 搜索量7天增长率 × 早期窗口系数
  官方信号强度：官方一手源=1.0 / 媒体转载=0.5
  早期窗口系数：公告<14天=1.5 | 14-30天=1.0 | >30天=0.5
  ```
- **频次**：每周 1 次

---

## 波段 2：介质跃迁与 pSEO / 社区借壳（Medium Shift & GEO）

### 2a 社区借壳截流（周级）
- **数据源**：Apify `trudax/reddit-scraper-lite` + DataForSEO SERP API
- **抓取逻辑**：
  1. 监控核心 subreddit（`r/dropship`、`r/SaaS`、`r/Shopify`、`r/smallbusiness` 等）
  2. 搜索句式："How to" / "Best tool for" / "Alternative to" / "Is there an app that"
  3. 命中痛点词后查 DataForSEO SERP，**若前3名是 Reddit/Quora 自身帖子（非专业工具站）→ 高优先级预警**

### 2b pSEO 长尾词库规模量化（双周/月级）
- **数据源**：DataForSEO Keywords Data（Keyword Suggestions + Google Ads Search Volume）
- **种子词**：convert / download / format / vs / generator / calculator
- **过滤条件**：`search_volume 30-500 AND KD≤15 AND cpc>0.5 AND keyword含'vs'/'alternative'/'tool'`

**打分公式（两条子任务共用）**：
```
Arbitrage Score = (Search Volume × Intent Weight) / (KD × SERP Competitor Strength) × Growth Rate
Intent Weight：buy/pricing/software/alternative = 2.0 ｜ 纯名词 = 0.5
SERP Competitor Strength：前3名全大厂(G2/Forbes) = 3.0 ｜ 前3名是Reddit/论坛 = 0.5
```

- **频次**：2a 每周1次；2b 双周/月1次

---

## 波段 3：宿主生态与插件卡位（Host Ecosystems）

- **数据源**：Apify `vujeen/chrome-web-store-scraper`（或 `tugelbay/chrome-web-store-intelligence`）+ `scoutlayer/shopify-appstore-scraper`
- **抓取逻辑**：
  1. 抓"近30天新上架"/"Trending飙升榜"
  2. 过滤：安装/评测增长率 >50%，评分 <3.8星
  3. 提取核心关键词回传 DataForSEO 验证真实搜索需求
- **打分公式**：
  ```
  Supply Vacuum Score (SVS) = 安装量30天增长率 ÷ 综合评分
  ```
- **频次**：每周 1 次

---

## 波段 4：突发新词与规则断裂（Regulatory & Trend Vacuum）

- **数据源**：DataForSEO Google Trends API + GitHub API（免费，复用已有 gh token，5000次/小时）+ HN Algolia API（免费，无需注册）
- **抓取逻辑**：
  1. 监测搜索热度从 0 突发飙升至 80+ 的新词
  2. 监测 GitHub 连续多天 Star 暴涨的新协议/工具
  3. 监测 HN 热帖中的新技术词出现频率
- **打分公式**：
  ```
  Trend Hijack Score = 7天搜索增长率 × (1 / (现有专业页面数+1)) × Intent Weight
  ```
- **频次**：每日 1 次（轻量扫描，约2分钟）

---

## 调度计划

| 任务 | 频次 | 系统 cron 现状 |
|---|---|---|
| 波段1 | 每周1次 | 需并入现有周任务 |
| 波段2a | 每周1次 | 需并入现有周任务 |
| 波段2b | 双周/月1次 | 新增独立调度 |
| 波段3 | 每周1次 | 需并入现有周任务 |
| 波段4 | **每日1次** | **现有系统没有，需新增每日 cron** |

---

## 模拟邮件输出

### 每周主报（波段1+2+3）

```
🛰️ 分发雷达周报 (2026-W34)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【波段1】巨头拓荒新阵地
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. TikTok Shop 正式开放 波兰站
   官方来源：TikTok Newsroom (2026-08-18)
   "TikTok Shop Poland" 搜索量7天增长：+210%
   PES = 1.0 × 2.1 × 1.5 = 3.15
   窗口：公告发布第4天，早期窗口系数拉满
   → 动作：波兰语站点/插件的窗口期，建议本周内评估

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【波段2a】社区借壳截流
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 关键词："batch webp to png with transparent background"
   月搜 320 | KD 6 | CPC $1.2
   Google 排名第2为 Reddit 帖子（r/webdev，47赞，吐槽现有工具限5张）
   Arbitrage Score = (320×2.0)/(6×0.5)×1.3 = 277.3
   → 动作：单页批量工具 + Reddit贴内软植入

【波段2b】pSEO 长尾词包（本期双周扫描）
   本期新增合格长尾词：38个（KD≤15, 月搜30-500, CPC>0.5）
   Top 5（按Arbitrage Score排序）见附件JSON

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【波段3】宿主生态供给真空
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Shopify App: "Auto Invoice PDF Generator"
   近30天安装增长 +85% | 评分 3.2星
   SVS = 85/3.2 = 26.6
   核心槽点：不支持多币种汇率自动换算
   → 动作：复制已验证功能 + 补多币种，上架截流

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
数据来源：DataForSEO + Apify
```

### 每日轻讯（仅波段4，达到阈值才发）

```
⚡ 分发雷达·突发新词预警 (2026-08-22)

新词："{某新开源模型名} prompt optimizer"
7天搜索暴涨：+650%
Google 当前专业页面数：0
Trend Hijack Score = 6.5 × (1/1) × 2.0 = 13.0

→ 动作：24小时内评估是否值得上线单页工具，吃前2个月流量真空
（低于阈值的当日候选：3个，未达发送标准，仅存档）
```

---

## 待办事项（写代码前需确认）

1. `vujeen/chrome-web-store-scraper` 与 `scoutlayer/shopify-appstore-scraper` 的具体事件定价表未核实，需要在实施前再查一次，纳入总预算测算
2. 波段1 的官方信源清单（Tier-1 Newsroom/Blog URL 列表）需要补充具体条目
3. 波段4 的每日 cron 在现有系统里不存在，需要新增
4. GEO（大模型引用监测）目前两套 API 都不覆盖，仍是已知缺口，本版本不处理
5. $10 Apify 预算的硬顶控制参数（`maxTotalChargeUsd`）需要写进脚本，避免超支
