<!--
  README.md for the Video Game Sales Analysis Project
  --------------------------------------------------
  This repository contains code and data for analyzing video game sales from 1980 to 2018.
-->

# 🎮 Video Game Sales Analysis (1980–2018)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow.svg)](#requirements)  
[![Project Status: Analysis](https://img.shields.io/badge/Status-Analysis-green.svg)](#status)

A **comprehensive** exploration of video game market trends, genres, and regional performance across four decades.

---

## 🚀 Introduction

The global video game industry has evolved dramatically since the 1980s. This project analyzes sales data from 1980 through 2018 to uncover:

- Top-selling platforms and genres  
- Regional market differences (NA, EU, JP, Other)  
- Sales trends over time  
- Correlations between critic/user ratings and sales  

---

## 📊 Dataset

- **Source**: Cleaned sales dataset covering video games released from 1980 to 2018.
- **Filename**: `data/video_game_sales.csv`
- **Fields**: `Name`, `Platform`, `Year`, `Genre`, `Publisher`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`, `Critic_Score`, `User_Score`

> 💾 **Size**: ~16,598 records

---

## 🛠 Code & Analysis

All code lives in the `src/` directory:

- `src/data_preprocessing.py` – Clean & prepare dataset  
- `src/eda.ipynb` – Exploratory Data Analysis notebook  
- `src/visualizations.py` – Chart generation scripts  
- `src/modeling.py` – Predictive modeling examples (e.g., regression)  

### Quickstart

1. **Clone** the repo  
   ```bash
   git clone https://github.com/yourusername/vg-sales-analysis.git
   cd vg-sales-analysis
   ```
2. **Install** dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. **Run** EDA notebook  
   ```bash
   jupyter notebook src/eda.ipynb
   ```
4. **Generate** visualizations  
   ```bash
   python src/visualizations.py
   ```

---

## 🔍 Key Insights

- 📈 **Genre Trends**: Action and Shooter titles dominate global sales.  
- 🌎 **Regional Favorites**: Japan favors Role-Playing Games, North America prefers Sports.  
- 🕹️ **Platform Shifts**: Transition from NES/SNES to current-gen consoles observable in sales spikes.  
- ⭐ **Ratings Correlation**: Higher critic scores moderately correlate with stronger global sales.

> _See the full report in `reports/` for detailed charts and tables._

---

## 📂 Repository Structure

```
├── data/
│   └── video_game_sales.csv
├── src/
│   ├── data_preprocessing.py
│   ├── eda.ipynb
│   ├── visualizations.py
│   └── modeling.py
├── reports/
│   └── vg_sales_report.pdf
├── requirements.txt
└── README.md
```

---

## 🎯 Roadmap & Status

- **Current**: Data cleaning & exploratory analysis (Complete)  
- **Next**: Advanced predictive modeling & time-series forecasting  
- **Future**: Interactive dashboard & web deployment  

---

## 📅 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  🎮✨ Dive into the data and level up your insights! ✨📊
</div>
