# Prompts

两种东西，不要混放。

| 目录 | 是什么 | 何时加载 |
|---|---|---|
| `roles/` | AI 在该域如何思考 | 由 `_meta/router.md` 路由表指定，定域后必读 |
| `templates/` | 可复制的提示词正文 | 用户明确要提示词，或角色文件指向某一模板时 |

`CONTEXT_INDEX.md` 里的「提示词」指 `templates/`，不是角色。
