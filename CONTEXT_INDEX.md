# Context Router

AI 应先根据问题识别领域，再加载下列最小上下文；不要默认遍历整个仓库。

| 场景 | 优先读取 |
|---|---|
| 当前任务与提醒 | `tasks/current.md`、`tasks/inbox.md` |
| 某个项目 | `projects/<name>/status.md`，再按需读取同目录其他文件 |
| 亲子与教育 | `family/parenting/`、`family/education/` |
| 提示词 | `prompts/<domain>/` |
| 商业、哲学、心理思考 | `thinking/<domain>/` |
| 政治、制度、国际关系（总览入口） | `thinking/politics/session.md`；目录说明：`thinking/politics/README.md`；来源库：`thinking/politics/sources.md` |
| 政治第一性原理（止掠场 × 剩余索取） | `thinking/politics/topics/politics-first-principles.md` |
| 政治大统一架构（物理 × 制度几何 × 帝王术） | `thinking/politics/topics/politics-grand-architecture.md` |
| 政治底层三元模型（利益 × 力学 × 博弈） | `thinking/politics/topics/politics-triad-mechanics-interests-games.md` |
| 政治学术语严密化与利益本质透视 | `thinking/politics/topics/politics-terminology-and-interests-essence.md` |
| 权贵财富悖论（寡头过度积财与流动性陷阱） | `thinking/politics/topics/why-elites-hoard-excess-wealth.md` |
| 政治分析十大认知误区（盲区全景） | `thinking/politics/topics/political-cognitive-fallacies.md` |
| 政治力学与制度演化深度问答（7大核心问题与实战案例） | `thinking/politics/topics/political-mechanics-in-depth-qa.md` |
| 缩圈清洗与承诺困境（中西历史比较与解法） | `thinking/politics/topics/purge-imperative-and-commitment.md` |
| 城镇化 × 势能 × 联盟算术 | `thinking/politics/topics/urbanization-coalition-momentum.md`；经济学正文仍读 `thinking/business/SESSION.md` §23 |
| 12.12 / 首尔之春：利益分配与最低获胜节点 | `thinking/politics/topics/seoul-spring-1212-coalition-game.md` |
| 信息拓扑、极值信号与收益函数相变大模型 | `thinking/politics/topics/information-payoff-phase-transition-model.md` |
| 分发—收益函数闭环共振模型（商业与政治通用动力学） | `thinking/politics/topics/distribution-payoff-resonance-engine.md` |
| 商业势能与综合会话 | `thinking/business/SESSION.md`；标杆企业：`thinking/business/benchmark-companies.md`；失败复盘：`thinking/business/failed-founders.md` |
| OpenClaw 服务器雷达（名称、逻辑、任务时间、运行状态） | `projects/openclaw-radars/status.md`，再读 `projects/openclaw-radars/overview.md`；方法论见 `thinking/business/distribution-radar-framework.md` |
| 实体套利/红利起家案例 | `thinking/business/case-studies-arbitrage-dividend.md` |
| 商业机会与套利爆发的先导指标级联模型（从技术到相变） | `thinking/business/leading-indicators-of-emerging-opportunities.md` |
| 技术与生产函数断裂（Level 1）的探测方法论：穿透公关噪音 | `thinking/business/detecting-level-1-technological-discontinuity.md` |
| 亚马逊中国卖家大爆发的历史复盘与底层规律 | `thinking/business/amazon-chinese-seller-surge-analysis.md` |
| **创业机会模型（新会话先读）** | `thinking/business/session-opportunity.md`（原该分支的 `SESSION.md`，合并时拆出以免覆盖势能会话） |
| 创业机会、分发、套利结构化 | `thinking/business/opportunity-discovery-model.md` |
| Byrne Hobart 套利与基础设施原句 | `thinking/business/hobart-arbitrage-infrastructure.md` |
| 价值洼地类型与分发复用（人群套利） | `thinking/business/valuation-gaps-and-distribution-reuse.md` |
| 价值洼地六大母体场景与战略特征 | `thinking/business/value-gap-archetypes-and-strategy.md` |
| 四大洼地自检维度与经典案例映射 | `thinking/business/four-gaps-case-mapping.md` |
| 四大洼地自检模型的通俗直觉重构 | `thinking/business/four-gaps-intuitive-framework.md` |
| 阶层差（需求减配）vs 技术差（供给革命）的本质区别 | `thinking/business/tier-vs-tech-gap-difference.md` |
| 高铁出海与一带一路：国家级四维洼地与卡口模型 | `thinking/business/hsr-belt-and-road-case-analysis.md` |
| 经典国家级大战略的经济学底层拆解 | `thinking/business/national-grand-strategies-economics.md` |
| 势能的双向流动模型：泄洪型势能（产能过剩）与虹吸型势能（生产力引进） | `thinking/business/dual-potential-energy-flow-model.md` |
| 价值的本质与势能的五大母体形态（泄洪/虹吸/黑洞/卡口/相变） | `thinking/business/value-and-potential-energy-archetypes.md` |
| 中国更多国家级大战略的微观经济学底层拆解 | `thinking/business/china-national-strategies-economic-deconstruction.md` |
| 中国对非贷款与基建出海：供应商融资与势能差闭环 | `thinking/business/china-africa-financing-model.md` |
| 势能差的本质：我们到底在赚谁的钱？（比较优势与正和博弈） | `thinking/business/nature-of-potential-energy-and-profit.md` |
| 矩阵套利机制与比较优势深度辨析 | `thinking/business/matrix-arbitrage-and-comparative-advantage.md` |
| 平台势能与个人能力：大厂光环、地租分润与佃农幻觉 | `thinking/business/platform-vs-individual-potential-energy.md` |
| 王兴「九败一胜」连续创业演化史：从极客到统帅 | `thinking/business/wang-xing-serial-entrepreneurship-evolution.md` |
| 大厂高管创业困境与势能再获取的概率学解构 | `thinking/business/executive-startup-dilemma-and-base-rates.md` |
| 流量获取的八大母体模式与分发全景图谱 | `thinking/business/traffic-acquisition-archetypes.md` |
| 城市修地铁与城际修高铁的土地财政双边补贴深度细化 | `thinking/business/metro-hsr-land-finance-deep-dive.md` |
| 分发洼地的四大发现维度：把自检模型套在流量上 | `thinking/business/distribution-gaps-four-lenses.md` |
| 分发套利与生产力迁移：高胜率机会发现方法论 | `thinking/business/distribution-arbitrage-methodology.md` |
| 从全球格局到微观产品的四层嵌套透镜与错误视角修正 | `thinking/business/macro-to-micro-nested-lenses.md` |
| 商业认知的终极升维：经济学之外的三层 | `thinking/business/beyond-economics-meta-model.md` |
| 商业落地终极五步闭环：借分发 → 找差 → 借货 → 放量 → 留底 | `thinking/business/borrow-distribution-five-steps-sop.md` |
| 分发雷达：未被定价的人流与意图探测系统 | `thinking/business/distribution-radar-framework.md` |
| 波段一（巨头战略拓荒）数据源与抓取工程全景方案 | `thinking/business/radar-band-one-data-sources-and-ops.md` |
| 波段一 AI 系统提示词、研判规则与 Python 完整脚本 | `thinking/business/radar-band-one-engineering-spec.md` |
| 流量情报工具评估：SimilarWeb、Sensor Tower 与 data.ai 的价值与平替 | `thinking/business/traffic-intelligence-tools-evaluation.md` |
| 分发雷达工程化实施方案：DataForSEO + Apify 自动化流水线 | `thinking/business/distribution-radar-engineering-sop.md` |
| 创业实战思维导图 2.0：五步闭环全景重构 (XML) | `thinking/business/startup-mindmap-5steps-complete.md` |
| 创业路径思维导图评估与 2.0 优化方案 | `thinking/business/startup-execution-framework-evaluation.md` |
| 复杂系统四要素、奢侈品与欲望模仿理论 | `thinking/business/complex-systems-and-mimetic-desire.md` |
| 分发三句：产品、租期、方向 | `thinking/business/where-distribution-is-going.md` |
| 明显的差与新产权 | `thinking/business/obvious-arb-and-new-property.md` |
| 信息差与麦克斯韦妖 | `thinking/business/information-gap-maxwell-demon.md` |
| 不对称行为：李嘉诚与早期腾讯 | `thinking/business/asymmetric-behavior-cases.md` |
| VC 幂律下注：损失封顶 × 上行不封顶 × 扩大 outlier 候选池；功能改进为何天花板锁死；Bezos 商业 / 投资核心观点汇总 | `thinking/business/vc-power-law-decision-rules.md` |
| Bezos 核心观点总览（商业 × 投资两条线，串联下面两篇 + 找机会的细化方法论） | `thinking/business/bezos-core-principles.md` |
| 顶尖创业者 / 投资人与大众不同的十个底层模式 | `thinking/business/contrarian-decision-patterns.md` |
| App 经济完整周期：装机 / 用户曲线、广告定价（CPI/CPM）与资本信号八阶段时间线（案例） | `thinking/business/app-economy-capital-signal-timeline.md` |
| Bezos 市场领导地位：窗口期、收益递增、终值 / DCF、语录合集、理论谱系、观测方法论 | `thinking/business/bezos-market-leadership-window-terminal-value.md` |
| Bezos 失败容忍、失败资产化、幂律下注、Explore/Exploit、基础设施抽取、京东 / 当当对照 | `thinking/business/bezos-failure-power-law-jd-dangdang.md` |
| 读创业史四问与五案 | `thinking/business/four-questions-five-products.md` |
| 第二问沉默面：对手身份图 | `thinking/business/airbnb-competitor-identity.md` |
| AI 创业、分发与商业化 | `thinking/business/session-ai-distribution.md` |
| B2B 轻应用商业范式与四大多态（X生态/端侧/插件） | `thinking/business/lightweight-b2b-ai-products-archetypes.md` |
| 读书相关 | `books/reading-list.md`、`books/notes/` |
| 历史决策 | 对应项目的 `decisions.md` 或 `thinking/decision-journal/` |

## 时间与冲突规则

- `status.md` 代表项目当前状态。
- 同一主题出现冲突时，优先采用日期更新且有证据的记录。
- 未在当前任务中重新验证的旧事实，应标注“可能过时”。
- 已结束项目移入 `projects/archive/`，不参与默认检索。

## 隐私边界

`private-local/` 仅存本地敏感材料，不进入 Git，也不应被 AI 默认读取。
