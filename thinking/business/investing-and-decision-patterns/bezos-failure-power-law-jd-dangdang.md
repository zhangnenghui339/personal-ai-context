# Bezos：失败容忍、幂律下注与京东/当当对照

- Date: 2026-08-27
- Status: working note
- Scope: 解释 Bezos 为什么允许大量小失败、Amazon 如何把失败转化为资产，以及京东/当当学习 Amazon 后为什么走出不同结果。
- 关联文件：`thinking/business/investing-and-decision-patterns/bezos-market-leadership-window-terminal-value.md`、`thinking/business/potential-energy-and-gaps/hobart-arbitrage-infrastructure.md`

---

## 一、核心结论

**Bezos 的真正优势不是“比别人少失败”，而是构建了一套让失败具有正期望值的资本配置系统。**

京东学到了 Amazon 的 **Retail + Logistics**；当当更多学到了 **Online Bookstore → General Merchandise**。但 Amazon 真正拉开差距的是第三层：

> **不断把零售产生的内部能力抽象成平台和基础设施，再开放给全社会。**

因此三者最终的战略抽象层级不同：

| 公司 | 最终抽象 |
|---|---|
| 当当 | 卖商品 |
| 京东 | 卖商品 + 供应链基础设施 |
| Amazon | Commerce + Marketplace + Logistics + Cloud Infrastructure + Advertising |

简化为一句话：

> **当当学到了商品，京东学到了基础设施，Bezos 真正构建的是“基础设施生成器”。**

---

## 二、Amazon 的典型失败案例

| 项目 | 结果 | 失败后留下的东西 |
|---|---|---|
| **Fire Phone** | 2014 年上市后迅速失败，并产生较大资产减记 | 硬件、语音、机器学习团队和经验部分迁移到 Echo / Alexa |
| **Amazon Auctions** | 挑战 eBay 失败 | 验证独立 Auction 入口难以撬动已有网络效应 |
| **zShops** | 独立第三方店铺模式没有形成预期规模 | 最终推动 Amazon 将第三方 Seller 直接嵌入核心商品页，演化为 Marketplace |
| **Amazon Restaurants** | 关闭 | 本地履约、即时配送、餐饮供给侧运营经验 |
| **Amazon Destinations** | 关闭 | 旅游垂类的需求与供应链经验 |
| **Dash Button** | 实体按钮退出 | 自动补货逻辑继续迁移到 Alexa / Smart Reorders 等数字化入口 |

关键不是这些项目失败了，而是：

```text
项目失败
→ 人才没有归零
→ 技术没有归零
→ 数据没有归零
→ 组织认知没有归零
→ 下一轮实验的边际成本下降
```

这可以定义为：**Failure Assetization（失败资产化）**。

传统失败模型：

```text
投入 → 失败 → 归零
```

Bezos 理想中的失败模型：

```text
投入 → 失败
      ↓
人才 / 技术 / 数据 / 基础设施 / 认知残值
      ↓
下一轮实验
```

因此衡量实验损失不能只看：

`Loss = 投入 − 项目收入`

更准确的是：

`Net Loss = 投入 − 项目收入 − 可复用资产残值`

---

## 三、为什么 Fire Phone 仍然可以是“好失败”

Fire Phone 本身商业上失败，但 Amazon 已经拥有 Cloud、Machine Learning、Voice Technology、Hardware Team 和庞大 Customer Base。

因此失败后的资产迁移可以表示为：

```text
Fire Phone
│
├─ Voice Recognition
├─ Hardware Engineers
├─ Machine Learning
├─ Cloud
└─ Consumer Device Experience
        ↓
     Echo / Alexa
```

Bezos 的关键不是“容忍失败”，而是：

> **尽量让失败发生在可复用能力附近。**

也就是说，同样亏掉 1 亿美元：

- 一个完全孤立、没有残值的项目，损失接近 1 亿；
- 一个产生核心技术、团队、数据和平台能力的项目，经济损失可能远低于账面损失。

所以“允许失败”不能脱离**资产残值**讨论。

---

## 四、Amazon Auctions → zShops → Marketplace：失败不是随机试错，而是连续逼近

Amazon 先做 Auctions，试图复制 eBay 的拍卖模式，失败。

随后做 zShops，让第三方商家拥有独立店铺，仍然没有形成预期规模。

真正的突破不是第三次“再试一次”，而是改变了系统结构：

> **不再要求消费者进入一个独立的第三方市场，而是把第三方商品直接放进 Amazon 原本已经拥有流量的 Product Detail Page。**

于是：

```text
Amazon 原有买家流量
        ↓
同一商品页展示 Amazon + Third-party Sellers
        ↓
Seller 直接共享 Amazon 已有 Distribution
        ↓
Selection 增加
        ↓
消费者体验增强
        ↓
更多买家
        ↓
更多 Seller
```

这说明 Bezos 的实验逻辑不是：

> 失败 → 换一个完全无关方向。

而更接近：

> **失败 → 提取失败信息 → 调整系统结构 → 再下注。**

失败本身也是 Information Acquisition。

---

## 五、为什么当当没有复制出 Amazon

当当学习的是 Amazon 最表层、最容易观察到的路径：

```text
Books
→ General Merchandise
→ Marketplace
```

但“图书”对于 Bezos 来说只是 **Wedge（切入口）**，不是商业本质。

图书之所以适合 1990 年代互联网，是因为：

- SKU 极多，线下实体店存在物理货架上限；
- ISBN 标准化，产品高度可搜索；
- 消费者无需试穿/试用；
- 批发供应体系相对集中；
- 互联网天然可以提供远大于实体店的 Selection。

所以 Bezos 的推理其实是：

```text
Internet 出现
→ 新 Distribution Infrastructure 出现
→ 哪个旧行业最容易被新基础设施重新定价？
→ Books
```

不是：

```text
我喜欢图书
→ 建一个网上书店
→ 再卖百货
```

当当后续进入百货时，图书原来的结构优势迅速下降：

- General Merchandise SKU 与供应链复杂度大幅增加；
- Inventory Risk 增加；
- Logistics 成为竞争核心；
- 第三方 Seller 的配送质量难以统一；
- 原有“网上书店”品牌认知难以自然迁移成 Everything Store。

因此，当当更接近：

> **复制 Amazon 的产品序列，没有复制产生这个产品序列的底层能力。**

---

## 六、京东为什么比当当更接近 Amazon

京东真正抓住的是：

> **Customer Experience → Logistics Infrastructure。**

刘强东长期坚持自建仓储配送，本质上和 Bezos 的底层逻辑高度一致：

```text
更多订单
→ 更高仓储/物流利用率
→ 单位履约成本下降
→ 更快配送 / 更可靠体验
→ 更多用户
→ 更多订单
```

京东因此不只是 Retailer，而逐渐拥有了可以独立对外销售的 Logistics / Supply Chain Infrastructure。

这意味着它已经完成了 Bezos 模型里极关键的一步：

> **把原本服务内部交易的 Cost Center，变成 External Revenue Infrastructure。**

所以不能简单说京东“失败复制 Amazon”。它事实上已经成为大型基础设施型企业。

真正差距是：

> **京东主要把 Commerce 能力抽象成 Supply Chain Infrastructure；Amazon 进一步把大量内部问题抽象成跨行业基础设施。**

最典型的就是 AWS。

---

## 七、Amazon 最大的能力：把内部成本中心产品化

Amazon 的抽象路线可以表示为：

```text
内部问题
↓
内部能力
↓
标准化
↓
服务化 / API 化
↓
开放第三方
↓
独立 Revenue Engine
↓
新 Flywheel
```

典型案例：

| Amazon 内部问题/能力 | 最终外部化 |
|---|---|
| 第三方商家扩充 Selection | Marketplace |
| 仓储配送能力 | FBA |
| 高频用户留存 | Prime |
| 大规模计算/存储基础设施 | AWS |
| 购物 Intent 与流量 | Amazon Ads |

这说明 Amazon 的真正母能力不是 E-commerce，而是：

> **不断发现内部已经规模化解决的问题，再判断这些问题是否也是全市场的公共问题，然后把内部能力外部产品化。**

可以称为：**Infrastructure Extraction（基础设施抽取）**。

---

## 八、允许大量小失败，等待极少数超级成功

Bezos 在 2015 年致股东信中给出一个非常清楚的例子：

> “Given a 10% chance of a 100x payoff, you should take that bet every time.”

这是典型的 **Asymmetric Payoff + Power Law**。

假设做 10 个独立实验，每个最多损失 1：

```text
9 个失败： -9
1 个成功： +100
----------------
组合结果： +91
```

成功率只有 10%，但整个 Portfolio 的期望值非常高。

因此：

> **单项目成功率低，不等于系统决策质量低。**

如果收益分布具有幂律特征，真正重要的是：

1. 单次失败是否有限；
2. 能否连续获得下注次数；
3. Winner 的 Upside 是否足够大；
4. Winner 是否能形成长期复利结构。

---

## 九、为什么商业世界比棒球更适合这种模型

Bezos 曾用棒球作类比。

棒球的单次成功存在天然上限：一次 Home Run 最多就是一个 Home Run。

但商业的单次成功没有类似上限：

```text
Fire Phone       -1
Amazon Auctions  -1
zShops           -1
其他实验          -1
AWS              +1000
```

AWS、Marketplace、Prime 这种超级赢家，理论上可以覆盖大量失败实验。

所以 Bezos 的关键不是“提高每次击球命中率”，而是：

> **保证自己长期拥有足够多次击球机会，并确保其中某些机会具有 100x/1000x 的非对称收益。**

这与 Venture Capital 的数学本质非常接近：

- 多数项目失败或平庸；
- 少数项目产生绝大多数 Fund Return；
- 因此不能用平均项目回报来设计投资组合。

---

## 十、但这绝不等于“随便烧钱”

Bezos 式实验至少需要同时满足两个核心前提。

### 10.1 Downside 必须可控

实验失败不能杀死母公司，也不能永久破坏核心品牌/现金流/资产负债表。

也就是：

```text
Maximum Loss << Survival Capital
```

### 10.2 Upside 必须足够大

如果一个项目：

```text
Downside = 100
Upside   = 120
```

即使成功概率高，也不属于 Bezos 式幂律下注。

真正值得承担高失败率的是：

```text
Downside = 1
Upside   = 100 / 1000
```

可形式化为：

`EV = P(success) × Upside − P(failure) × Downside`

但 Bezos 模型还应该再加入一项：**Residual Asset Value（失败残值）**。

更完整：

`Adjusted EV = P(success) × Upside − P(failure) × (Downside − Residual Asset Value)`

这就解释了为什么同样是高失败率项目，Amazon 更愿意下注那些能够沉淀：

- Software / Code
- Infrastructure
- Data
- Talent
- Distribution
- Customer Relationship
- Seller Network
- Brand / Trust

的项目。

---

## 十一、“失败容忍”真正应该设计成 Portfolio，而不是文化口号

错误理解：

> 鼓励创新，所以允许失败。

Bezos 更接近：

```text
大量小额可逆实验
        ↓
控制每次 Downside
        ↓
快速取得真实数据
        ↓
砍掉弱信号
        ↓
对强信号持续加码
        ↓
极少数项目进入规模化阶段
        ↓
极少数超级赢家覆盖整个实验组合
```

因此系统分两阶段：

### 阶段 A：探索（Explore）

特点：

- Two-way Door；
- 小仓位；
- 高失败率；
- 目标不是利润，而是 Information Gain。

### 阶段 B：利用（Exploit）

一旦出现强信号：

- 大幅增加资本投入；
- 快速争取 Market Leadership；
- 建设难以复制的 Infrastructure；
- 把短暂套利窗口变成长期 Flywheel。

真正厉害的地方是：

> **失败时像 VC，成功以后像垄断型基础设施公司。**

---

## 十二、与“势差 → 管道 → 资产”模型的统一

这套模型可以继续接入现有的机会雷达：

`机会质量 ≈ 势差 × Upside × 可复用资产率 ÷ 失败成本`

进一步拆解：

| 维度 | 核心问题 |
|---|---|
| **势差** | 市场现在是否存在尚未被重新定价的结构变化？ |
| **Upside** | 成功后是 2x 还是可能 100x？ |
| **Downside** | 验证失败最多损失多少？ |
| **Residual Asset** | 失败后留下多少 Code / Data / Distribution / Brand / Network？ |
| **Flywheel Potential** | 成功后今天的增长能否降低明天的增长成本？ |
| **Infrastructure Potential** | 能否把内部能力继续卖给第三方？ |

例如：

| 实验 | 失败后的典型残值 |
|---|---|
| 普通一次性 Dropshipping | 极低 |
| SEO 网站 | Domain / Content / Keyword Data / Backlinks |
| AI App | Code / User Data / Distribution / Prompt Workflow |
| API Infrastructure | Code / Developer Network / Usage Data |
| Marketplace | Buyers / Sellers / Transaction Graph / Trust System |

所以最值得下注的实验不是单纯“成功概率最高”，而是：

> **失败时损失有限并留下砖；成功时能产生极大的非对称收益，并最终把砖修成路。**

这与 `thinking/business/potential-energy-and-gaps/hobart-arbitrage-infrastructure.md` 的核心判据一致：

> **Arbs close, infrastructure remains.**

---

## 十三、最终压缩

Bezos 的资本配置算法可以压缩为：

```text
发现结构变化
→ 用小成本获取信息
→ 接受多数实验失败
→ 保证失败具有资产残值
→ 找到少数非对称机会
→ 强信号出现后重仓
→ 把成功项目转化为基础设施
→ 基础设施形成 Flywheel
→ 极少数超级赢家覆盖大量失败
```

因此最值得保留的一句话不是“Amazon 很能容忍失败”，而是：

> **Bezos 把失败设计成有限损失，把成功设计成无限收益，再让失败过程本身沉淀资产。**

---

## 来源 / 待进一步核验

- Amazon 2015 Letter to Shareholders：10% chance / 100x payoff、幂律回报与实验思想
- Amazon 2018 Letter to Shareholders：随着公司规模扩大，失败实验规模也应扩大；Big Winners 足以覆盖大量失败
- Amazon 官方关于 Auctions / zShops / Marketplace 演化的历史材料
- Amazon 官方关于 Fire Phone 与 Echo / Alexa 团队、技术迁移的回顾
- 京东历年 Annual Report / Earnings Release：JD Retail、JD Logistics、Supply Chain Infrastructure
- 当当上市期间 SEC 20-F：General Merchandise、Marketplace、Inventory / Logistics 风险

> 注：本文件定位为 working note；用于公开文章或正式研究时，具体财务数字、逐字语录和历史因果关系应再次回到 Amazon Shareholder Letters、SEC filings、京东年报、当当 20-F 等一手材料复核。