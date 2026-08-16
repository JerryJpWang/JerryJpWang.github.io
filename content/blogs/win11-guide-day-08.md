---
title: "Day 08：Windows 11 右鍵選單變更教學：輕鬆恢復傳統選單，提升操作效率"
date: 2024-09-27T08:20:00+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "升級到 Windows 11 後，某些改變可能會讓人感到不便，其中之一便是 右鍵選單 的使用方式有所變化。以前我們常用的選項，例如使用壓縮軟體 7Zip 的功能，現在需要多點幾下才能看到熟悉的選項。 "
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 08／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

升級到 Windows 11 後，某些改變可能會讓人感到不便，其中之一便是 **右鍵選單** 的使用方式有所變化。以前我們常用的選項，例如使用壓縮軟體 7-Zip 的功能，現在需要多點幾下才能看到熟悉的選項。

## 1. 不便之處：右鍵選單選項不見了

當我在 Windows 11 中想要解壓縮檔案，按下右鍵後，發現熟悉的選項不見了。

![Day 8 截圖 1](/images/blogs/win11-guide/day-08-1.png)

別擔心，這時只需要點選 **Show more options。** (或者 按 shift + 滑鼠右鍵 開啟選單 )

就能看到我們熟悉的傳統選單。

雖然這樣可以解決問題，但每次都需要點兩次滑鼠才能看到選項，實在讓人不太方便。那麼，有沒有辦法恢復 Windows 10 的傳統右鍵選單呢？

![Day 8 截圖 2](/images/blogs/win11-guide/day-08-2.png)

## 2. 解決方案：修改註冊表恢復傳統右鍵選單

可以透過修改註冊表來一勞永逸地恢復傳統的右鍵選單。下面介紹具體操作步驟。

### 步驟 1：開啟註冊表編輯器

按下 **Win + R** 快捷鍵，輸入 **regedit**，並按下 Enter 以開啟註冊表編輯器。

![Day 8 截圖 3](/images/blogs/win11-guide/day-08-3.png)

### 步驟 2：導航到 CLSID 路徑

在註冊表編輯器中，導航到以下路徑：

```
Computer\HKEY_CURRENT_USER\Software\Classes\CLSID
```

### 步驟 3：新增 CLSID 鍵值

在 **CLSID** 路徑下，右鍵選擇新增一個新的 **Key**，並將其命名為： `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`

![Day 8 截圖 4](/images/blogs/win11-guide/day-08-4.png)

接著，在該鍵下再新增一個名為 **InprocServer32** 的子鍵，並修改它的值為”空“ （原本是 value not set）。

![Day 8 截圖 5](/images/blogs/win11-guide/day-08-5.png)

(確認 **InprocServer32** 的值修改為”空”)

![Day 8 截圖 6](/images/blogs/win11-guide/day-08-6.png)

### 步驟 4：重啟檔案總管 Windows Explorer

完成以上步驟後開啟Task Manager，重啟檔案總管 Windows Explorer。你會發現右鍵選單已經恢復到 Windows 10 的傳統樣式了！

![Day 8 截圖 7](/images/blogs/win11-guide/day-08-7.png)

---

### 使用CMD方式實現 (需要透過Administrator權限執行)

除了手動修改註冊表，還可以透過命令行快速新增或刪除註冊表 Key：

### 步驟 1： 恢復 Windows 10 傳統右鍵選單的命令：

```
reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

這條命令將在指定的 CLSID 目錄下新增 `InprocServer32` 子鍵並清空其值，達到恢復傳統右鍵選單的效果。  
(記得要重啟檔案總管 Windows Explorer)

### 步驟 2： 恢復 Windows 11 新右鍵選單的命令：

```
reg delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f
```

此命令將刪除剛剛添加的 `InprocServer32` 子鍵，並恢復到 Windows 11 的新右鍵選單。

---

### 命令參數解釋：

1. **`reg add`**
   - 用於在註冊表中新增或修改鍵和值。
2. **`reg delete`**
   - 用於刪除指定的註冊表鍵或值。
3. **`/f`**
   - 強制執行命令，無需確認。
4. **`/ve`**
   - 表示不為該鍵設置具體值，相當於清空。

REF: [(learn.microsoft.com) reg add](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-add)

---

### 無論是使用手動方式還是命令行方式，你都可以輕鬆切換 Windows 11 的右鍵選單樣式。如果你對新**選單**不適應，可以透過上述步驟找回熟悉的操作體驗。如果後續希望恢復新的設計，亦可通過命令或手動刪除註冊表 Key 來實現。

### 建議

- 如果你**經常使用右鍵選單**且偏好傳統選單，可以考慮**修改註冊表**，以便每次右鍵都預設顯示傳統選單，這樣更符合你的操作習慣。
- 如果你**偶爾需要傳統選單**，或不想進行系統更改，使用**Shift + 右鍵**會更方便，無需進行任何設置。

改變是成長的開始，讓我們一起擁抱Windows 11吧！

---

[上一篇：Day 07](/blogs/win11-guide-day-07/)　｜　[下一篇：Day 09](/blogs/win11-guide-day-09/)
