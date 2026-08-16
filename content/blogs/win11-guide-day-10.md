---
title: "Day 10：Windows 11：如何刪除 Dev Drive 並釋放磁碟空間"
date: 2024-09-29T18:09:15+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "在體驗 Dev Home 的功能時，曾建立了一個開發者磁碟機。經過體驗後，決定不再使用 Dev Home 相關功能來管理專案與日常開發作業。 本篇文章將引導你如何刪除先前建立的開發者磁碟機並釋放出磁碟"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 10／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

在體驗 **Dev Home** 的功能時，曾建立了一個開發者磁碟機。經過體驗後，決定不再使用 Dev Home 相關功能來管理專案與日常開發作業。

本篇文章將引導你如何刪除先前建立的開發者磁碟機並釋放出磁碟空間。

---

Ref: (learn.microsoft.com) [Dev Derive](https://learn.microsoft.com/zh-tw/windows/dev-drive/)

### 什麼是開發人員磁碟機？

> 開發人員磁碟機是一種新型儲存體磁碟區，旨在提升主要開發工作負載的效能。

開發人員磁碟機是基於 [ReFS](https://learn.microsoft.com/zh-tw/windows-server/storage/refs/refs-overview) 技術打造，並針對目標檔案系統進行效能優化。它提供了更高的儲存體控制和安全性選項，包含信任指定、防毒設定、及管理控制篩選等功能。

更多有關開發人員磁碟機的效能改善，可參考這篇部落格文章：[在 Visual Studio 中獲得效能改善的開發人員磁碟機和開發人員方塊](https://aka.ms/vsdevdrive)。

### **必要條件:**

- Windows 11 組建 #10.0.22621.2338 或更新版本 (檢查 Windows 更新)
- 建議 16gb 記憶體 (至少 8gb)
- 最小 50gb 可用磁碟空間
- 所有 Windows SKU 版本都提供開發人員磁碟機。
- 本機系統管理員權限。

### 開發人員磁碟機有什麼好處？

Ref: <https://devblogs.microsoft.com/visualstudio/devdrive/>

![Day 10 截圖 1](/images/blogs/win11-guide/day-10-1.png)

---

### 什麼樣的檔案適合存放在開發人員磁碟機？

開發人員磁碟機適用於：

1. 原始程式碼存放庫和專案檔
2. 封裝快取
3. 建置輸出和中繼檔案

(體驗期間用來存放專案檔, 原始碼)

![Day 10 截圖 2](/images/blogs/win11-guide/day-10-2.png)

---

## **如何刪除開發人員磁碟機 [Dev Drive](https://learn.microsoft.com/zh-tw/windows/dev-drive/)**

您可以在 Windows 11 的系統設定中刪除開發人員磁碟機。步驟如下：

1. 開啟 **設定** > **儲存體** > **磁碟與磁碟區**。
2. 選擇 **進階儲存體設定**，並找到已建立的 Dev Drive (D:)。
3. 按下 **屬性**，然後在 **格式** 標籤下選擇 **刪除**。

### 步驟 1: `System` > `Storage` > `Disks & volumes`

找到先前建立的 **Dev Drive (D:)**，名稱可能會與你的系統不同，需對應你當初設定的名稱與代號。

![Day 10 截圖 3](/images/blogs/win11-guide/day-10-3.png)

### 步驟 2: 點擊 **Properties**，進入 **Dev Drive (D:)** 屬性，然後點擊 **Format**，選擇 "Delete"

![Day 10 截圖 4](/images/blogs/win11-guide/day-10-4.png)

### 提醒

在刪除開發人員磁碟機前，請先備份裡面的資料，避免資料遺失。

![Day 10 截圖 5](/images/blogs/win11-guide/day-10-5.png)

---

## **中斷虛擬磁碟機連線並刪除 VHDX 檔案**

接下來，我們需要中斷虛擬磁碟機與系統的連接，並刪除對應的 VHD 檔案。

1. 開啟 **Computer Management** > **磁碟管理**。
2. 找到對應的開發磁碟機，點擊滑鼠右鍵，選擇 **中斷連結 VHD**。  
   ![Day 10 截圖 6](/images/blogs/win11-guide/day-10-6.png)
3. 刪除 DevDrives 對應使用的 VHDX檔案。  
   ![Day 10 截圖 7](/images/blogs/win11-guide/day-10-7.png)

---

### **結語**

完成以上步驟後，開發人員磁碟機 (Dev Drive) 及其對應的 VHDX 檔案將從系統中移除，釋放出原本使用的空間。

"Dev Drive"筆者測試起來沒有感覺到吸引使用的動力，很難說服團隊統一採用Dev drive的方式作為管理開發環境的方式。  
(統一的開發環境有助於團隊成員間的相互協助)

技術導入是為了解決問題，而非製造新的問題。選擇能為團隊帶來實質價值的技術，才能讓團隊更上一層樓。

---

[上一篇：Day 09](/blogs/win11-guide-day-09/)　｜　[下一篇：Day 11](/blogs/win11-guide-day-11/)
