---
title: "Day 11：Windows 11 備份介面設計與策略規劃"
date: 2024-09-30T14:28:37+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "在這篇文章中，將探索 Windows 11 的備份功能，以及如何規劃有效的備份策略。 備份策略規劃 我們可以從兩個層面來規劃備份策略： 1. 系統層面：System Restore 和 Restore"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 11／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

在這篇文章中，將探索 Windows 11 的備份功能，以及如何規劃有效的備份策略。

---

### 備份策略規劃

我們可以從兩個層面來規劃備份策略：

1. **系統層面：System Restore 和 Restore Point**
   - **設定還原點**：在進行驅動更新或 Windows 較大的版本更新前，可以利用這個功能來設定還原點。
   - **系統還原**：若遇到系統更新後出現問題，可以透過此功能來還原系統。
2. **資料層面：Windows Backup**
   - **OneDrive 資料備份**：
     - **雲端同步與資料備份**：OneDrive 提供雲端同步與資料備份，強調跨裝置存取和團隊合作。
   - **應用程式與偏好設定備份**：
     - **Remember my apps**：備份應用程式列表，確保在重新安裝或更換設備時，可以快速恢復所有已安裝的應用程式。
     - **Remember my preferences**：備份系統偏好設定，包括桌面佈局、語言設定、顯示設定等，讓你在重置系統或更換設備後，能夠快速恢復到熟悉的使用環境。

---

### Windows Backup 設定

可以透過以下路徑進行 Windows Backup 設定：

**Settings > Accounts > Windows backup**  
![Day 11 截圖 1](/images/blogs/win11-guide/day-11-1.png)

**管理 OneDrive 備份項目**  
![Day 11 截圖 2](/images/blogs/win11-guide/day-11-2.png)

---

### System Restore 設定

**System Restore** 是一個強調系統穩定性的回溯工具，適合快速解決系統問題。

可以透過以下路徑進行 System Restore 設定：

**開始選單 > Create a restore point**  
![Day 11 截圖 3](/images/blogs/win11-guide/day-11-3.png)

**Create a restore point**  
![Day 11 截圖 4](/images/blogs/win11-guide/day-11-4.png)

**System Restore**  
![Day 11 截圖 5](/images/blogs/win11-guide/day-11-5.png)

---

### 備份策略建議

1. **個人資料備份（使用 OneDrive）**：
   - 建議將重要的個人檔案（如桌面、文件、圖片等）設定為透過 OneDrive 自動同步至雲端，這樣你可以隨時存取，並減少因設備損壞或遺失造成的風險。
2. **應用程式列表與偏好設定備份**：
   - **Remember my apps**：定期啟用 Windows 備份來保存應用程式列表，這樣如果需要重置系統或更換設備，可以快速恢復所有已安裝的應用程式，節省重新下載和安裝的時間。
   - **Remember my preferences**：備份系統偏好設定，包括桌面佈局、語言設定、顯示設定等，讓你在重置系統或更換設備後，能夠快速恢復到熟悉的使用環境，提升使用體驗。

要避免檔案遺失、提升工作效率？將檔案備份到 OneDrive 是個明智的選擇。它不僅能保障資料安全，還能讓協作變得更簡單，是我工作中不可或缺的工具

---

[上一篇：Day 10](/blogs/win11-guide-day-10/)　｜　[下一篇：Day 12](/blogs/win11-guide-day-12/)
