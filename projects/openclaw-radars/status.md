# OpenClaw 雷达运行状态

> Last verified: 2026-08-27
> Evidence: 服务器 `openclaw cron list --all --json`、任务 README、Prompt 与执行脚本只读核验
> Timezone: `Asia/Shanghai`

## 当前阶段

删除旧雷达后的运行基线已经收敛为：

- **13 个已启用 cron 任务**（2026-08-27 新增 `TechDiscontinuityDaily`、`AICapitalFlowDaily`、`Band2MediumShiftWeekly`、`Band2RuleSniffDaily`、`Band4RegBreakDaily`；退役 `GPTBusinessOpportunityWeekly`）；
- **0 个已禁用 cron 任务**；
- **1 个保留执行文件、但没有 cron 的先导信号模块**（`capital-signals`，已被 `AICapitalFlowDaily` 取代，待退役）；
- 所有邮件由任务自身通过 SMTP 发送，OpenClaw `delivery.mode=none`，避免重复投递。
- 2026-08-27 起，所有现存雷达邮件最底部统一展示“本雷达的判断逻辑”。

## 现有定时雷达

| 雷达 / Job 名称 | 当前状态 | 任务时间（上海） | 核心逻辑 | 邮件策略 |
|---|---:|---|---|---|
| 波段 | 雷达 / Job 名称 | 当前状态 | 任务时间（上海） | 核心逻辑 | 邮件策略 |
|---|---|---:|---|---|---|
| 〇·前导 | `TechDiscontinuityDaily` | **启用** | 每天 **05:10** | arXiv 30 + HN Top 50/留 25；新增候选调 Codex，按 Breakthrough Magnitude / Credibility / Spillover 研判 | 每次发监测报告；`score>=7.5` 且可行动才列追踪 |
| 一·巨头拓荒 | `RadarBand1DailySniff` | **启用** | 每天 **06:00** | 巨头跨国拓荒 / 平台补贴 / 主权合规断裂；关键词矩阵预筛 → LLM，`score>=7.5` 命中。**2026-08-27：Chrome/Shopify/PH 采集下线（归波段三）；DataForSEO 查询加 6 组 AI 平台新面（GPT Store/Apps/MCP/Perplexity 购物/Gemini）** | 有高价值命中才发；无命中静默 |
| 一·资本异动 | `AICapitalFlowDaily` | **启用**（首次验证运行待跑） | 每天 **05:05** | AI ~14 子领域聪明钱：`collect.py`（SEC Form D + DataForSEO News + lab RSS，Apify-free）→ Claude Code headless 8 阶段定位 + 大企业行为路径与势差 | 有实质事件才发；非周一静默；周一必发全量阶段表 |
| 二·介质跃迁 | `Band2MediumShiftWeekly` | **启用**（首次验证运行待跑） | 每周三 **11:00** | 80 词 DataForSEO SERP（ai_overview）+ 引用源 churn + AI Optimization 查询 + AI 搜索规则汇总，聚焦 AI 工具 / 互联网场（组 1–6 战场 + 组 7 校准锚）；Apify-free；Claude Code headless | 每周固定发 |
| 二·规则哨 | `Band2RuleSniffDaily` | **启用**（首次验证运行待跑） | 每天 **05:20** | 只扫 AI 搜索 / 答案引擎规则变化（RSS + DataForSEO News）；Apify-free | 有实质规则变化才发，否则静默 |
| 三·宿主生态 | `RadarBand3RawSnapshotEmail` | **启用** | 每天 **06:10** | 原始快照。**2026-08-27 补 4 源（Apify-free，带昨日 diff 新增高亮）**：VS Code 扩展市场（搜 ai，官方 Gallery API）、MCP servers（PulseMCP API）、Raycast（GitHub commits API），GPT Store 保留 stub 待接入。前三源 Chrome/Shopify/PH 仍走 Apify。 | 每次运行发原始数据邮件 |
| 四·规则断裂 | `Band4RegBreakDaily` | **启用**（首次验证运行待跑） | 每天 **05:25** | AI / 科技 / 平台监管与规则变化（Federal Register · AI rules / FTC / Copyright / EU + DataForSEO News 10 组）；跨境关税留波段一；Apify-free；Claude Code headless | 有实质规则断裂才发，否则静默 |
| 四·新词真空 | `RadarBand2Parasite-dropship/SaaS/Shopify/smallbusiness` | **启用** | 每周一 **06:00–07:00** | 各扫一个 subreddit 高意图痛点帖；SERP Top 3 全 UGC = Parasite SEO 供给真空。**2026-08-27：邮件前缀改 `【波段四·新词真空·r/{sub}】`** | 黄金命中立即发；抓取失败单独告警 |
| 四·冷长尾 | `RadarBand2PseoMonthly` | **启用** | 每月 **1 日 06:30** | 6 种子词扩长尾，`Volume 30–500 / KD<=15 / CPC>0.5 / 含 vs·alternative·tool`，Top 25 核验 SERP。**前缀改 `【波段四·冷长尾】`** | 月度长尾词包 |
| 综合 | `OpportunityDistributionRadarWeekly` | **启用** | 每周二 **11:00** | 分发市场新增量 → `DIS × SOS × ACR` → `TEST / WATCH / REJECT` | 每周 JSON + HTML，SMTP 成功才写 history |

### Live cron IDs

| Job | ID |
|---|---|
| TechDiscontinuityDaily | `56d08557-7fd6-4088-92ff-ccdc0de1e1c9` |
| AICapitalFlowDaily | `f5e72292-5208-4a4c-9048-5bb27a28bed3` |
| Band2MediumShiftWeekly | `1ff145db-52fa-4080-8892-2e1e44520658` |
| Band2RuleSniffDaily | `8a84850e-7803-43b3-9716-904c963cf7db` |
| Band4RegBreakDaily | `825cee58-e4c3-49cf-bf20-f9619c76f8c2` |
| RadarBand1DailySniff | `d3defe2c-ae62-41c7-986f-d44e7cfbd707` |
| RadarBand3RawSnapshotEmail | `4bfb85b8-4fab-49f5-a05a-ee991c6fdb04` |
| RadarBand2Parasite-dropship | `1b5bc085-bb09-4233-b8bb-ea1a1380b910` |
| RadarBand2Parasite-SaaS | `30c06500-1aa9-4555-9b9f-72d41455eb28` |
| RadarBand2Parasite-Shopify | `d6aa7529-0e6a-4ca3-8386-b65888f0f035` |
| RadarBand2Parasite-smallbusiness | `c58469f6-016d-4c8b-be89-6978a926a7ae` |
| RadarBand2PseoMonthly | `c0eb37c7-fb82-4691-b0f2-ec2c81ac66dd` |
| OpportunityDistributionRadarWeekly | `6e27fab8-b859-4b6c-a755-6af15b2a5ecd` |

## 四波段归属

| 波段 | 核心目的 | 雷达 |
|---|---|---|
| 〇·前导 | 生产函数是否数量级断裂 | TechDiscontinuityDaily |
| 一·巨头拓荒与新阵地 | 巨头开新地区 / 入口 / 补贴 → 可插入的分发面 | RadarBand1DailySniff、AICapitalFlowDaily（资本行为路径 → 势差） |
| 二·介质跃迁与 AEO 搜索 | 发现多快从蓝链迁到答案引擎，谁拿引用位 | Band2MediumShiftWeekly、Band2RuleSniffDaily |
| 三·宿主生态与插件 | app / 插件市场新供给 / 新需求 | RadarBand3RawSnapshotEmail |
| 四·规则断裂与新词真空 | (a) 规则变化让新打法可行 / 失效；(b) 有需求没产品接 | Band4RegBreakDaily、RadarBand2Parasite-*、RadarBand2PseoMonthly |
| 综合 | 把上述信号汇总成机会排序 | OpportunityDistributionRadarWeekly |

未决优化（`overview.md` 详列）：Band1↔AICapitalFlow 边界写进 prompt；Band3 加日 diff + 补 GPT Store / MCP / VS Code 市场；Parasite 加 AI subreddit；`signals/` 共享 feed 接入各雷达 + 放开 ODRW 的「禁读其它雷达」。

## 保留但未定时的雷达模块

| 模块 | 当前状态 | 逻辑 | 任务时间 |
|---|---|---|---|
| `opportunity-distribution-radar-capital-signals` | 有执行文件，无 cron | Level 2 资本异动：SEC EDGAR 全市场 8-K/10-Q + NVIDIA/ASML/TSMC 定向监控 | **未设置**；已被 `AICapitalFlowDaily` 取代，待退役 |

## 已删除且不应重新纳入

2026-08-27 已从 live cron、Agent 注册表与执行目录中移除以下旧雷达；恢复文件仅保留在服务器隔离归档中，不属于当前运行基线：

1. Tool Demand Radar
2. 工具类双核探针
3. Career Keyword Radar
4. Career Pain Radar
5. 旧 SEO 竞品雷达
6. `GPTBusinessOpportunityWeekly`（2026-08-27 退役：品类被 LLM 内联回答吞没，且与 ODRW 综合器角色重复；`D×A×G×P×S×L÷C` 打分法转为 ODRW 可选 lens。task 目录移入 `deleted-radars/2026-08-27-gpt-business-opportunity-weekly/`）

## 已确认的配置漂移

- **`AICapitalFlowDaily` / `Band2MediumShiftWeekly` / `Band2RuleSniffDaily` / `Band4RegBreakDaily`（均由 Claude Code headless 执行）首次完整验证运行都未跑通**：`claude -p --dangerously-skip-permissions` 在 root 下被拒，四个 `run-claude.sh` 均已改用 `--permission-mode acceptEdits --allowedTools "Bash Read Write Edit Glob Grep"`。各自的 `collect.py` 已单独实测通过（AICapitalFlow 140 条 / Band2 sniff 154 条 / Band4 175 条）。需 `openclaw cron run <id> --wait` 各验证一次。回退方案：`run-claude.sh` 里 `claude` → `codex`（与其余雷达一致）。
- **Band1 已改**（2026-08-27）：`radar_band1.py` 停止调用 `collect_app_market_candidates()`（Chrome/Shopify/PH 归波段三，消除 Band1↔Band3 双抓）；`DATAFORSEO_QUERIES` 加 6 组 AI 平台新面查询；邮件主题前缀 `[分发雷达·波段一]` → `【波段一·巨头拓荒】`。函数体保留未删，syntax 已过，需下次 06:00 运行验证。
- **邮件前缀统一**（2026-08-27，f-string 改，syntax 已过，未跑验证）：Band3 → `【波段三·宿主生态】`；Parasite `[分发雷达·波段二]` → `【波段四·新词真空·r/{sub}】`（旧「波段二」编号与新的介质跃迁波段冲突，必须改）；Pseo → `【波段四·冷长尾】`。ODRW / TechDiscontinuity 前缀待改。
- **Band3 补源已改**（2026-08-27）：`radar_band3_raw_snapshot.py` 加 `fetch_vscode_raw` / `fetch_mcp_raw` / `fetch_raycast_raw`（分别实测 30/40/30 条）+ `fetch_gptstore_raw` stub + 通用 `_diff_section`（baseline 存 `data/`）。syntax 已过，fetcher 已实测；完整 run()（含发信）需下次 06:10 验证。三个新源各自 try/except，失败只在邮件里显示「❌ 采集失败」，不影响既有三源。
- `signals/` 已建空目录（`~/.openclaw/workspace/signals/`），接入各雷达 + 放开 ODRW 禁读规则为待办。
- 雷达 LLM 执行器保持不变：codex(GPT-5.6) 用于 Band1 / TechDiscontinuity / ODRW；claude headless 用于 AICapitalFlow / Band2 / Band4；Band3 / Parasite / Pseo 无 LLM。deepseek-v4-pro 仅服务 agentTurn 型非雷达任务，2026-08-27 明确不引入雷达。
- `OpportunityDistributionRadarWeekly` 的服务器旧 README 写的是周二 05:50，但 **live cron 当前为周二 11:00**；本文件以 live cron 为准。
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
