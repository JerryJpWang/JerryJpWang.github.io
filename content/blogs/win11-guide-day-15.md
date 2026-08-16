---
title: "Day 15：Windows 11 啟用核心隔離與記憶體完整性"
date: 2024-10-04T10:36:04+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "在升級到 Windows 11 後，進入 Windows 安全性，可能會看到一項「黃燈」警告。 從 Windows 11 22H2 開始，當記憶體完整性關閉時，Windows 安全性 會顯示警告。這個"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 15／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

在升級到 Windows 11 後，進入 **Windows 安全性**，可能會看到一項「黃燈」警告。

從 Windows 11 22H2 開始，當記憶體完整性關閉時，**Windows 安全性** 會顯示警告。這個警告會在 Windows 任務列及通知中心的 Windows 安全性圖示上顯示，用戶可以手動在 **Windows 安全性** 中關閉該警告。

![Day 15 截圖 1](/images/blogs/win11-guide/day-15-1.png)

---

**核心隔離** 和 **記憶體完整性** 是 Windows 11 中的重要安全功能，利用虛擬化技術來隔離關鍵系統程序，增強系統的安全性。啟用這些功能有助於防範高風險攻擊

## 啟用核心隔離：常見問題

### 1. 啟用核心隔離會對系統性能產生什麼影響？

- **效能影響**：雖然大多數現代電腦能夠應對該功能的需求，但在較舊的設備上，可能會稍微影響系統效能。

### 2. 記憶體完整性與核心隔離有什麼關係？

- **記憶體完整性** 是核心隔離的一部分，用來防止惡意程式碼注入記憶體中的高安全性程序。

### 3. 如何確認我的電腦是否支持核心隔離？

- 在 **裝置安全性** 中，確認是否可以啟用 **核心隔離** 與 **記憶體完整性**。

---

## Memory Integrity：核心隔離的重要組成

**Memory Integrity** 是 Windows 安全功能的一部分，用來保護系統免受惡意軟體的攻擊，尤其是針對驅動程式和記憶體。這是 **核心隔離** 技術的一部分，利用虛擬化來分離和保護敏感的系統部分。

### 建議開啟的原因：

1. **增強安全性**：防止惡意軟體注入，特別是針對內核層級的攻擊。
2. **防止驅動程式篡改**：阻止未簽署或不安全的驅動程式運行。
3. **虛擬化隔離**：提高 Windows 的安全性。

### 開啟後的潛在影響：

1. **效能影響**：可能會稍微影響效能，尤其是在較舊的設備上。
2. **驅動程式相容性問題**：某些老舊驅動可能會因為不符合安全標準而無法運行。
3. **硬體需求**：需要支援虛擬化技術的硬體（如 Intel VT-x 或 AMD-V）。

---

(以Lenovo 更新為範例)

![Day 15 截圖 2](/images/blogs/win11-guide/day-15-2.png)

### 建議：

- **如果硬體較新** 且驅動程式符合最新要求，建議開啟以增強安全性。

## 啟用 Core Isolation 的步驟

1. 打開 Windows Security 應用程式。
2. 點擊 Device security。
3. 在 Core isolation 部分，啟用 Memory integrity。
4. 重新啟動電腦。

![Day 15 截圖 3](/images/blogs/win11-guide/day-15-3.png)

完成這些步驟後，看到安全性指示變為綠燈，表示 **Core Isolation** 已成功啟用。

![Day 15 截圖 4](/images/blogs/win11-guide/day-15-4.png)

---

![Day 15 截圖 5](/images/blogs/win11-guide/day-15-5.png)

開啟後，實際體驗起來，日常作業使用的工具Visual Studio 2022, Visual Studio Code 沒有感到效能影響。

日常生活中，我們經常需要在不同的選擇間取得平衡，無論是效能與安全，還是其他選擇。但當牽涉到系統保護時，安全應該永遠放在首位。

---

[上一篇：Day 14](/blogs/win11-guide-day-14/)　｜　[下一篇：Day 16](/blogs/win11-guide-day-16/)
