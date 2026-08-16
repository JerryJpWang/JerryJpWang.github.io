---
title: "Day 06：提升開發效率：善用 Windows 11 的 Snipping Tool 及 Text Action 功能"
date: 2024-09-25T16:07:48+08:00
draft: false
author: "Jerry"
tags:
  - Windows 11
  - iThome鐵人賽
  - 生產力
description: "在開發團隊中，我們經常需要用截圖來溝通結果或記錄資料。然而，截圖只能提供視覺資訊，當我們需要使用圖片中的內容來進行進一步操作時，常常遇到一個問題：如何將圖片中的文字快速轉換成可編輯的格式？ 今天，我們"
toc: true
---

> 本文為「Windows 11 Pro 升級指南：從軟體開發工程師視角探索生產力極限」系列文章 Day 06／30，原文發表於 [第 16 屆 iThome 鐵人賽](https://ithelp.ithome.com.tw/users/20169610/ironman/8103)。

在開發團隊中，我們經常需要用截圖來溝通結果或記錄資料。然而，截圖只能提供視覺資訊，當我們需要使用圖片中的內容來進行進一步操作時，常常遇到一個問題：**如何將圖片中的文字快速轉換成可編輯的格式？**

今天，我們來看看如何使用 Windows 11 的內建截圖工具 **Snipping Tool** 和它的 Text Action 功能來解決這個問題，提升開發過程中的工作效率。

---

## 1. 團隊合作中的常見問題

在開發中，像 SQL 語法這樣的重要資訊，通常需要被共享和記錄。我們時常收到來自同事或筆記中的截圖，這些截圖裡包含查詢語法或結果資料。如果我們只收到一張圖片，可能會遇到這樣的情況：  
![Day 6 截圖 1](/images/blogs/win11-guide/day-06-1.png)

- **無法直接複製圖片中的文字**，必須手動重新輸入，浪費時間且容易出錯。
- 當需要進行後續分析或修改時，**圖片格式限制了可操作性**。

這些問題，透過 Snipping Tool 的 Text Action 功能可以有效解決。

---

## 2. 如何使用 Snipping Tool 的 Text Action 功能

### 步驟 1: 截取圖片

按下 **Win + Shift + S**，使用 Snipping Tool 截取你需要的畫面。這個功能能快速選取螢幕中的任意區域。  
![Day 6 截圖 2](/images/blogs/win11-guide/day-06-2.png)

### 步驟 2: 使用 Text Action 功能

截圖後，打開 Snipping Tool，點擊 **Text Action**，此時工具會自動將圖片中的內容轉換為可編輯的文字。

### 步驟 3: 複製文字

點擊 **Copy all text**，即可將圖片中的所有文字複製到剪貼簿，方便接下來的操作。

![Day 6 截圖 3](/images/blogs/win11-guide/day-06-3.png)

### 範例：擷取 SQL 語法

以下是一個範例，我們透過 Snipping Tool 擷取了一段 SQL 語法，並轉換為文字格式：

```
SELECT TOP 20 DatabaseName = DB_NAME(CONVERT (INT, epa. value) ),
[Execution count] = qs.execution_count,
[CpuPerExecution] = total_worker_time / qs.execution_count,
[TotalCPU] = total_worker_time,
[IOPerExecution] = (total_logical_reads + total_logical_writes) / qs.execution_count,
[TotalIO] = (total_logical_reads + total_logical_writes),
[AverageElapsedTime] = total_elapsed_time / qs.execution_count,
[AverageTimeBlocked] = (total_elapsed_time - total_worker_time) / qs.execution_count,
[AverageRowsReturned] = total_rows / qs.execution_count,
[Query Text] = SUBSTRING(qt. TEXT, qs. statement_start_offset / 2 + 1, (
CASE
WHEN qs.statement_end_offset = - 1
THEN LEN(CONVERT (NVARCHAR(max), qt. TEXT)) * 2
ELSE qs.statement_end_offset
END - qs.statement_start_offset
)/2),
[Parent Query] = qt. TEXT,
[Execution Plan] = p.query_plan,
[Creation Time] = qs.creation_time,
[Last Execution Time] = qs.last_execution_time
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) AS qt
OUTER APPLY sys.dm_exec_query_plan(qs.plan_handle) p
OUTER APPLY sys.dm_exec_plan_attributes(plan_handle) AS epa
WHERE epa.attribute = 'dbid'
AND epa.value = db_id()
ORDER BY [AverageElapsedTime] DESC ;-- Other column aliases can be used -- Finding the most expensive statements in your database
```

---

## 3. 測試與排版

### 測試 SQL 語法

我們將上面的 SQL 語法放到 **SQL Server Management Studio (SSMS)** 中執行，結果顯示正確執行，語法沒有錯誤。  
![Day 6 截圖 4](/images/blogs/win11-guide/day-06-4.png)

### 排版問題

從圖片擷取的文字，可能在排版上有些微問題，例如縮排不一致。雖然這不會影響執行，但為了確保可讀性，我們可以使用排版工具如 **Beyond Compare** 來對比原始的 SQL 語法和擷取的文字。

![Day 6 截圖 5](/images/blogs/win11-guide/day-06-5.png)

如上圖，左側是原始的 SQL 語法，右側是通過 Snipping Tool 擷取的結果。除了些微的排版問題外，擷取內容基本無誤。

## 4. 小結

Snipping Tool 的 **Text Action** 是一個方便且實用的工具，特別是在開發過程中能節省大量時間。不僅如此，它還能提高我們在團隊協作中的工作效率，讓我們能夠快速從圖片中取得需要的文字資訊，避免手動重新輸入的麻煩。

「Text Action」功能，本質上就是一種 OCR，不是新技術，但將其整合到 Windows 11 的內建截圖工具中，讓使用者可以更輕鬆地處理日常工作，大幅提升生產力。如果你經常需要處理截圖中的文字內容，不妨試試這個功能！

"你的一個小動作，小小的貼心，可能會為團隊帶來巨大的改變。"

---

[上一篇：Day 05](/blogs/win11-guide-day-05/)　｜　[下一篇：Day 07](/blogs/win11-guide-day-07/)
