#!/usr/bin/env python3
"""
AI 工具評測文章自動生成器
自動生成符合 SEO 的 AI 工具評測文章
"""

import os
import random
from datetime import datetime, timedelta

# AI 工具資料庫
AI_TOOLS = [
    {
        "name": "ChatGPT",
        "category": "AI 聊天機器人",
        "affiliate_url": "https://chat.openai.com",
        "pros": ["強大的對話能力", "多語言支持", "免費版本可用", "Plugins 擴展功能"],
        "cons": ["有使用限制", "知識有截止日期", "需要科學上網"],
        "price": "免費 / $20/月 (Plus)",
        "best_for": "日常對話、寫作輔助、程式問題"
    },
    {
        "name": "Claude",
        "category": "AI 助手",
        "affiliate_url": "https://claude.ai",
        "pros": ["長文本處理能力強", "安全性高", "分析深入", "支持檔案上傳"],
        "cons": ["需要有 Anthropic 帳號", "回應速度有時較慢"],
        "price": "免費 / $20/月 (Pro)",
        "best_for": "長文分析、創意寫作、學術研究"
    },
    {
        "name": "Notion AI",
        "category": "智慧筆記",
        "affiliate_url": "https://notion.so/product/ai",
        "pros": ["無縫整合 Notion", "自動總結功能", "智慧搜尋", "多語言翻譯"],
        "cons": ["需要 Notion 訂閱", "功能相對有限"],
        "price": "$10/月起",
        "best_for": "知識管理、會議紀錄、文件整理"
    },
    {
        "name": "Canva AI",
        "category": "AI 設計",
        "affiliate_url": "https://www.canva.com/ai/",
        "pros": ["操作簡單", "Magic Design 功能", "AI 圖像生成", "豐富模板"],
        "cons": ["Pro 功能需要付費", "輸出有浮水印（免費版）"],
        "price": "免費 / $12.99/月 (Pro)",
        "best_for": "社群媒體圖片、簡報、海報設計"
    },
    {
        "name": "Midjourney",
        "category": "AI 圖像生成",
        "affiliate_url": "https://www.midjourney.com",
        "pros": ["生成品質極高", "藝術風格多樣", "社群活躍", "持續更新"],
        "cons": ["需要 Discord", "需要付費才能使用", "有使用限制"],
        "price": "$10/月起",
        "best_for": "數位藝術、概念設計、行銷素材"
    },
    {
        "name": "Jasper",
        "category": "AI 文案生成",
        "affiliate_url": "https://www.jasper.ai",
        "pros": ["專為行銷設計", "多種模板", "品牌聲音設定", "團隊協作"],
        "cons": ["價格較高", "需要學習使用方式"],
        "price": "$49/月起",
        "best_for": "行銷文案、廣告文案、SEO 文章"
    },
    {
        "name": "Runway",
        "category": "AI 影片",
        "affiliate_url": "https://runwayml.com",
        "pros": ["文字轉影片", "智慧編輯", "多項 AI 功能", "持續上新功能"],
        "cons": ["處理時間較長", "高品質輸出需付費"],
        "price": "免費試用 / $15/月起",
        "best_for": "影片創作、內容行銷、社交媒體"
    },
    {
        "name": "Copy.ai",
        "category": "AI 文案工具",
        "affiliate_url": "https://www.copy.ai",
        "pros": ["操作簡單", "大量模板", "多語言支持", "有免費方案"],
        "cons": ["生成品質參差不齊", "需要人工潤飾"],
        "price": "免費 / $36/月起",
        "best_for": "社群貼文、郵件行銷、產品描述"
    },
    {
        "name": "Grammarly",
        "category": "AI 寫作助手",
        "affiliate_url": "https://www.grammarly.com",
        "pros": ["即時語法檢查", "風格建議", "多種平台支援", "瀏覽器擴展"],
        "cons": ["高級功能需付費", "有時會誤判"],
        "price": "免費 / $12/月起",
        "best_for": "英文寫作、商業郵件、論文檢查"
    },
    {
        "name": "DALL-E 3",
        "category": "AI 圖像生成",
        "affiliate_url": "https://openai.com/dall-e-3",
        "pros": ["理解複雜描述", "文字生成準確", "與 ChatGPT 整合", "安全過濾"],
        "cons": ["需要 OpenAI 帳號", "生成有額度限制"],
        "price": "免費（含額度）/ $15起",
        "best_for": "插圖創作、概念視覺化、品牌素材"
    }
]

# 文章標題模板
TITLE_TEMPLATES = [
    "{tool_name} 評測 2025：完整使用心得與教學",
    "【{tool_name}】真的好用嗎？深度評測告訴你",
    "{tool_name} vs 競爭對手：哪個更值得訂閱？",
    "2025 年必用的 AI 工具：{tool_name} 完整評測",
    "從零開始使用 {tool_name}：新手完整教學",
    "為什麼專業人士都推薦 {tool_name}？",
    "{tool_name} 評測：功能、價格、性價比全面分析",
    "【獨家】{tool_name} 一個月使用報告",
]

# 內容段落模板
INTRO_TEMPLATE = """
{tool_name} 是目前市面上最受歡迎的 {category} 工具之一。在這篇評測中，我將分享實際使用的完整心得，幫助你決定 {tool_name} 是否適合你。

作為一個每天都在使用各種 AI 工具的人，我對 {tool_name} 進行了為期一個月的深度測試。以下是我的真實使用感受。
"""

PROS_CONS_TEMPLATE = """
## {tool_name} 的優點

{tool_name} 有以下幾個突出的優點：

{pros_list}

## {tool_name} 的缺點

當然，{tool_name} 也不是完美的：

{cons_list}
"""

FEATURES_TEMPLATE = """
## 主要功能特色

{tool_name} 提供以下核心功能：

### 功能一：{feature1}
這個功能特別適合需要經常處理相關任務的用戶。

### 功能二：{feature2}
實際使用下來，這個功能確實能大幅提升效率。

### 功能三：{feature3}
對於專業用戶來說，這是不可或缺的功能。
"""

PRICE_TEMPLATE = """
## 定價方案

{tool_name} 的定價如下：

| 方案 | 價格 | 適合人選 |
|------|------|---------|
| 免費版 | {price_free} | 初次體驗 |
| 付費版 | {price_paid} | 專業用戶 |

整體來說，{tool_name} 的定價在同類工具中屬於{price_comment}。
"""

CONCLUSION_TEMPLATE = """
## 總結：{tool_name} 值得使用嗎？

經過完整的評測，我的結論是：

**{conclusion}**

{tool_name} 特別適合：
- {best_for_1}
- {best_for_2}
- {best_for_3}

如果你符合以上需求，強烈建議你嘗試 {tool_name}！

👉 [立即開始使用 {tool_name}]({affiliate_url})
"""

FAQ_TEMPLATE = """
## 常見問題 FAQ

**Q: {tool_name} 需要付費嗎？**
A: {tool_name} 有免費版本，但進階功能需要付費訂閱。

**Q: {tool_name} 支援中文嗎？**
A: 是的，{tool_name} 支援中文介面和中文輸入。

**Q: {tool_name} 安全嗎？**
A: {tool_name} 由知名公司開發，有嚴格的隱私政策保護用戶數據。

**Q: 我該如何開始使用？**
A: 點擊上方連結即可免費註冊開始使用。
"""

def generate_slug(title):
    """將標題轉換為 URL 友好的 slug"""
    slug = title.lower()
    # 移除特殊字符
    for char in [' ', '：', '！', '？', '【', '】', '（', '）', '/', '\\', '"', "'"]:
        slug = slug.replace(char, '-')
    # 移除多餘的破折號
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug

def generate_article(tool, date):
    """為指定工具生成完整文章"""
    title_template = random.choice(TITLE_TEMPLATES)
    title = title_template.format(tool_name=tool["name"])
    slug = generate_slug(title)

    # 生成日期格式
    date_str = date.strftime("%Y-%m-%d")
    filename = f"{date_str}-{slug}.md"

    # 處理優點列表
    pros_list = "\n".join([f"- {pro}" for pro in tool["pros"][:4]])
    cons_list = "\n".join([f"- {con}" for con in tool["cons"][:3]])

    # 根據類別生成功能描述
    features = {
        "AI 聊天機器人": ("智能對話", "內容生成", "程式輔助"),
        "AI 助手": ("長文分析", "創意寫作", "檔案處理"),
        "智慧筆記": ("自動總結", "智慧搜尋", "翻譯功能"),
        "AI 設計": ("Magic Design", "AI 圖像生成", "智慧去背"),
        "AI 圖像生成": ("文字生成圖像", "風格遷移", "圖像編輯"),
        "AI 文案生成": ("多模板支援", "品牌風格", "批量生成"),
        "AI 影片": ("文字轉影片", "智慧剪輯", "特效添加"),
        "AI 文案工具": ("社群文案", "郵件範本", "產品描述"),
        "AI 寫作助手": ("語法檢查", "風格建議", "抄襲檢測"),
    }

    feature_tuple = features.get(tool["category"], ("智能功能", "自動處理", "效率提升"))

    # 生成結論
    conclusions = [
        f"{tool['name']} 絕對值得一試，特別是其核心功能非常出色。",
        f"如果你需要 {tool['category']} 工具，{tool['name']} 是很好的選擇。",
        f"{tool['name']} 的性價比很高，付費版本的功能絕對值得。",
        f"從實際使用來看，{tool['name']} 能顯著提升工作效率。",
    ]

    # 處理價格
    price_parts = tool["price"].split("/")
    price_free = price_parts[0].strip() if price_parts else "免費"
    price_paid = price_parts[1].strip() if len(price_parts) > 1 else "付費版"

    # 判斷價格評論
    if "免費" in tool["price"]:
        price_comment = "合理的，性價比不錯"
    else:
        price_comment = "中等價位"

    # 生成 best_for 列表
    best_for = tool["best_for"].split("、")
    best_for_1 = best_for[0] if len(best_for) > 0 else "一般用戶"
    best_for_2 = best_for[1] if len(best_for) > 1 else best_for[0]
    best_for_3 = best_for[2] if len(best_for) > 2 else best_for[0]

    # 組合文章內容
    content = f"""---
layout: post
title: "{title}"
date: {date_str}
categories: [{tool["category"]}, 評測, 工具推薦]
---

{INTRO_TEMPLATE.format(tool_name=tool["name"], category=tool["category"])}

{tool["name"]} 是 {tool["category"]} 領域的領導者之一。接下來讓我們深入了解這款工具。

{PROS_CONS_TEMPLATE.format(tool_name=tool["name"], pros_list=pros_list, cons_list=cons_list)}

{FEATURES_TEMPLATE.format(tool_name=tool["name"], feature1=feature_tuple[0], feature2=feature_tuple[1], feature3=feature_tuple[2])}

{PRICE_TEMPLATE.format(tool_name=tool["name"], price_free=price_free, price_paid=price_paid, price_comment=price_comment)}

## 實際使用場景

### 場景一：日常工作
在日常工作中，{tool["name"]} 可以幫助你快速完成重複性任務。

### 場景二：專業項目
對於專業項目，{tool["name"]} 的進階功能能提供更好的支援。

### 場景三：學習提升
如果你想學習新技能，{tool["name"]} 也是很好的輔助工具。

{CONCLUSION_TEMPLATE.format(
    tool_name=tool["name"],
    conclusion=random.choice(conclusions),
    best_for_1=best_for_1,
    best_for_2=best_for_2,
    best_for_3=best_for_3,
    affiliate_url=tool["affiliate_url"]
)}

{FAQ_TEMPLATE.format(tool_name=tool["name"])}

---

*💡 注意：本文包含聯盟連結。如果你通過本文連結訂閱，我可能會獲得佣金，這不會增加你的費用，但能幫助支持這個網站的運營。*

*📌 這個網站由 AI 自動生成內容，每日更新最新 AI 工具評測。*
"""

    return filename, content

def main():
    """主函數：生成文章並保存"""
    posts_dir = "_posts"
    os.makedirs(posts_dir, exist_ok=True)

    # 檢查現有文章
    existing_files = set(os.listdir(posts_dir))

    # 計算下一篇文章的日期
    today = datetime.now()
    existing_count = len([f for f in existing_files if f.endswith('.md')])
    next_date = today + timedelta(days=existing_count)

    # 選擇一個還沒有評測的工具
    used_tools = set()
    for f in existing_files:
        for tool in AI_TOOLS:
            if tool["name"] in f:
                used_tools.add(tool["name"])

    available_tools = [t for t in AI_TOOLS if t["name"] not in used_tools]

    if not available_tools:
        # 如果所有工具都評測過了，隨機選擇一個
        available_tools = AI_TOOLS

    # 選擇工具
    tool = random.choice(available_tools)

    # 生成文章
    filename, content = generate_article(tool, next_date)
    filepath = os.path.join(posts_dir, filename)

    # 保存文章
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 文章已生成: {filename}")
    print(f"📝 主題: {tool['name']} 評測")
    print(f"🔗 聯盟連結: {tool['affiliate_url']}")

    return filepath

if __name__ == "__main__":
    main()
