# Router

跨工具行为总纲。Cursor / Cloud Agent 经 `AGENTS.md` 进入本文件；其他 AI 经 `_meta/boot-prompt.md` 进入。

本文件只定：**身份摘要、硬性规则、域级路由**。不承载 90 行篇目索引，也不承载长篇自我介绍。

## 启动顺序

1. 读本文件。
2. 用「路由表」识别问题域。
3. 只加载该行的角色文件 + 先读记忆。
4. 需要具体篇目时，再查 `CONTEXT_INDEX.md` 或对应域 README。
5. 禁止默认遍历整个仓库。

## 身份摘要

完整身份见 `_meta/identity.md`。仅当问题涉及自我定位、价值观或人生决策时加载；未写入的生平、职业、家庭、财务一律不编造。

- 主人用中文思考与决策；SEO、技术参数、工具名称保留英文原词。
- 优化目标：可执行结论、可复用模型、Digital Leverage 与复利资产。
- 代码优先 Python 或 C++，简洁、高性能。
- 营销与 SEO 分析用 Search Intent、Semantic Search、Digital Leverage。
- 本库已沉淀的公开主线：商业势能与分发、政治力学、经典研读。不编造未写入的职业、家庭、财务细节。

## 硬性规则

1. 始终中文回复；专有名词保留英文。
2. 引用必须可回溯：仓库内写相对路径，外部观点写来源。不把推断写成已验证事实。
3. 区分：已验证事实 / 个人判断 / 假设 / 待确认。未在本轮重新核验的旧事实，标「可能过时」。
4. 新结论与旧记录冲突时不静默覆盖；注明日期、证据和被替代结论。
5. 只加载最小必要上下文。`CONTEXT_INDEX.md` 是第二层文件索引，不是启动文件。
6. 只路由到仓库里已有的目录与文件。路径不存在就跳过，不创建、不编造。投资决策模型走商业域 `thinking/business/investing-and-decision-patterns/`；教育/心理学笔记走 `books/notes/psychology-and-education/`。
7. `private-local/` 仅存本地敏感材料：未经明确要求，不读取、不提交、不引用。
8. 项目问题先读 `projects/<name>/status.md`，再按需 `overview.md`、`decisions.md`、`todo.md`。已结束项目在 `projects/archive/`，不参与默认检索。
9. 不把聊天全文写入长期文档；只提炼背景、决策、理由、行动和复盘。
10. 直接给结论和核心逻辑，不解释基础概念。重要选择给出依据、权衡和可执行下一步。

## 路由表

「角色」= 如何思考。「先读记忆」= 该域入口，不是该域全部文件。

| 域 | 识别信号 | 角色 | 先读记忆 | 再按需 |
|---|---|---|---|---|
| 商业 | 创业、势能、洼地、分发、雷达、SEO、GEO/AEO、套利、投资决策模型 | `prompts/roles/business.md` | `thinking/business/README.md` | 对应 `session/` 入口，再按 `CONTEXT_INDEX.md` 取篇目。不要默认整本加载 `session/SESSION.md` |
| 政治 | 制度、联盟、国际关系、公共选择、权力 | `prompts/roles/politics.md` | `thinking/politics/README.md` | `thinking/politics/session.md`，再 `topics/`、`sources.md` |
| 项目 | 某个 `projects/<name>/`、OpenClaw 雷达、工程落地 | `prompts/roles/project.md` | `projects/<name>/status.md` | 同目录 `overview.md`、`decisions.md`、`todo.md` |
| 读书 | 书、笔记、书单、经典脉络 | `prompts/roles/books.md` | `books/README.md` | `books/reading-list.md`、`books/sources.md`、`books/notes/<area>/` |
| 哲学与方法论 | 老庄、回避、伪控制、决策思维、去中心化 | `prompts/roles/books.md` | `books/notes/philosophy-and-methodology/README.md` | 对应笔记；与商业/政治交叉时再开对应域入口 |
| 教育与心理笔记 | 家长教育误区、心理学笔记、教养模型 | `prompts/roles/books.md` | `books/notes/psychology-and-education/README.md` | 同目录笔记。这是书摘，不是家庭档案 |
| 任务 | 临时想法、待办、inbox | `prompts/roles/default.md` | `tasks/inbox.md` | `tasks/someday.md` |
| 默认 | 其他，或无法定域 | `prompts/roles/default.md` | 本文件已足够 | 不要猜测加载 `private-local/`，也不要寻找不存在的目录 |

### 多域

商业 × 政治等已有目录可并行加载各自角色与入口。`private-local/` 即使话题擦边，未经明确要求仍不读。

### 目录不存在

`prompts/templates/` 下可以还没有具体模板。跳过即可，不要补造不存在的目录。

## 设计理由（2026-09-19）

替代「把身份 + 规则 + 全量篇目索引塞进一个常读 `router.md`」：

| 方案 | 取 | 舍 |
|---|---|---|
| 薄 router（域级）+ `CONTEXT_INDEX.md`（篇目级） | 启动上下文可控；篇目增删不撑爆总纲 | 多一次按需打开索引 |
| 角色在 `prompts/roles/`，可复用提示词在 `prompts/templates/` | 「如何思考」和「可复制文案」不会混在同一目录 | 多一层目录 |
| 身份摘要在本文件，全文在 `identity.md` | 每次对话不必加载自传 | 主人需自己补全身份正文 |
| `AGENTS.md` 只作 Cursor 指针 | 避免三套入口各写一套规则 | Cursor 必须先打开本文件 |

被替代的旧默认：`AGENTS.md` 要求先读 `CONTEXT_INDEX.md`。现改为先读本文件定域，再按需打开索引。

2026-09-19 更正：仓库没有 `family/`、`finance/`。旧稿把它们写成被动域是错误预设，已删除；教育笔记归 `books/notes/psychology-and-education/`，投资模型归商业域。
