# 侧边栏副驾驶：寄生宿主入口的 B2B 轻应用五案（待比较）

- Date: 2026-08-31
- Status: candidate / 待比较（非结论，收集来源为对话，未逐一核实产品现状）
- Scope: 「极轻宿主入口 + 离钱最近的单一 Task + 侧边栏 Accept/Reject」这一模式下的 5 个存量方向样本，用于后续横向比较与选型。
- 锚点：`thinking/business/cases/b2b-ai-products-library.md`、`thinking/business/distribution-radar/ai-distribution-surface-selection.md`、`thinking/business/cases/ai-shift-direction-library.md`

---

## 一句话

不做「大应用」，去看某个高薪岗位（外贸业务员、跨境广告优化师、合规官……）一天里打开时间最长的那个软件，在它上面加一层「侧边栏副驾驶」：寄生宿主零后台、只解决离钱最近的单一 Task、由人做最后一碰（逐条 Accept/Reject），顺带沉淀高价值数据闭环。

---

## 1. 法律与合同合规审查（对标 Spellbook）

- **寄生入口（Zero-Infra）**：MS Word 插件。律师和法务本来就在 Word 里拟定与修订合同，不用登录任何独立 SaaS 后台。
- **离钱距离（High WTP）**：直击 B2B 交易中最贵的「合同风险与对赌条款审查」。企业按年付费，ACV 极高。
- **最后一碰（Human-in-the-Loop）**：AI 在 Word 侧边栏对每条风险条款给出修改建议（Redline），专业律师逐条点「接受 / 拒绝」。法务承担法律责任，AI 提供审核杠杆。

## 2. B2B 销售获客与 Cold Email 外展（对标 Clay / Magical AI）

- **寄生入口（Zero-Infra）**：Google Sheets 插件 / Chrome 侧边栏。销售在 LinkedIn 或企业官网浏览线索时直接唤起。
- **离钱距离（High WTP）**：自动化「线索补全（Enrichment）→ 竞品技术栈识别 → 个性化开发信拟定」，直接绑定企业的新增订单与 Pipeline。
- **最后一碰（Human-in-the-Loop）**：AI 批量生成 100 封个性化 Pitch 邮件存为草稿，销售在侧边栏做秒级快审（10 分钟审完 100 封），满意后一键触发发送，杜绝把客户写砸的黑盒风险。

## 3. 数据处理与杂乱表格自动化（对标 GPT for Work / Coefficient）

- **寄生入口（Zero-Infra）**：Google Sheets / Excel 官方 Add-on。纯粹作为自定义函数嵌入表格，如 `=GPT("提取以下客服评语的主题", A2)`。
- **离钱距离（High WTP）**：解决运营、财务、电商团队每周几十小时的非结构化数据清洗、分类、多语言翻译。
- **最后一碰（Human-in-the-Loop）**：数据直接填入单元格，业务人员看到结果后手动抽查、修正，最后「复制为纯文本值」锁定结果，进入下一步业务流。

## 4. B2B 领英 / 社媒引流与个人 IP 矩阵（对标 Taplio）

- **寄生入口（Zero-Infra）**：Chrome 扩展（直接重构 LinkedIn 网页端界面）。
- **离钱距离（High WTP）**：海外 B2B 高管和销售极度依赖 LinkedIn 获客。解决「每天不知道发什么、如何回帖引流」。
- **最后一碰（Human-in-the-Loop）**：AI 侧边栏生成符合个人风格的帖子或专业评论，用户改一两个关键词后手动点「发布」或「排期」。

## 5. 跨境电商视觉合规与 Listing 优化（Shopify Admin Inline Copilot / Chrome 插件）

- **寄生入口（Zero-Infra）**：寄生在 Shopify 后台商品编辑页，或 Amazon 卖家后台侧边栏。
- **离钱距离（High WTP）**：一键检查 Listing 是否含侵权词 / 违禁词，或直接生成符合平台算法规则的多语言商品描述。
- **最后一碰（Human-in-the-Loop）**：AI 在侧边栏提供 Before/After 对比预览，卖家确认后点「覆写至当前商品」。

---

## 底层共通公式

```
[极轻宿主入口]  Word / Sheets / Chrome / Shopify
      ↓
[离钱最近的单一 Task]  写开发信 / 审合同 / 洗数据 / 充实 Listing
      ↓
[侧边栏 Accept/Reject]  用户完成最后一碰 → 产生高价值数据闭环
```

## 切入策略

要在这个模式下切入一个新的存量方向，最好的策略不是做「大应用」，而是：**观察某个高薪岗位（外贸业务员、跨境广告优化师、合规官……）一天中打开时间最长的那个软件，然后在它上面做一层「侧边栏副驾驶」。**

---

## 待办 / 比较维度（后续填）

- [ ] 每个样本核实现状：产品是否还在、定价、ACV、宿主政策变化
- [ ] 宿主风险排序：Word / Google Workspace / Chrome / Shopify 谁最可能自营收编
- [ ] 留底强弱：哪个能把「侧边栏数据闭环」沉淀成专有数据 / 迁移成本
- [ ] 与 `b2b-ai-products-library.md` 的四大多态对齐，判断这 5 个各属哪一态
