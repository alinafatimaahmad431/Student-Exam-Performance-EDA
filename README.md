# 🐍 Data Analysis Using Python — EDA Project

**Author:** Alina Fatima Ahmad  
**Tools:** Python · Pandas · NumPy · Matplotlib · Seaborn  
**Skills:** Data Cleaning, EDA, Feature Engineering, Data Visualization, Statistical Analysis

---

## 📌 Project Overview

End-to-end Exploratory Data Analysis (EDA) on a Student Exam Performance dataset. Covers the full data analysis pipeline from raw data ingestion to actionable insights and visualizations.

---

## 🔄 Pipeline Steps

```
Raw Data → Inspection → Cleaning → Feature Engineering → EDA → Visualizations → Insights
```

| Step | Description |
|------|-------------|
| Data Inspection | Shape, dtypes, null check, first look |
| Data Cleaning | Handle missing values (median fill), remove duplicates |
| Feature Engineering | Total score, average score, grade classification |
| Descriptive Statistics | Mean, median, std, percentiles by group |
| Visualizations | 6-panel chart: distributions, bar plots, pie, scatter, correlation |
| Insights | Summary of key findings |

---

## 📊 Visualizations Generated

- Score distribution histogram (Math / Reading / Writing)
- Average score by gender
- Impact of test preparation on scores
- Grade distribution pie chart
- Parental education vs average score
- Math vs Reading correlation scatter plot

---

## 📈 Sample Insights

- Students who completed test prep score **~8 points higher** on average
- Math and Reading scores show a **strong positive correlation (0.82)**
- Higher parental education levels correspond with better student outcomes

---

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib
python eda_analysis.py
```

Output: Console stats + `eda_visualizations.png` chart saved locally.

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `eda_analysis.py` | Main analysis script (end-to-end pipeline) |
| `eda_visualizations.png` | Generated chart output |
| `README.md` | Project documentation |
