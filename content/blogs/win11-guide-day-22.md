---
title: "Day 22：Windows 11 支援直接運行圖形化 Linux 應用程式：WSLg"
date: 2024-10-11T16:07:12+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "自從 Windows 11 推出以來，微軟加強了對開發者的支持，提供了許多新功能，其中之一就是 Windows Subsystem for Linux (WSL) 與其改進版 WSL2。WSL 允許用"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 22／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

自從 Windows 11 推出以來，微軟加強了對開發者的支持，提供了許多新功能，其中之一就是 **Windows Subsystem for Linux (WSL)** 與其改進版 **WSL2**。WSL 允許用戶在 Windows 中運行 Linux 環境，而 WSLg（Windows Subsystem for Linux GUI）則進一步提升，允許用戶直接在 Windows 上運行 Linux 圖形化應用程式，無需額外的虛擬機器配置。這對於開發者來說，是一個非常強大的工具。

## WSL 和 WSL2 是什麼？

**WSL** 是一個使 Windows 使用者可以在 Windows 系統上運行 Linux 二進制執行檔的兼容層。它讓開發者可以在 Windows 上使用熟悉的 Linux 命令列工具與開發環境，而不必切換到另一台設備或安裝虛擬機器。

**WSL2** 是 WSL 的升級版本，使用了真正的 Linux 核心來提供更佳的性能和完整的系統相容性。WSL2 與虛擬機相比，它的啟動速度非常快，佔用的系統資源也比較少，提供了近乎原生 Linux 的體驗。

## WSL 和虛擬機器有什麼不同？

傳統的虛擬機器（例如 VMware 或 VirtualBox）會創建一個獨立的操作系統環境，並且需要大量的系統資源來運行。它們的啟動過程相對較長，而且需要分配專門的 CPU、記憶體等硬體資源。

相比之下，**WSL** 和 **WSL2** 只是將 Linux 環境整合進 Windows，而不是創建一個完全獨立的操作系統，這使得它的性能表現更加輕便。WSL2 雖然也使用虛擬機技術，但它的虛擬機是由微軟高度優化過的，幾乎不會拖慢系統運行。

## 安裝 Ubuntu

要在 Windows 11 中運行 Linux，你可以透過 Windows Terminal 透過 WSL 安裝 Ubuntu。安裝過程非常簡單，僅需以下步驟：

```
wsl --install Ubuntu
```

![Day 22 截圖 1](/images/blogs/win11-guide/day-22-1.png)

## 在 Linux Terminal 中安裝圖形化應用程式

安裝完成後，你可以打開 **Linux 終端機** 並開始安裝你想要的應用程式，例如 LibreOffice 這個常用的辦公軟體：

```
sudo apt-get update
sudo apt-get install libreoffice
```

![Day 22 截圖 2](/images/blogs/win11-guide/day-22-2.png)

## 運行 Linux 圖形化應用程式

安裝完成後，WSLg 會自動將這些 Linux 圖形化應用程式與 Windows 整合。你可以直接從 Windows 開始選單中找到剛剛安裝的 **LibreOffice**，並點擊啟動。

這個功能使得 Windows 開發者和 Linux 用戶能夠更無縫地運行和使用兩個操作系統的應用程式，大幅提升了開發效率和工作流的靈活性。對於那些習慣使用 Linux 圖形化應用程式的開發者，這是一個非常實用的功能，因為它無需進行複雜的虛擬機配置。

![Day 22 截圖 3](/images/blogs/win11-guide/day-22-3.png)

![Day 22 截圖 4](/images/blogs/win11-guide/day-22-4.png)

Ref: <https://learn.microsoft.com/zh-tw/windows/wsl/tutorials/gui-apps>

要使用 WSLg 功能，系統必須是 \*\*`Windows 10 版本 19044 以上** 或 **Windows 11**` 才能存取這項功能。過去我並沒有特別留意這個功能，以往需要 Linux 環境時，總是習慣使用虛擬機器 (VM) 來處理。直到參加這個主題的時候，才發現並探索到這項便捷功能。

這讓我感觸頗深，許多我們平時覺得繁瑣的事情，或許隨著科技的快速發展，已經有了更高效的解決方案，只是我們的學習速度沒有跟上罷了。感覺就像我還在用冷兵器作戰，而外面的世界都已經再使用無人機了。

---

[上一篇：Day 21](/blogs/win11-guide-day-21/)　｜　[下一篇：Day 23](/blogs/win11-guide-day-23/)
