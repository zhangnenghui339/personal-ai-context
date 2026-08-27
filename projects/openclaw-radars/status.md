# OpenClaw 雷达运行状态

> Last verified: 2026-08-27
> Evidence: 服务器 `openclaw cron list --all --json`、任务 README、Prompt 与执行脚本只读核验
> Timezone: `Asia/Shanghai`

## 当前阶段

删除旧雷达后的运行基线已经收敛为：

- **10 个已启用 cron 任务**（2026-08-27 新增 `TechDiscontinuityDaily`、`AICapitalFlowDaily`）；
- **1 个已禁用 cron 任务**；
- **1 个保留执行文件、但没有 cron 的先导信号模块**（`capital-signals`，已被 `AICapitalFlowDaily` 取代，待退役）；
- 所有邮件由任务自身通过 SMTP 发送，OpenClaw `delivery.mode=none`，避免重复投递。
- 2026-08-27 起，所有现存雷达邮件最底部统一展示“本雷达的判断逻辑”。

## 现有定时雷达

| 雷达 / Job 名称 | 当前状态 | 任务时间（上海） | 核心逻辑 | 邮件策略 |
|---|---:|---|---|---|
| `AICapitalFlowDaily` | **启用**（首次验证运行待跑） | 每天 **05:05** | AI ~14 子领域的聪明钱流向：`collect.py`（SEC EDGAR Form D + DataForSEO Google News + lab RSS，Apify-free）→ Claude Code headless 归类 + 8 阶段定位 + 反推大企业行为路径与势差；实质事件阈值（≥$100M 轮 / M&A / 巨头 AI 组织 / Sherlocking / 洗牌簇 / 主权资本 / 跨阶段） | 有实质事件才发；无事件的非周一静默；周一必发全量阶段表 |
| `RadarBand1DailySniff` | **启用** | 每天 **06:00** | 监控巨头跨国拓荒、平台补贴、主权政策/合规断裂；关键词矩阵预筛后交给 LLM 研判，`score >= 7.5` 且可行动才命中 | 有高价值命中才发送；无命中静默 |
| `RadarBand3RawSnapshotEmail` | **启用** | 每天 **06:10** | 抓取 Chrome Web Store Top 30、Shopify App Store 分类页、Product Hunt Top 10，输出应用/插件市场原始快照 | 每次运行发送原始数据邮件 |
| `TechDiscontinuityDaily` | **启用** | 每天 **05:10** | 采集 arXiv 最新 30 篇与 Hacker News Top 50/保留 25；对新增候选调用 Codex，按 Breakthrough Magnitude、Credibility、Spillover Potential 研判 | 每次运行发送监测报告；`score >= 7.5` 且可行动才列为追踪候选 |
| `RadarBand2Parasite-dropship` | **启用** | 每周一 **06:00** | 扫描 `r/dropship` 高意图痛点帖；若 Google SERP Top 3 全为 Reddit/Quora，则判为 Parasite SEO 供给真空 | 黄金命中立即发送；抓取彻底失败单独告警 |
| `RadarBand2Parasite-SaaS` | **启用** | 每周一 **06:20** | 与上项相同，独立扫描 `r/SaaS` | 同上 |
| `RadarBand2Parasite-Shopify` | **启用** | 每周一 **06:40** | 与上项相同，独立扫描 `r/Shopify` | 同上 |
| `RadarBand2Parasite-smallbusiness` | **启用** | 每周一 **07:00** | 与上项相同，独立扫描 `r/smallbusiness` | 同上 |
| `RadarBand2PseoMonthly` | **启用** | 每月 **1 日 06:30** | 从 6 个种子词扩展长尾；按 `Volume 30–500 / KD <= 15 / CPC > 0.5 / 含 vs、alternative 或 tool` 过滤，Top 25 再核验 SERP | 生成并发送月度长尾词包 |
| `OpportunityDistributionRadarWeekly` | **启用** | 每周二 **11:00** | 独立扫描分发市场新增量，计算 `DIS × SOS × ACR`，输出 `TEST / WATCH / REJECT` | 每周生成 JSON + HTML，SMTP 成功后才写 history |
| `GPTBusinessOpportunityWeekly` | **禁用** | 原计划每周二 **05:50**；当前无自动触发 | 独立扫描泛工具机会，按 `D × A × G × P × S × L ÷ C` 排序，输出 `BUILD_TEST / OBSERVE / REJECT` | 仅手动运行时发信；2026-08-27 手动运行成功 |

### Live cron IDs

| Job | ID |
|---|---|
| AICapitalFlowDaily | `f5e72292-5208-4a4c-9048-5bb27a28bed3` |
| RadarBand1DailySniff | `d3defe2c-ae62-41c7-986f-d44e7cfbd707` |
| RadarBand3RawSnapshotEmail | `4bfb85b8-4fab-49f5-a05a-ee991c6fdb04` |
| TechDiscontinuityDaily | `56d08557-7fd6-4088-92ff-ccdc0de1e1c9` |
| RadarBand2Parasite-dropship | `1b5bc085-bb09-4233-b8bb-ea1a1380b910` |
| RadarBand2Parasite-SaaS | `30c06500-1aa9-4555-9b9f-72d41455eb28` |
| RadarBand2Parasite-Shopify | `d6aa7529-0e6a-4ca3-8386-b65888f0f035` |
| RadarBand2Parasite-smallbusiness | `c58469f6-016d-4c8b-be89-6978a926a7ae` |
| RadarBand2PseoMonthly | `c0eb37c7-fb82-4691-b0f2-ec2c81ac66dd` |
| OpportunityDistributionRadarWeekly | `6e27fab8-b859-4b6c-a755-6af15b2a5ecd` |
| GPTBusinessOpportunityWeekly | `760338a0-dec5-47fc-ab04-b5270305c97f` |

## 保留但未定时的雷达模块

| 模块 | 当前状态 | 逻辑 | 任务时间 |
|---|---|---|---|
| `opportunity-distribution-radar-capital-signals` | 有执行文件，无 cron | Level 2 资本异动：SEC EDGAR 全市场 8-K/10-Q + NVIDIA/ASML/TSMC 定向监控；判断 CapEx 激增、卖铲人订单/Backlog、资本决心、方向清晰度和领先时间；`score >= 7.5` 才预警 | **未设置** |

## 已删除且不应重新纳入

2026-08-27 已从 live cron、Agent 注册表与执行目录中移除以下旧雷达；恢复文件仅保留在服务器隔离归档中，不属于当前运行基线：

1. Tool Demand Radar
2. 工具类双核探针
3. Career Keyword Radar
4. Career Pain Radar
5. 旧 SEO 竞品雷达

## 已确认的配置漂移

- `AICapitalFlowDaily`（2026-08-27 新建）：首次 `openclaw cron run` 调试失败——`claude -p --dangerously-skip-permissions` 在 root 下被拒。`run-claude.sh` 已改为 `--permission-mode acceptEdits --allowedTools "Bash Read Write Edit Glob Grep"`。`collect.py` 已单独实测通过（返回 140 条真实融资 / M&A 新闻）。**首次完整验证运行尚未跑通**；若改后的 claude headless 仍在 root 下报错，回退方案是把 `run-claude.sh` 里的 `claude` 换成 `codex`（与其余雷达一致）。
- `AICapitalFlowDaily` 取代了 dormant 的 `opportunity-distribution-radar-capital-signals`（全市场、无 cron）；后者待从执行目录退役。
- `OpportunityDistributionRadarWeekly` 的服务器旧 README 写的是周二 05:50，但 **live cron 当前为周二 11:00**；本文件以 live cron 为准。
- `GPTBusinessOpportunityWeekly` 虽保留 `05:50` cron 表达式，但 `enabled=false`，不能视为自动运行。
- GitHub 只记录结构、规则和运行状态；SMTP 密码、API Token、私钥、收件地址等敏感配置不进入仓库。

## 邮件 Footer 规范

每封雷达邮件最底部必须包含以下五项，并与实际执行代码一致：

1. 监控目标；
2. 数据源；
3. 筛选或评分流程；
4. 触发发信条件；
5. 任务时间与决策边界。

该要求覆盖正常报告、命中预警和抓取失败告警；周报由外层 runner 在 SMTP 发送前确定性注入，避免依赖模型是否按格式生成。

## 维护规则

每次新增、删除或调整服务器雷达后，应同时更新：

1. 本文件的 live 状态与时间；
2. `overview.md` 的逻辑边界；
3. `Last verified` 日期；
4. 以 live cron 为事实源，不从旧 README 反推当前配置。
