---
title: "Day 07：掌握 Windows 11 的復原策略：延長猶豫期，保護你的選擇"
date: 2024-09-26T11:57:48+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "如果不喜歡 Windows 11，我可以在升級後移回 Windows 10 嗎？ 是的，升級至 Windows 11 之後，您還有 “10 天”可以移回 Windows 10，同時保留您一起帶的檔案和"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 07／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

### 如果不喜歡 Windows 11，我可以在升級後移回 Windows 10 嗎？

> 是的，升級至 Windows 11 之後，您還有 “10 天”可以移回 Windows 10，同時保留您一起帶的檔案和資料。 在該 10 天的期間後，您必須備份資料，然後執行「全新安裝」才能回復到 Windows 10。

REF: [https://support.microsoft.com/zh-tw/windows/升級到-windows-11-常見問題集-fb6206a2-1a0f-448a-80f1-8668ee5b2bf9](https://support.microsoft.com/zh-tw/windows/%E5%8D%87%E7%B4%9A%E5%88%B0-windows-11-%E5%B8%B8%E8%A6%8B%E5%95%8F%E9%A1%8C%E9%9B%86-fb6206a2-1a0f-448a-80f1-8668ee5b2bf9)

![Day 7 截圖 1](/images/blogs/win11-guide/day-07-1.png)

---

當升級到 Windows 11 Pro 後，許多用戶會發現系統磁碟（通常是 **C:**）中多了一個名為 **C:\Windows.old** 的資料夾。這個資料夾具有特定用途，請勿隨意刪除。本文將詳細說明該資料夾的功能、如何安全地處理它，以及其他常見問題。

![Day 7 截圖 2](/images/blogs/win11-guide/day-07-2.png)

---

### 什麼是 **Windows.old** 資料夾？

當你從 Windows 10 升級到 Windows 11 後，系統會自動生成一個 **Windows.old** 資料夾。這個資料夾的主要功能如下：

1. **復原到舊系統**：如果升級後遇到問題，或不喜歡新系統，你可以在升級後的 10 天內利用此資料夾復原至 Windows 10。
2. **保留舊系統檔案**：它會暫時保存舊系統中的使用者設定、應用程式和驅動程式，避免升級過程中遺失重要資料。
3. **系統備份**：這個資料夾就像是升級前的系統備份，用於回復舊系統檔案。

---

### 注意事項

- **C:\Windows.old** 資料夾可能佔用大量磁碟空間(筆者這次升級案例佔用約 44 GB。)
- Windows 系統會自動在 10 天(預設值)後刪除這個資料夾來釋放空間。如果確認不再需要復原到舊系統，可以選擇手動刪除。

---

## 如何查看升級到 Windows 11 的日期？

若你想確認系統的升級日期，可以使用以下指令：  
(CMD)

```
systeminfo | find /i "original install date"
```

此指令會顯示系統的「原始安裝日期」，即升級到 Windows 11 的日期。  
![Day 7 截圖 3](/images/blogs/win11-guide/day-07-3.png)

---

## 如何延長復原期限？

Windows 預設復原至舊系統的期限是 10 天，但你可以使用指令來延長這個期限（例如設置為 30 天或 60 天）。**請注意，延長復原期限的操作必須在升級的 10 天復原期限內完成。若復原期限已過，將無法再延長**。以下是具體操作方法。

### 查詢當前復原期限

首先，你可以使用以下指令查詢目前的復原期限：  
(CMD)

```
DISM /Online /Get-OSUninstallWindow
```

此指令會顯示系統升級後可復原至 Windows 10 的剩餘天數。

### 設定復原期限

若想延長復原期限，可以使用以下指令：  
(CMD)

```
DISM /Online /Set-OSUninstallWindow /Value:<days>
```

將 `<days>` 替換為你想設置的天數，例如 30 天或 60 天。  
如果您指定的值小於 2 或大於 60，則系統會使用預設值 10。

---

### 實際範例

1. 升級到Window11後，復原期限為 10 天，首先通過以下指令查詢：  
   ![Day 7 截圖 4](/images/blogs/win11-guide/day-07-4.png)
2. 若確認需要將期限延長至 60 天，可以使用以下指令進行設置，但**此操作必須在 10 天的復原期限內進行**：  
   ![Day 7 截圖 5](/images/blogs/win11-guide/day-07-5.png)
3. 完成設定後，可以再次使用查詢指令來驗證更改是否生效：  
   ![Day 7 截圖 6](/images/blogs/win11-guide/day-07-6.png)

---

**請務必記住，延長復原期限的操作必須在升級到Windows 11的 10 天復原期限內完成，否則將無法延長**。希望這些資訊能幫助你順利管理升級過程中的一些常見挑戰。

勇敢地踏出第一步，智慧地規劃每一步。

---

[上一篇：Day 06](/blogs/win11-guide-day-06/)　｜　[下一篇：Day 08](/blogs/win11-guide-day-08/)
