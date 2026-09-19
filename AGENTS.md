# AI Collaboration Rules

Cursor / Cloud Agent 的自动入口。跨工具总纲在 `_meta/router.md`，不要在本文件再写一套规则。

1. 先读 `_meta/router.md`，遵守其中「硬性规则」和「路由表」。
2. 定域后只加载对应 `prompts/roles/` 与「先读记忆」。具体篇目再查 `CONTEXT_INDEX.md`。
3. 不要默认遍历整个仓库。未经明确要求，不读取或提交 `private-local/`。
