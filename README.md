<!--
  README.md for the Video Game Sales Analysis Project
  --------------------------------------------------
  This repository contains code and data for analyzing video game sales from 1980 to 2018.
-->

# 🎮📊 Video Game Sales Analysis & Sorting Algorithms Comparison

This project performs a comprehensive exploration of the video game market from 1980 to 2018 and compares the performance of two fundamental sorting algorithms—**Insertion Sort** and **QuickSort**—on sales data.
---

## 🚀 Introduction

The global video game industry has evolved dramatically since the 1980s. This project analyzes sales data from 1980 through 2018 to uncover:

- Top-selling platforms and genres  
- Regional market differences (NA, EU, JP, Other)  
- Sales trends over time  
- Correlations between critic/user ratings and sales  

---
## 🚀 Project Goals

- Analyze global video game sales trends over four decades.
- Compare two core sorting algorithms—**Insertion Sort** and **QuickSort**—using real-world data.
- Measure and visualize performance differences in terms of execution time and efficiency.

---
## 📊 Dataset

- **Source**: Cleaned sales dataset covering video games released from 1980 to 2018.
- **Fields**: `Name`, `Platform`, `Year`, `Genre`, `Publisher`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`, `Critic_Score`, `User_Score`
> 💾 **Size**: ~16,598 records

---

## 📖 Sorting Algorithms: Concept & Benefits

### 🧮 Insertion Sort

- **Concept**: Builds the sorted array one element at a time by comparing and inserting each new element into its proper position.
- **Time Complexity**:  
  - Best Case: O(n) (nearly sorted data)  
  - Average/Worst Case: O(n²)
- **Advantages**:
  - Simple and easy to implement
  - Efficient for small or nearly sorted datasets
  - Stable (preserves input order for equal keys)

### ⚡ QuickSort

- **Concept**: Divide-and-conquer algorithm that selects a 'pivot' element and partitions the array into subarrays that are recursively sorted.
- **Time Complexity**:  
  - Best/Average Case: O(n log n)  
  - Worst Case: O(n²) (rare, can be optimized with pivot strategy)
- **Advantages**:
  - Much faster on large datasets
  - In-place (low memory usage)
  - Widely used in production systems

### 🔁 Comparison Focus

We will compare these two algorithms by:

- Running them on varying dataset sizes from the sales data
- Recording execution time and step count
- Analyzing performance for best, average, and worst-case inputs


| Dataset Size | Insertion Sort Time | QuickSort Time |
| ------------ | ------------------- | -------------- |
| 100          | 0.012 sec           | 0.004 sec      |
| 1,000        | 1.31 sec            | 0.05 sec       |
| 10,000       | >10 sec             | 0.22 sec       |

---


<div align="center">
  ⚔️ Insertion Sort vs QuickSort – Who wins on the leaderboard? 🎮📊
</div>
