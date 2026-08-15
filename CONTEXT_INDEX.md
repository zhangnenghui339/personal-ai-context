# Context Router

AI 应先根据问题识别领域，再加载下列最小上下文；不要默认遍历整个仓库。

| 场景 | 优先读取 |
|---|---|
| 当前任务与提醒 | `tasks/current.md`、`tasks/inbox.md` |
| 某个项目 | `projects/<name>/status.md`，再按需读取同目录其他文件 |
| 亲子与教育 | `family/parenting/`、`family/education/` |
| 提示词 | `prompts/<domain>/` |
| 商业、哲学、心理思考 | `thinking/<domain>/` |
| **创业机会模型（新会话先读）** | `thinking/business/SESSION.md` |
| 创业机会、分发、套利结构化 | `thinking/business/opportunity-discovery-model.md` |
| Byrne Hobart 套利与基础设施原句 | `thinking/business/hobart-arbitrage-infrastructure.md` |
| 价值洼地类型与分发复用（人群套利） | `thinking/business/valuation-gaps-and-distribution-reuse.md` |
| 商业认知的终极升维：经济学之外的三层 | `thinking/business/beyond-economics-meta-model.md` |
| 复杂系统四要素、奢侈品与欲望模仿理论 | `thinking/business/complex-systems-and-mimetic-desire.md` |
| 分发三句：产品、租期、方向 | `thinking/business/where-distribution-is-going.md` |
| 明显的差与新产权 | `thinking/business/obvious-arb-and-new-property.md` |
| 信息差与麦克斯韦妖 | `thinking/business/information-gap-maxwell-demon.md` |
| 不对称行为：李嘉诚与早期腾讯 | `thinking/business/asymmetric-behavior-cases.md` |
| 读创业史四问与五案 | `thinking/business/four-questions-five-products.md` |
| 第二问沉默面：对手身份图 | `thinking/business/airbnb-competitor-identity.md` |
| 读书相关 | `books/reading-list.md`、`books/notes/` |
| 历史决策 | 对应项目的 `decisions.md` 或 `thinking/decision-journal/` |

## 时间与冲突规则

- `status.md` 代表项目当前状态。
- 同一主题出现冲突时，优先采用日期更新且有证据的记录。
- 未在当前任务中重新验证的旧事实，应标注“可能过时”。
- 已结束项目移入 `projects/archive/`，不参与默认检索。

## 隐私边界

`private-local/` 仅存本地敏感材料，不进入 Git，也不应被 AI 默认读取。

