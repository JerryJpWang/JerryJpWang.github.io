---
title: "Day 12：自主掌控 Windows 11：建立並管理本機帳戶"
date: 2024-10-01T07:55:06+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "如何在 Windows 11 中管理本地帳戶 在這篇文章中，我們將探討如何在 Windows 11 中管理本地帳戶。隨著 Windows 的不斷更新，帳戶管理選項變得更加靈活且便捷。以下示範的是如何在"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 12／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

# 如何在 Windows 11 中管理本地帳戶

在這篇文章中，我們將探討如何在 Windows 11 中管理本地帳戶。隨著 Windows 的不斷更新，帳戶管理選項變得更加靈活且便捷。以下示範的是如何在 Windows 11 (版本 23H2) 中不使用 Microsoft 帳號來創建本地帳戶。

## 使用的版本

- **Windows 版本**: 23H2
- **Windows Feature Experience Pack**: 1000.22700.1041.0

在早期的 Windows 11 版本中，創建本地帳戶需要與 Microsoft 帳號綁定，這對某些使用者而言相當不便。隨著用戶反饋的增多，微軟在最新的更新中增加了不使用 Microsoft 帳號創建本地帳戶的選項。現在，我們可以更靈活地管理帳戶，而不必依賴 Microsoft 帳號。

---

## 如何建立本地帳戶（不需 Microsoft 帳號）

### 步驟一：打開控制面板

1. 進入 **控制面板**，選擇 **User Accounts (使用者帳戶)**。
2. 點擊 **Manage another account (管理其他帳戶)**。

![Day 12 截圖 1](/images/blogs/win11-guide/day-12-1.png)

### 步驟二：選擇新增帳戶

系統會要求你輸入電子郵件或電話號碼，此時選擇 **I don’t have this person’s sign-in information (我沒有此人的登入資訊)**。

![Day 12 截圖 2](/images/blogs/win11-guide/day-12-2.png)

### 步驟三：選擇建立本地帳戶

系統會嘗試幫你建立 Microsoft 帳號，但你可以選擇 **Add a user without a Microsoft account (建立不使用 Microsoft 帳號的使用者)**。

![Day 12 截圖 3](/images/blogs/win11-guide/day-12-3.png)

### 步驟四：設定本地帳戶名稱和密碼

接下來，輸入你希望創建的本地帳戶名稱和密碼。此處帳號為 **UncleJerry**。

![Day 12 截圖 4](/images/blogs/win11-guide/day-12-4.png)

### 步驟五：設置管理權限

創建完帳戶後，你可以選擇將這個帳戶設置為 **Administrator (管理員)** 。

![Day 12 截圖 5](/images/blogs/win11-guide/day-12-5.png)

### 步驟六：使用新帳戶登入

使用剛剛創建的本地帳號 **UncleJerry** 登入後，你就可以成功管理這台電腦了。

## https://ithelp.ithome.com.tw/upload/images/20241001/20169610WAsNPC0ZHZ.png

## 本地帳戶與 Microsoft 帳號的差異

### 優勢

1. **隱私保護**：本地帳戶無需將個人資料如電子郵件、聯絡資訊等與 Microsoft 服務綁定，提升使用者的隱私。
2. **離線操作**：不需要連接網路即可使用，特別適合那些不依賴雲端服務或不希望與雲端進行過多交互的使用者。
3. **靈活性**：不受 Microsoft 帳號的限制，能更加靈活地控制和管理電腦。

### 劣勢

1. **同步功能缺失**：Microsoft 帳號能夠將偏好、設定和檔案同步到多台裝置，使用本地帳戶無法使用此功能。
2. **無法訪問 Microsoft 服務**：需要訪問 Microsoft Store、OneDrive 等服務時，仍需登入 Microsoft 帳號。
3. **密碼恢復不便**：若忘記本地帳戶密碼，恢復過程比使用 Microsoft 帳號來得複雜。

---

## 如何有效管理本地帳戶

使用本地帳戶，你可以更靈活地管理自己的系統，且不受限於 Microsoft 生態系統。例如，許多系統任務（如排程任務管理）可專門使用不同的本地帳戶進行管理，以提高安全性和穩定性。在企業環境中，這樣的設置有助於不同團隊依照不同權限分工合作。下面我們以 **UncleJerry** 帳號為例，設置該帳號專門用來管理排程任務：

1. **創建帳號**：如上文所述，創建不使用 Microsoft 帳號的本地帳戶。
2. **分配權限**：將該帳號設定為 **Administrator (管理員)**，以允許完全控制排程任務的操作。
3. **執行任務**：登入 **UncleJerry** 帳號，設置排程任務，確保日常管理和操作不會受到其他帳戶干擾。

![Day 12 截圖 7](/images/blogs/win11-guide/day-12-7.png)

---

透過本地帳戶，我們可以更加自主地管理 Windows 11 系統，不必綁定Microsoft帳號。

---

[上一篇：Day 11](/blogs/win11-guide-day-11/)　｜　[下一篇：Day 13](/blogs/win11-guide-day-13/)
