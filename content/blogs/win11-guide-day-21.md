---
title: "Day 21：Windows 11中打造你的離線AI工作站：從安裝到應用的完整指南"
date: 2024-10-10T10:15:36+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "今天來聊聊關於「離線使用 AI 的功能」。雖然目前各大廠牌（如 ChatGPT、Gemini、Claude）都提供了一定的免費使用額度，但這些額度通常很快就會被消耗完，無法應付長期需求。 針對這個問題"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 21／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

今天來聊聊關於「**離線使用 AI 的功能**」。雖然目前各大廠牌（如 **ChatGPT**、**Gemini**、**Claude**）都提供了一定的免費使用額度，但這些額度通常很快就會被消耗完，無法應付長期需求。

針對這個問題，雖然我的筆電不符合**AI PC NPU 效能標準（至少 40 TOPS）**，但利用更輕量的 AI 模型，例如 **llama 3.2 - 3b 小語言模型**，依然能在我的筆電上運行，提供一些離線測試的能力。

接下來，我將一步步介紹如何在 **Windows 11 環境**中安裝這些工具，讓我們一起完成這個過程吧！

---

## 環境介紹

筆者的設備為 **Lenovo X1 Carbon**，是一台輕便型的商務筆電，GPU 性能較為有限，因此選擇了相對輕量的模型來執行。

## 安裝環境準備

在開始安裝之前，我們需要先準備以下工具：

1. [**Ollama**](https://ollama.com/download/windows)（下載並安裝）

![Day 21 截圖 1](/images/blogs/win11-guide/day-21-1.png)

2. [**Docker Desktop**](https://www.docker.com/products/docker-desktop)（支援 Windows 版本）
3. [**Open-WebUI**](https://docs.openwebui.com/)（用於管理模型的 Web 介面）

![Day 21 截圖 2](/images/blogs/win11-guide/day-21-2.png)

開啟Terminal 執行安裝 **Open-WebUI**

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always [ghcr.io/open-webui/open-webui:main](http://ghcr.io/open-webui/open-webui:main)
```

這邊提醒一下 `3000` 是我們本地使用的port 我們可以自己更換，不要跟原有的服務衝突

筆者這邊是使用 `4000:8080`

open-webui 成功在docker 執行

![Day 21 截圖 3](/images/blogs/win11-guide/day-21-3.png)

(第一次登入，要先建立帳號) 這個帳號資訊 只會落在本機

![Day 21 截圖 4](/images/blogs/win11-guide/day-21-4.png)

**Open WebUI 不會建立任何外部連線，而且您的資料會安全地儲存在您本機伺服器上**

![Day 21 截圖 5](/images/blogs/win11-guide/day-21-5.png)  
登入成功

![Day 21 截圖 6](/images/blogs/win11-guide/day-21-6.png)

我們登入之後的第一件事情就是要先安裝我們的模型

![Day 21 截圖 7](/images/blogs/win11-guide/day-21-7.png)

![Day 21 截圖 8](/images/blogs/win11-guide/day-21-8.png)

![Day 21 截圖 9](/images/blogs/win11-guide/day-21-9.png)

1. [\*\*點選這裡。](https://ollama.com/library)\*\* <https://ollama.com/library> 我們可以在這邊找到 適合我們使用的模型名稱
2. 找到我們要使用的模型 在此輸入名稱 這邊以 “llama3.2:3b” 為範例
3. 點擊下載

下載中

![Day 21 截圖 10](/images/blogs/win11-guide/day-21-10.png)

下載完成後 我們選取下載好的llama3.2

![Day 21 截圖 11](/images/blogs/win11-guide/day-21-11.png)

若有多個模型下載，也可以指定預設要使用的模型

![Day 21 截圖 12](/images/blogs/win11-guide/day-21-12.png)  
最大的好處就是 離線也能運作 (雖然中文支持程度沒有很好)

![Day 21 截圖 13](/images/blogs/win11-guide/day-21-13.png)

## 離線運行的優勢與挑戰

### 優勢

- **隱私保護**：所有的資料與模型均儲存在本地，不會外傳。
- **穩定性**：即便網路中斷，AI 服務依然可以正常運行。

### 挑戰

- **硬體限制**：對硬體效能要求較高，尤其是在執行大型模型時。
- **模型支持度**：中文的支持程度目前較為有限，可能需要進行額外的調整與優化。

---

## 結語

筆者目前使用的 X1 Carbon（2021 年）雖然符合升級至 Windows 11 的最低門檻，但在執行 AI 模型時，受到硬體限制，效能表現並不理想。未來若能升級配備 NPU、GPU 的設備，這些裝置將可能解鎖更多有趣的應用場景。

無論如何，離線使用 AI 模型的嘗試讓我們看到了更多的可能性，也希望未來有更多模型能夠在本地環境中流暢運行。

---

[上一篇：Day 20](/blogs/win11-guide-day-20/)　｜　[下一篇：Day 22](/blogs/win11-guide-day-22/)
