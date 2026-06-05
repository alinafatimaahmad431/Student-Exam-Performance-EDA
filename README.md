# 🐍 Student Exam Performance — EDA (Data Analysis using Python)

**Author:** Alina Fatima Ahmad  
**Tools:** Python · Pandas · NumPy · Matplotlib  
**Skills:** Data Cleaning · EDA · Feature Engineering · Data Visualization · Descriptive Statistics

---

## 🔴 Live Repository

> 💻 **[github.com/alinafatimaahmad431/Student-Exam-Performance-EDA](https://github.com/alinafatimaahmad431/Student-Exam-Performance-EDA)**

---

## 📌 Project Overview

End-to-end Exploratory Data Analysis (EDA) on a Student Exam Performance dataset with 200 records. Covers the full data analysis pipeline — from raw data ingestion and cleaning to statistical analysis and multi-panel visualizations — generating actionable academic insights.

---

## 🔄 Analysis Pipeline

```
Raw Data → Inspection → Cleaning → Feature Engineering → EDA → Visualizations → Insights
```

| Step | What Was Done |
|------|---------------|
| **Data Inspection** | Shape, dtypes, null check, first look at records |
| **Data Cleaning** | Filled missing scores with column median, removed duplicates |
| **Feature Engineering** | Added total score, average score, grade column (A/B/C/D/F) |
| **Descriptive Statistics** | Mean, median, std, min/max by group (gender, test prep, education) |
| **Visualizations** | 6-panel chart covering distributions, comparisons, correlations |
| **Insights** | Summary of key findings with quantified impact |

---

## 📊 Visualizations Generated

| Chart | Type | Purpose |
|-------|------|---------|
| Score Distribution | Histogram | Compare spread across Math, Reading, Writing |
| Score by Gender | Bar Chart | Gender-based performance comparison |
| Test Prep Impact | Bar Chart | Effect of test preparation on scores |
| Grade Distribution | Pie Chart | % of students in each grade band |
| Parental Education vs Score | Horizontal Bar | Socioeconomic factor analysis |
| Math vs Reading | Scatter Plot | Correlation analysis between subjects |

---

## 💡 Key Insights

- Students who completed test prep score **~8 points higher** on average
- Math and Reading show a **strong positive correlation (r ≈ 0.82)**
- Higher parental education consistently leads to better student outcomes
- Around **15% of students** fall in the top A-grade band

---

## ▶️ How to Run

**Install dependencies:**
```bash
pip install pandas numpy matplotlib
```

**Run the analysis:**
```bash
python eda_analysis.py
```

**Output:** Console statistics + `eda_visualizations.png` saved locally ✅

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `eda_analysis.py` | Full pipeline — inspection, cleaning, EDA, visualizations |
| `eda_visualizations.png` | Generated 6-panel chart output |
| `README.md` | Project documentation |

---

## 🛠️ Libraries Used

```python
import pandas as pd        # Data manipulation & cleaning
import numpy as np         # Numerical operations
import matplotlib.pyplot   # Visualizations
import warnings            # Suppress non-critical warnings
```

---

## 📬 Contact

**Alina Fatima Ahmad**  
📧 alinafatimaahmad431@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/alina-fatima-2555b5312/)  
💻 [GitHub](https://github.com/alinafatimaahmad431)

---

> ⭐ If you found this project helpful, please give it a star!
