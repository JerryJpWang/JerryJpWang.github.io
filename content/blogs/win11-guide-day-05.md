---
title: "Day 05：Windows 11 升級關鍵：TPM 2.0 的重要性與安全提升"
date: 2024-09-24T17:52:39+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "升級至 Windows 11 的必要條件之一是擁有 TPM 2.0。 什麼是信賴平台模組（TPM）？ TPM（信賴平台模組）用來提升電腦的安全性。像 BitLocker 磁碟機加密 和 Windows"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 05／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

升級至 Windows 11 的必要條件之一是擁有 TPM 2.0。

## 什麼是信賴平台模組（TPM）？

TPM（信賴平台模組）用來提升電腦的安全性。像 [BitLocker 磁碟機加密](https://docs.microsoft.com/windows/security/information-protection/bitlocker/bitlocker-device-encryption-overview-windows-10) 和 [Windows Hello](https://support.microsoft.com/zh-tw/windows/%E8%A8%AD%E5%AE%9A-windows-hello-dae28983-8242-bb2a-d3d1-87c9d265a5f0) 等服務，均利用 TPM 來建立並儲存加密金鑰，並確保作業系統及韌體的完整性，防止被竄改。

一般來說，TPM 是主機板上的獨立晶片，但 TPM 2.0 標準允許製造商（如 Intel 和 AMD）將 TPM 功能直接整合到其晶片組內。

TPM 已使用超過 20 年，自 2005 年起成為電腦的一部分。現行標準是 TPM 2.0，於 2016 年成為新電腦的標配。

## 如何檢查電腦是否支援 TPM 2.0

### 方法 1：使用 Windows 安全性應用程式

1. 在搜索欄中輸入「Windows Security」，打開應用程式。
2. 點擊「Device security」，查看是否有 TPM 相關信息。  
   ![Day 5 截圖 1](/images/blogs/win11-guide/day-05-1.png)

### 方法 2：使用 Microsoft 管理主控台

1. 按 **Win + R**，輸入 `tpm.msc`，按 **Enter**。
2. 在 TPM 管理控制台中查看 TPM 狀態和版本。  
   ![Day 5 截圖 2](/images/blogs/win11-guide/day-05-2.png)

### 方法 3：使用 PC Health Check 工具

下載 [PC Health Check](https://aka.ms/GetPCHealthCheckApp) 工具，檢查電腦是否符合 Windows 11 升級需求。

### 檢查 BIOS 中的 TPM 設定

如果上述方法顯示 TPM 未啟用，可能需要進入 BIOS 來啟用 TPM 功能。根據不同的電腦製造商（如 ASUS、Dell、Lenovo 等），操作步驟可能會有所不同，可參考 [Microsoft 提供的教學](https://support.microsoft.com/zh-tw/windows/%E5%9C%A8%E9%9B%BB%E8%85%A6%E4%B8%8A%E5%95%9F%E7%94%A8-tpm-2-0-1fd5a332-360d-4f46-a1e7-ae6b0c90645c)。

(Levono教學，啟用 Security Chip Enable)  
![Day 5 截圖 3](/images/blogs/win11-guide/day-05-3.png)

## 為什麼要升級到 TPM 2.0？

隨著 Windows 10 在 2025年的10月14日結 EOS 的來臨 (還能透過ESU來保障系統安全)，Windows 11 將 TPM 2.0 作為必要條件，以加強安全性。TPM 2.0 能有效保護數據，防止外部攻擊。對於我們軟體工程師來說，電腦是最重要的工作工具，不支援 TPM 2.0 的設備多半已經過時，是時候考慮升級。

「工欲善其事，必先利其器。」升級至 TPM 2.0 不僅是提高工作效率，更是對數位安全的長期投資。

**Day 5** Always Prepare

隨著 Windows 10 即將步入生命週期終止 (EOS)，是時候提前為未來做好準備與規劃了。Windows 11 不僅僅是一個系統升級，更是一個邁向更高效、更安全工作環境的機會。

---

[上一篇：Day 04](/blogs/win11-guide-day-04/)　｜　[下一篇：Day 06](/blogs/win11-guide-day-06/)
