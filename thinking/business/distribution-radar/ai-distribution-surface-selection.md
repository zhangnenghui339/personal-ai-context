# AI 产品分发面选择备忘（2026-08）

- Date: 2026-08-31
- Status: working memo / decision aid
- Scope: 当下（AI 应用层）该把分发押在哪个面。两种分发形态 + 货架类渠道打分 + 选择程序 + 留底铁律。
- 锚点：`thinking/business/opportunity-discovery/ai-shift-opportunity-checklist.md`、`thinking/business/distribution-radar/where-distribution-is-going.md`、`thinking/business/distribution-radar/traffic-acquisition-archetypes.md`、`thinking/business/opportunity-discovery/borrow-distribution-five-steps-sop.md`、`thinking/business/opportunity-discovery/geo-aeo-answer-engine-pipeline.md`、`thinking/business/cases/ai-shift-direction-library.md`

---

## 一、分发的两种形态

按「你和用户的相对位置」分两类，都属于 `where-distribution-is-going.md` 说的「分发正在去的那一层」，但打法相反：

| 形态 | 你在哪 | 机制 | 代表面 |
|---|---|---|---|
| **注意力入口型（你在场）** | 常驻用户工作流，用户做事时你一直在 | 你成为用户「用 AI 的第一入口」，顺带拿到上下文（AI 的燃料）。抢**常驻位** | 浏览器插件、MCP / Skill、IDE 扩展、Raycast |
| **被引用型（你被召唤）** | 不在场，被答案引擎 / agent 在回答时拉进来 | 你是「答案背后的信源 / 可被调用的能力」，靠结构化 + 权威度被优先引用。抢**召回权** | GEO/AEO 答案引擎、MCP Server 被 agent 调用 |

---

## 二、浏览器插件 = 用户注意力入口

**它抓住的现实**：

- 用户正在浏览网页 / 搜索信息 / 做任务
- 用户愿意装插件（低门槛、可逆）
- 插件能读网页上下文 —— AI 的燃料

**本质**：你在用户的工作流里，成为他们**使用 AI 的第一入口**。这就是分发。

- 八大母体位置：寄生截流（母体 2）+ 工具诱饵（母体 5）的合体。宿主 = Chrome / Edge Web Store。
- 窗口：不是「刚开闸」，是「AI 让页面内副驾驶成为新品类」，Level 3→4 交界。
- 留底强：账号体系、收款、EDM 都能自建；用户主动卸载前，触点归你。
- 风险：Manifest V3 能力限制、Google 审核、浏览器自带 AI（Gemini in Chrome）。

---

## 三、GEO / AEO = 答案引擎层的「被引用位」

- 这是**答案引擎这一层**的分发，不是单一 Google：Google AI Overview / Gemini、ChatGPT Search、Perplexity、Copilot、各垂直助手。
- 分发资产 = 成为被引用的信源。用户问 → 引擎合成答案 → 你的内容 / 数据 / 工具被列为来源和外链。
- 八大母体位置：程序化生成 / 权威信源（母体 4）的 AI 变体，够独立，单列一行。势能形态 = **卡口型**（坐在「内容 → 答案引擎 → 客户决策」的必经位）。
- **选它的前提**：你的东西是**内容 / 数据 / 权威信源型**，不是功能工具型。是工具型就走入口型渠道。
- 窗口：1–2 年，AI 搜索的引用规则 / 信源权重 / 反垃圾都在成型。
- 主要风险：CTR 归零（答案给完用户不点）；引擎改引用规则或自己做数据合作绕开外链。
- 详见 `geo-aeo-answer-engine-pipeline.md`。

---

## 四、货架类渠道打分

| 渠道 | 窗口红利 | 付费意愿 | 抗平台抽干 | 可留底 | AI 契合 | 定位 |
|---|:--:|:--:|:--:|:--:|:--:|---|
| MCP Apps / Claude Skill / ChatGPT Apps / Cursor·VSCode | ★★★★★ | ★★★☆ | ★★★（本地版） | ★★★ | ★★★★★ | 主攻（= 机会点 05） |
| Chrome 扩展 | ★★★☆ | ★★★★ | ★★★ | ★★★★ | ★★★★ | A / beachhead |
| Zapier / Make | ★★★ | ★★★★ | ★★☆ | ★★ | ★★★★ | B+，结构性被 MCP 上游替代 |
| WordPress 插件 | ★★☆（合规 / SEO 场景 ★★★★） | ★★☆ | ★★★★★ | ★★★★★ | ★★★ | B，长半衰期，不追窗口 |
| Shopify App Store | ★★★ | ★★★★★ | ★★ | ★★ | ★★★☆ | 缝隙可做，你是租客 |
| Webflow Apps | ★★★★（新） | ★★☆ | ★★☆ | ★★ | ★★★ | C，占坑 / 练手，TAM 太小 |
| Intercom / HubSpot App Store | ★★ | ★★★★★ | ★☆ | ★☆ | ★★（Fin / Breeze 自营碾压） | D，只做官方明确不碰的合规记账层 |

**不在货架品类、但同属「现在的窗口」**：

| 渠道 | 窗口红利 | 付费意愿 | 抗平台抽干 | 可留底 | AI 契合 | 定位 |
|---|:--:|:--:|:--:|:--:|:--:|---|
| GEO/AEO 被引用位 | ★★★★ | ★★★ | ★★★ | ★★★（结构化库 + 归因数据） | ★★★★ | 内容 / 信源型主线 |

---

## 五、选择程序

1. 先分类你的东西：**功能工具** → 入口型渠道；**内容 / 数据 / 信源** → GEO/AEO。
2. 入口型选 beachhead：用户做那件事时人在**对话里** → MCP / Skill；人在**某个网页 / SaaS 上** → Chrome 扩展。
3. 一个内核 80% 共享，先跑通一个 beachhead 的 3 笔真实付费，再 20% 胶水横向复制（+ Raycast / VS Code / cursor.directory）。
4. 不当主战场：Shopify / Intercom / HubSpot（租客位、被自营 AI 碾压），除非做官方明确不碰的合规缝隙。

---

## 六、留底铁律（所有渠道通用）

官方 Registry、ChatGPT Directory、平台 App Store 都是房东面 —— 用来被发现，不是护城河。带得走的只有：开源本地版引流来的**自持用户 / 邮箱**、**专有数据与归因历史**、**工作流锁定**。套利会关，这些留下（Hobart：arbs close, infrastructure remains）。

---

## 附：分发地址清单（2026-08）

- **MCP**：registry.modelcontextprotocol.io（官方，先发）→ mcp.so / glama.ai / pulsemcp.com / smithery.ai（抓取或 PR）
- **VS Code / Copilot**：编辑器内 `@mcp` gallery、GitHub MCP Registry、marketplace.visualstudio.com
- **Cursor**：cursor.com/marketplace（官方 curated）、cursor.directory（社区）
- **Claude**：github.com/anthropics/claude-plugins-official（官方 curated）、skills.sh（有安装榜）
- **ChatGPT**：ChatGPT App Directory，提交入口 developers.openai.com/apps-sdk（需 MCP server + 资产；变现受限）
- **邻近**：store.raycast.com（安装数公开、Mac 高意图人群）
