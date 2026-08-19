# Context Router

AI 应先根据问题识别领域，再加载下列最小上下文；不要默认遍历整个仓库。

| 场景 | 优先读取 |
|---|---|
| 当前任务与提醒 | `tasks/current.md`、`tasks/inbox.md` |
| 某个项目 | `projects/<name>/status.md`，再按需读取同目录其他文件 |
| 亲子与教育 | `family/parenting/`、`family/education/` |
| 提示词 | `prompts/<domain>/` |
| 商业、哲学、心理思考 | `thinking/<domain>/` |
| 政治、制度、国际关系 | `thinking/politics/session.md`；目录说明：`thinking/politics/README.md`；来源库：`thinking/politics/sources.md` |
| 政治联盟算术（团结/拉拢/放弃/孤立/打击/利用） | `thinking/politics/topics/coalition-arithmetic.md` |
| 城镇化 × 势能 × 联盟算术 | `thinking/politics/topics/urbanization-coalition-momentum.md`；经济学正文仍读 `thinking/business/SESSION.md` §23 |
| 商业势能与综合会话 | `thinking/business/SESSION.md`；标杆企业：`thinking/business/benchmark-companies.md`；失败复盘：`thinking/business/failed-founders.md` |
| 实体套利/红利起家案例 | `thinking/business/case-studies-arbitrage-dividend.md` |
| **创业机会模型（新会话先读）** | `thinking/business/session-opportunity.md`（原该分支的 `SESSION.md`，合并时拆出以免覆盖势能会话） |
| 创业机会、分发、套利结构化 | `thinking/business/opportunity-discovery-model.md` |
| Byrne Hobart 套利与基础设施原句 | `thinking/business/hobart-arbitrage-infrastructure.md` |
| 分发三句：产品、租期、方向 | `thinking/business/where-distribution-is-going.md` |
| 明显的差与新产权 | `thinking/business/obvious-arb-and-new-property.md` |
| 信息差与麦克斯韦妖 | `thinking/business/information-gap-maxwell-demon.md` |
| 不对称行为：李嘉诚与早期腾讯 | `thinking/business/asymmetric-behavior-cases.md` |
| 读创业史四问与五案 | `thinking/business/four-questions-five-products.md` |
| 第二问沉默面：对手身份图 | `thinking/business/airbnb-competitor-identity.md` |
| AI 创业、分发与商业化 | `thinking/business/session-ai-distribution.md` |
| 读书相关 | `books/reading-list.md`、`books/notes/` |
| 历史决策 | 对应项目的 `decisions.md` 或 `thinking/decision-journal/` |

## 时间与冲突规则

- `status.md` 代表项目当前状态。
- 同一主题出现冲突时，优先采用日期更新且有证据的记录。
- 未在当前任务中重新验证的旧事实，应标注“可能过时”。
- 已结束项目移入 `projects/archive/`，不参与默认检索。

## 隐私边界

`private-local/` 仅存本地敏感材料，不进入 Git，也不应被 AI 默认读取。
