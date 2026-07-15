# Context Router

AI 应先根据问题识别领域，再加载下列最小上下文；不要默认遍历整个仓库。

| 场景 | 优先读取 |
|---|---|
| 当前任务与提醒 | `tasks/current.md`、`tasks/inbox.md` |
| 某个项目 | `projects/<name>/status.md`，再按需读取同目录其他文件 |
| 亲子与教育 | `family/parenting/`、`family/education/` |
| 提示词 | `prompts/<domain>/` |
| 商业、哲学、心理思考 | `thinking/<domain>/` |
| 读书相关 | `books/reading-list.md`、`books/notes/` |
| 历史决策 | 对应项目的 `decisions.md` 或 `thinking/decision-journal/` |

## 时间与冲突规则

- `status.md` 代表项目当前状态。
- 同一主题出现冲突时，优先采用日期更新且有证据的记录。
- 未在当前任务中重新验证的旧事实，应标注“可能过时”。
- 已结束项目移入 `projects/archive/`，不参与默认检索。

## 隐私边界

`private-local/` 仅存本地敏感材料，不进入 Git，也不应被 AI 默认读取。

