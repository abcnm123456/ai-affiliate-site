# 🚀 部署指南 - AI 聯盟行銷網站

## 快速開始（5分鐘完成）

### 步驟 1：上傳到 GitHub

**方法 A：使用 GitHub Desktop（推薦新手）**

1. 打開 [GitHub Desktop](https://desktop.github.com/) 並登入
2. 點擊 `File` → `Add Local Repository`
3. 選擇 `ai-affiliate-site` 資料夾
4. 點擊 `Publish repository`
5. 設定：
   - Name: `ai-affiliate-site`
   - 勾選 "Keep this code private"（可選）
   - 點擊 `Publish Repository`

**方法 B：使用命令列**

```bash
# 進入專案資料夾
cd ai-affiliate-site

# 初始化 Git（如果還沒有的話）
git init

# 添加所有檔案
git add .

# 提交
git commit -m "Initial commit: AI Tools Review Site"

# 添加遠端（把 YOUR_USERNAME 換成你的 GitHub 用戶名）
git remote add origin https://github.com/YOUR_USERNAME/ai-affiliate-site.git

# 推送上去
git branch -M main
git push -u origin main
```

### 步驟 2：啟用 GitHub Pages

1. 在 GitHub 上開啟你的專案
2. 點擊 `Settings`（設定）
3. 左側選單找到 `Pages`
4. 在 `Source` 下拉選單選擇：
   - Branch: `main`
   - Folder: `/ (root)`
   - 點擊 `Save`
5. 等待 1-2 分鐘，你的網站就會上線！

### 步驟 3：設定自動化（可選）

要讓網站每天自動生成新文章：

1. 進入你的 GitHub 專案
2. 點擊 `Settings` → `Secrets and variables` → `Actions`
3. 點擊 `New repository secret`
4. 名稱：`GH_TOKEN`
5. 值：你的 GitHub Personal Access Token

**如何建立 PAT：**
1. 進入 GitHub Settings
2. 左側點擊 `Developer settings`
3. `Personal access tokens` → `Tokens (classic)`
4. 點擊 `Generate new token (classic)`
5. 勾選 `repo` 權限
6. 點擊 `Generate token`
7. **立刻複製這個 token**（只會顯示一次）

### 步驟 4：驗證系統

1. 在 GitHub 專案頁面，點擊 `Actions` 分頁
2. 你應該會看到 "Daily AI Article Generator" workflow
3. 點擊它，然後點擊 `Run workflow` → `Run workflow`
4. 等待執行完成
5. 檢查 `_posts` 資料夾是否出現了新文章

---

## 🎉 完成！

你的網站現在應該可以在：
```
https://YOUR_USERNAME.github.io/ai-affiliate-site/
```

---

## 系統工作原理

```
┌─────────────────────────────────────────────────────────┐
│                      每日自動化流程                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  每天 UTC 00:00 (台灣時間 早上8點)                        │
│         │                                               │
│         ▼                                               │
│  ┌──────────────────┐                                  │
│  │ GitHub Actions   │                                  │
│  │ 自動觸發腳本      │                                  │
│  └────────┬─────────┘                                  │
│           │                                             │
│           ▼                                             │
│  ┌──────────────────┐                                  │
│  │ generate_articles.py │                              │
│  │ - 選擇一個 AI 工具                                    │
│  │ - 生成評測文章                                        │
│  │ - 插入聯盟連結                                        │
│  └────────┬─────────┘                                  │
│           │                                             │
│           ▼                                             │
│  ┌──────────────────┐                                  │
│  │ GitHub Pages     │                                  │
│  │ 自動部署更新      │                                  │
│  └──────────────────┘                                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 如何賺錢？

### 當前設定的聯盟連結
| 工具 | 聯盟計劃 |
|------|---------|
| Notion AI | [申請 Notion 聯盟](https://www.notion.so/affiliates) |
| Canva | [申請 Canva 聯盟](https://www.canva.com/affiliates/) |
| Jasper | [申請 Jasper 聯盟](https://www.jasper.io/affiliate) |
| Grammarly | [申請 Grammarly 聯盟](https://www.grammarly.com/affiliates) |

### 如何獲得真實聯盟連結

1. **註冊聯盟計劃**：到各平台的聯盟頁面申請
2. **替換連結**：編輯 `generate_articles.py` 中的 `affiliate_url`
3. **追蹤成效**：每個聯盟計劃都有後台查看點擊和轉換

### 開始賺錢的時間線

| 時間 | 預期成果 |
|------|---------|
| 第 1 個月 | 建立內容，申請聯盟計劃 |
| 第 2-3 個月 | 開始有自然流量 |
| 第 4-6 個月 | 第一筆聯盟收入 |
| 第 6-12 個月 | 穩定被動收入 |

---

## 常見問題

**Q: 網站多久更新一次？**
A: 預設每天 UTC 00:00 自動更新一次（台灣時間早上8點）。

**Q: 我可以手動觸發更新嗎？**
A: 可以！在 GitHub Actions 頁面點擊 "Run workflow"。

**Q: 如何修改網站名稱或描述？**
A: 編輯 `_config.yml` 文件。

**Q: 文章內容是中文還是英文？**
A: 目前是繁體中文。如需英文，編輯 `generate_articles.py`。

**Q: 需要付費嗎？**
A: 完全免費！GitHub Pages、GitHub Actions 都是免費的。

---

## 下一步優化建議

1. **申請更多聯盟計劃** - 申請 Amazon Associates, ShareASale 等
2. **自訂域名** - 透過 Namecheap 或 GoDaddy 購買（約 $10/年）
3. **SEO 優化** - 添加 meta tags, sitemap, robots.txt
4. **分析工具** - 接入 Google Analytics
5. **郵件訂閱** - 接入 Mailchimp 或 ConvertKit

---

*祝你創業成功！ 🚀*
