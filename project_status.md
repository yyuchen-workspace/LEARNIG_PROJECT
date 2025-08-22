# Flask 待辦事項管理器 - 專案狀態

## 目前進度
**日期：** 2025-08-22  
**學習階段：** 準備階段  
**GitHub 儲存庫：** https://github.com/yyuchen-workspace/LEARNIG_PROJECT.git  
**完成項目：**
- ✅ 建立 .gitignore 檔案
- ✅ 建立專案狀態追蹤檔案
- ✅ 上傳至 GitHub 儲存庫
- ✅ 基本 Flask 應用結構設定

## 下一步計畫
根據 CLAUDE.md 中的 4 週學習計畫，接下來需要：

### 第 1 週：Flask 基礎 + 簡單任務管理
**待完成項目：**
- [ ] 建立基本的 Flask 應用結構
- [ ] 設定路由和基本的 HTML 模板
- [ ] 實作簡單的任務列表功能（不含資料庫）
- [ ] 建立任務新增、顯示、刪除功能

## 技術決策記錄
- **開發環境：** Python 3.8+
- **框架：** Flask + SQLAlchemy
- **資料庫：** SQLite（開發階段）
- **前端：** HTML + CSS (Bootstrap) + Jinja2

## 專案結構規劃
```
learning_project/
├── app.py              # 主應用檔案
├── templates/          # HTML 模板
├── static/            # CSS, JS 靜態檔案
├── models.py          # 資料庫模型（第2週加入）
├── requirements.txt   # Python 套件清單
└── config.py         # 應用設定
```

## 學習重點
- Flask 路由與請求處理
- Jinja2 模板引擎
- HTML 表單處理
- SQLAlchemy ORM（第2週）
- 用戶認證系統（第3週）

## 跨電腦工作流程
**clone 專案：**
```bash
git clone https://github.com/yyuchen-workspace/LEARNIG_PROJECT.git
cd LEARNIG_PROJECT
```

**開始工作前：**
```bash
git pull origin main  # 拉取最新版本
```

**工作完成後：**
```bash
git add .
git commit -m "描述你的變更"
git push origin main
```

## 注意事項
- 遵循 CLAUDE.md 中的 4 週計畫進行
- 每週都要達成設定的里程碑
- 優先編輯現有檔案而非建立新檔案
- 不要提前建立文件檔案除非必要
- 每次工作前記得先 git pull，完成後要 git push