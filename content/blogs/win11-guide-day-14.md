---
title: "Day 14：Windows 11 升級必要條件：Secure Boot"
date: 2024-10-03T09:52:39+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "今天我們來看 Windows 11 的一個重要升級必要條件——「安全開機」（Secure Boot）。 什麼是安全開機？ 安全開機 是一項基本的安全功能，確保電腦在啟動過程中不會被惡意軟體攻擊，避免系"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 14／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

今天我們來看 Windows 11 的一個重要升級必要條件——「安全開機」（Secure Boot）。

### 什麼是安全開機？

- **安全開機** 是一項基本的安全功能，確保電腦在啟動過程中不會被惡意軟體攻擊，避免系統在啟動時遭到損害。
- Windows 11 的設備預設啟用了安全開機。
- 可以按下 `Win + R`，輸入 `msinfo32`，查看安全開機狀態是否顯示為「開啟」。

### 為什麼需要安全開機？

在電腦的啟動過程中，每個基本組件會啟動並進行彼此的通訊。為確保每次啟動都是安全的，安全開機技術經由電腦製造商開發，用於防止惡意軟體在啟動過程中進行攻擊，保護設備免受損壞。

### 從啟動開始保護

PC 的啟動過程對於維持其安全性至關重要。惡意軟體可能在啟動過程中植入，並繞過作業系統的安全措施，導致系統在開機時已經被感染。例如，**Rootkit** 是一種惡意軟體，能夠在系統核心模式下運行，並在作業系統啟動之前隱蔽地操作。

### 安全開機如何工作？

在電腦啟動過程中，**安全開機** 會使用數位簽名來驗證軟體的合法性。它確保只允許受信任的軟體運行，並在執行任何可執行檔案前驗證其數位簽章，以防止軟體被篡改。

### 如何在 Windows 11 上啟用安全開機？

在 Windows 11 的設備上，安全開機通常已預設啟用，這也是升級到 Windows 11 的必要條件之一。若要檢查是否已啟用安全開機：

1. 按下 **Windows + R** 開啟執行對話框。
2. 輸入 `msinfo32`，按下 **Enter**。
3. 檢查「安全開機狀態」是否顯示為「開啟」。

![Day 14 截圖 1](/images/blogs/win11-guide/day-14-1.png)

## https://ithelp.ithome.com.tw/upload/images/20241003/20169610ELh25Smsyb.png

## **開機順序**

1. 開啟電腦後，檢查平臺金鑰簽章。
2. 若韌體不受信任，UEFI 韌體會啟動 OEM 特定的復原程序。
3. 若 Windows 開機管理員無法正常運作，韌體會嘗試啟動備份。若備份也失敗，則會執行 OEM 的補救措施。
4. Windows 開機管理員開始執行後，若驅動程式或核心發生問題，系統會載入 Windows 復原環境（Windows RE）以進行修復。
5. 系統會載入反惡意軟體程式。
6. Windows 會載入其他核心驅動並初始化使用者模式的進程。

---

### **如何進入 BIOS 啟用/停用安全開機 (以 Lenovo ThinkPad 為例)**

1. 按下 **電源按鈕** 開啟電腦，出現 Lenovo Logo 時，快速按 **F1** 進入 BIOS。
2. 使用箭頭鍵導航到 **Security** 選項。
3. 選擇 **Secure Boot** 子選單，按 **Enter**。
4. 按下 **Enter** 啟用或停用 Secure Boot 功能。

(Ref: [Lenovo](https://pcsupport.lenovo.com/tw/zh/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-9th-gen-type-20xw-20xx/20xw/20xw0063tw/pf2yzj3t/solutions/ht509044?Products=LAPTOPS-AND-NETBOOKS/THINKPAD-X-SERIES-LAPTOPS/THINKPAD-X1-CARBON-9TH-GEN-TYPE-20XW-20XX/20XW/20XW0063TW/PF2YZJ3T))

1. 按下**電源**按鈕打開PC。當出現紅色或白色的Lenovo Logo時，快速連按F1直到出現BIOS。

   ![Day 14 截圖 3](/images/blogs/win11-guide/day-14-3.png)
2. 使用鍵盤箭頭鍵到**Security**選項。

   ![Day 14 截圖 4](/images/blogs/win11-guide/day-14-4.png)
3. 使用鍵盤箭頭鍵導航到**Secure Boot**子選單，然後按Enter鍵打開選單。

   ![Day 14 截圖 5](/images/blogs/win11-guide/day-14-5.png)
4. 透過按**安全啟動**選單項上的Enter啟用或停用SecureBoot功能。

---

可以看出，Windows 11 已將安全性作為升級的門檻之一。這是一個很好的機會來檢視當前設備的安全性。安全開機不僅提升了設備的安全防護，也是升級Windows 11系統的一項必要條件。對於那些無法滿足升級條件的舊設備，可能需要考慮硬體更新或替換。

---

[上一篇：Day 13](/blogs/win11-guide-day-13/)　｜　[下一篇：Day 15](/blogs/win11-guide-day-15/)
