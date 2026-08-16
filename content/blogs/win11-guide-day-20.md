---
title: "Day 20：探索 Windows 11 23H2：兼容性與日常開發工具的測試"
date: 2024-10-09T12:20:59+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "作為一名開發人員，筆者的日常工作涉及 .NET C、Vue.js 以及一些測試工具。筆者最近升級至 Windows 11 23H2，並針對日常使用的開發工具進行了兼容性測試。在這篇文章中，我將分享測試"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 20／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

作為一名開發人員，筆者的日常工作涉及 **.NET C#**、**Vue.js** 以及一些測試工具。筆者最近升級至 **Windows 11 23H2**，並針對日常使用的開發工具進行了兼容性測試。在這篇文章中，我將分享測試結果與系統體驗。

## 兼容性測試：日常開發工具是否順利運行？

升級至新系統時，對於開發者而言，**兼容性** 是最重要的考量因素之一。以下是筆者在 **Windows 11 23H2** 上測試的開發工具及其運行情況。

### 1. 常用開發工具測試結果

- **Visual Studio 2022 / VS Code**：兩者都能順利進行開發和編譯，無任何運行問題。
- **Docker Desktop**：筆者測試了使用 Docker 運行的 **OWASP Juice Shop**，應用順利運行，並能在本地環境打開
- **Oracle VM VirtualBox**：虛擬機順利運行。筆者使用虛擬機測試了 **Kali Linux**，系統無明顯延遲或兼容性問題。

(Docker 順利運行)  
![Day 20 截圖 1](/images/blogs/win11-guide/day-20-1.png)

### 2. 測試工具

- **Kali Linux**：在虛擬機中運行時，各類滲透測試工具運行良好，並無兼容性問題。
- **ZAP (Zed Attack Proxy)**：在 **Windows 11 23H2** 上能正常運行，所有功能均能順利使用。

### 3. 生產力工具測試結果

除了開發工具，筆者還測試了一些日常使用的生產力工具，結果如下：

| 軟體名稱 | 測試結果 |
| --- | --- |
| **Logitech Options** | 正確運行 |
| **PicPick** | 正確運行 |
| **ZAP** | 正確運行 |
| **Notion** | 正確運行 |
| **Visual Studio 2022** | 正確運行 |
| **VS Code** | 正確運行 |
| **Docker Desktop** | 正確運行 |
| **Notepad++** | 正確運行 |
| **Spotify** | 正確運行 |
| **Fork** | 正確運行 |
| **OneDrive** | 正確運行 |
| **OneNote** | 正確運行 |
| **Google Drive** | 正確運行 |
| **Oracle VM VirtualBox** | 正確運行 |
| **Chocolatey** | 正確運行 |
| **Firefox** | 正確運行 |

根據以上測試結果，筆者所常用的工具在 **Windows 11 23H2** 上均能正常運行，且未發現重大兼容性問題。因此，在升級至新系統後，我的工作流程並未受到影響，開發效率得以保持。

## 最後的建議

升級到 **Windows 11 23H2** 是值得的，特別是對於開發者而言，像是先前有提到的截圖工具可以方便我們做OCR圖片轉文字，還強化了安全性。在享受新系統帶來的便利之前，筆者建議先進行工具的兼容性測試，確保所有工具正常運行後再全面升級。

若有任何兼容性問題或疑慮，可以參考 [微軟官方的 Windows 11 23H2 已知問題與通知](https://learn.microsoft.com/zh-tw/windows/release-health/status-windows-11-23h2)，了解相關的修正與排除方案。

---

[上一篇：Day 19](/blogs/win11-guide-day-19/)　｜　[下一篇：Day 21](/blogs/win11-guide-day-21/)
