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

- **Approach**: Starts with the first element of the array and inserts each new element into its correct position within the already‐sorted left side.
- **Ideal Use**: Best for **small** datasets or **nearly sorted** data.
- **Time Complexity**:  
  - **Best Case**: O(n) – when the array is already sorted  
  - **Average/Worst Case**: O(n²)
- **Benefits**:
  - Very simple to implement  
  - Stable (preserves the order of equal elements)  
  - Low overhead for tiny or almost‐sorted inputs

### ⚡ QuickSort
- **Approach**: Uses a **pivot** element to partition the array into “less than pivot” and “greater than pivot” subarrays, then recursively sorts each partition.
- **Ideal Use**: Efficient on both **small** and **large** datasets.
- **Time Complexity**:  
  - **Best/Average Case**: O(n log n)  
  - **Worst Case**: O(n²) – typically when the pivot choice is poor (e.g., already sorted data with naive pivot)
- **Benefits**:
  - Very fast on large, random datasets  
  - In‐place (requires only O(log n) extra space for recursion)  
  - Widely used in practice with good pivot‐selection strategies


### 🔁 Comparison Focus

We will compare these two algorithms by:

- Running them on varying dataset sizes from the sales data
- Recording execution time and step count
- Analyzing performance for best, average, and worst-case inputs


![image](https://github.com/user-attachments/assets/a6c04119-d342-496e-afaf-9512c35f0580)
![image](https://github.com/user-attachments/assets/33ad993e-cd6d-4cec-9f3c-a2c4fc2b8a4a)

---
### 🔁 Summary Comparison Table

| Feature                    | Insertion Sort              | QuickSort                   |
|----------------------------|-----------------------------|-----------------------------|
| **Method**                 | Insert into sorted portion  | Divide & conquer via pivot  |
| **Best Case**              | O(n) (sorted input)         | O(n log n) (balanced pivots)|
| **Average Case**           | O(n²)                       | O(n log n)                  |
| **Worst Case**             | O(n²)                       | O(n²) (poor pivot)          |
| **Stability**              | ✅ Stable                  | ❌ Not guaranteed           |
| **Memory Overhead**        | O(1) extra                  | O(log n) recursion stack    |
| **Dataset Suitability**    | Small or nearly sorted      | Small and large             |

<div align="center">
  ⚔️ Insertion Sort vs QuickSort – Who wins on the leaderboard? 🎮📊
</div>
