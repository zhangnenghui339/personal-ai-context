# 分发雷达 · 波段一（巨头战略拓荒与主权政策）AI 执行规范与落地脚本

- Date: 2026-08-24
- Status: operational engineering SOP & AI Prompt
- Scope: 专注出海视角的波段一（巨头战略拓荒与国家主权政策）AI 系统提示词、数据源抓取规则、关键词过滤词典、LLM 结构化研判提示词与完整 Python 自动化发信脚本。

---

## 一、 系统提示词规范 (System Prompt for AI Agent)

```markdown
# Role: 全球分发雷达 · 波段一研判引擎 (Platform Expansions & Policy Radar)

## 1. 核心使命
你是一个专注于捕捉「万亿巨头跨国拓荒、规则断裂与国家主权政策变动引发的流量/制度套利机会」的情报分析引擎。
你的目标是识别那些【巨头为了冲数据主动给予免费流量/免佣补贴，或重大合规变动瞬间制造了供给真空】的商业切口。
坚决排除纯国内内循环信息（不监控国内抖音、小红书）。

## 2. 监控波段与数据源 (Data Sources)
- TikTok: TikTok Newsroom (Global RSS) / TikTok Shop Seller Academy
- Amazon: Amazon Seller Central News / Amazon Global Selling Blog
- Google / Meta: Google Search Central Blog (RSS) / Meta for Developers (RSS)
- Shopify: Shopify Developer Changelog (RSS)
- 关税与政策: US Federal Register / EU Trade & Digital Policies

## 3. 核心触发关键词 (Trigger Keywords)
- 扩张与新市场: "new market", "new region", "launch", "cross-border", "semi-managed", "半托管", "expansion"
- 补贴与红利: "0% commission", "zero commission", "fee waiver", "subsidy", "subsidized shipping", "seller incentive"
- 主权与合规: "de minimis", "tariff", "compliance deadline", "vat regulation", "customs", "EPR"

## 4. 输出结构要求 (Output Schema)
每次分析必须输出纯 JSON，包含：
- is_actionable (boolean): 是否有可落地的商业套利机会
- score (0~10): 机会评分（>= 7.5 分触发高优先级预警）
- platform: 涉及平台/国家
- event_summary: 一句话事实核心
- subsidy_type: 补贴或政策类型
- window_half_life: 预估红利窗口期
- arbitrage_playbook: 具体的 3 步落地执行动作（进场、选品、资产沉淀）
```

---

## 二、 核心关键词过滤词典 (Filter Matrix)

```python
# 必须命中的维度 A：业务与地区动作
EXPANSION_KEYWORDS = [
    "new market", "new country", "new region", "launching in", "expand into",
    "global selling", "cross-border", "semi-managed", "half-custody", "半托管",
    "new site", "marketplace launch", "latin america", "middle east", "europe"
]

# 必须命中的维度 B：补贴与红利动作
INCENTIVE_KEYWORDS = [
    "0% commission", "zero commission", "fee waiver", "subsidy", "subsidized",
    "free shipping", "seller incentive", "traffic boost", "invitation only",
    "early bird", "bonus", "cashback", "免佣", "流量补贴", "运费补贴"
]

# 必须命中的维度 C：主权与合规断裂动作
SOVEREIGNTY_KEYWORDS = [
    "de minimis", "tariff", "customs", "tax policy", "compliance deadline",
    "EPR", "vat regulation", "account suspension", "ban", "restriction", "关税", "合规"
]
```

---

## 三、 Python 自动化监控与发信完整脚本 (`radar_band1.py`)

```python
import os
import smtplib
import json
import hashlib
import feedparser
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ----------------------------------------------------
# 1. 核心配置区
# ----------------------------------------------------
BAND1_RSS_FEEDS = {
    "TikTok Newsroom": "https://newsroom.tiktok.com/en-us/rss",
    "Google Search Central": "https://developers.google.com/search/blog/rss.xml",
    "Shopify Changelog": "https://shopify.dev/changelog.atom",
    "Federal Register Trade": "https://www.federalregister.gov/api/v1/documents.rss?conditions%5Bterm%5D=tariff"
}

CACHE_FILE = "band1_seen_hashes.json"

# ----------------------------------------------------
# 2. 邮件发送模块 (SMTP)
# ----------------------------------------------------
def send_email(subject: str, html_body: str):
    smtp_server = os.getenv("SMTP_SERVER", "localhost")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "radar@yourdomain.com")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    recipient = os.getenv("RADAR_RECIPIENT", "your_email@domain.com")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"分发雷达 · 波段一 <{smtp_user}>"
    msg["To"] = recipient
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        if smtp_port == 465:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            server = smtplib.SMTP(smtp_server, smtp_port)
            if smtp_port == 587:
                server.starttls()
        if smtp_password:
            server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, [recipient], msg.as_string())
        server.quit()
        print(f"[{datetime.now()}] 邮件预警已发送至: {recipient}")
    except Exception as e:
        print(f"邮件发送失败: {e}")

# ----------------------------------------------------
# 3. 关键词粗筛与去重
# ----------------------------------------------------
def load_seen_hashes() -> set:
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_seen_hashes(hashes: set):
    with open(CACHE_FILE, "w") as f:
        json.dump(list(hashes), f)

def contains_trigger_keywords(text: str) -> bool:
    text_lower = text.lower()
    keywords = [
        "new market", "new region", "launch", "cross-border", "subsidy",
        "0% commission", "zero commission", "fee waiver", "tariff", "de minimis",
        "compliance", "policy update", "expansion", "seller incentive", "半托管"
    ]
    return any(kw in text_lower for kw in keywords)

# ----------------------------------------------------
# 4. LLM 结构化研判调用
# ----------------------------------------------------
def analyze_with_llm(raw_text: str, source_name: str, link: str) -> dict:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        return {
            "is_actionable": True,
            "score": 8.0,
            "platform": source_name,
            "event_summary": raw_text[:200],
            "subsidy_type": "未配置 LLM API，显示原文摘要",
            "window_half_life": "未知",
            "arbitrage_playbook": ["配置 OPENAI_API_KEY 以启用大模型自动研判 Playbook"]
        }

    prompt = f"""
    请分析以下来自 {source_name} 的官方公告，评估其是否包含可套利的商业机会：
    URL: {link}
    内容: {raw_text[:3000]}

    输出纯 JSON 格式：
    {{
      "is_actionable": true/false,
      "score": 0到10的浮点数,
      "platform": "平台名",
      "region": "涉及国家/区域",
      "event_summary": "一句话核心事实",
      "subsidy_type": "补贴或政策类型",
      "window_half_life": "预估红利窗口期",
      "arbitrage_playbook": ["步骤1", "步骤2", "步骤3"]
    }}
    """
    
    headers = {"Authorization": f"Bearer {openai_api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"}
    }
    
    try:
        resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=30)
        return json.loads(resp.json()["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"LLM 研判调用异常: {e}")
        return {"is_actionable": False, "score": 0}

# ----------------------------------------------------
# 5. 主执行流程 (Daily Pulse / Alert)
# ----------------------------------------------------
def run_band1_radar():
    seen_hashes = load_seen_hashes()
    high_value_alerts = []

    for source_name, feed_url in BAND1_RSS_FEEDS.items():
        print(f"[{datetime.now()}] 正在扫描: {source_name}...")
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:10]:
                content = entry.get("summary", "") or entry.get("description", "")
                text_to_check = f"{entry.title} {content}"
                entry_hash = hashlib.md5((entry.link + entry.title).encode()).hexdigest()

                if entry_hash in seen_hashes:
                    continue
                seen_hashes.add(entry_hash)

                if contains_trigger_keywords(text_to_check):
                    print(f"🎯 命中关键词: {entry.title}")
                    analysis = analyze_with_llm(text_to_check, source_name, entry.link)
                    
                    if analysis.get("score", 0) >= 7.5:
                        analysis["link"] = entry.link
                        analysis["source"] = source_name
                        analysis["title"] = entry.title
                        high_value_alerts.append(analysis)
        except Exception as e:
            print(f"抓取源 {source_name} 失败: {e}")

    save_seen_hashes(seen_hashes)

    if high_value_alerts:
        html_content = "<h2>🛰️ 分发雷达 · 波段一高价值预警报告</h2>"
        for alert in high_value_alerts:
            playbook_html = "".join([f"<li>{step}</li>" for step in alert.get('arbitrage_playbook', [])])
            html_content += f"""
            <div style="border: 1px solid #ddd; padding: 15px; margin-bottom: 20px; border-radius: 6px; font-family: sans-serif;">
                <h3 style="color: #d9534f; margin-top: 0;">[{alert.get('platform', '未知平台')}] {alert.get('event_summary')}</h3>
                <p><strong>机会评分:</strong> <span style="color: #f0ad4e; font-weight: bold;">{alert.get('score')} / 10</span> | <strong>预估窗口期:</strong> {alert.get('window_half_life', '未知')}</p>
                <p><strong>涉及区域:</strong> {alert.get('region', '全球')} | <strong>补贴/政策:</strong> {alert.get('subsidy_type', '无')}</p>
                <p><strong>原文链接:</strong> <a href="{alert.get('link')}" target="_blank">{alert.get('title')}</a></p>
                <h4 style="margin-bottom: 5px;">🚀 建议套利路径 (Action Playbook):</h4>
                <ol style="padding-left: 20px;">{playbook_html}</ol>
            </div>
            """
        send_email(f"🚨 [分发雷达] 发现 {len(high_value_alerts)} 个巨头拓荒/政策高价值机会", html_content)
    else:
        print("今日无高价值突破性事件，保持静默。")

if __name__ == "__main__":
    run_band1_radar()
```

---

## 四、 部署与调度说明 (Crontab)

```bash
# 每天早上 08:00 自动执行波段一轻量扫描（发现 >= 7.5 分机会自动发邮件，无机会静默）
0 8 * * * /usr/bin/python3 /path/to/radar_band1.py >> /var/log/radar_band1.log 2>&1
```
