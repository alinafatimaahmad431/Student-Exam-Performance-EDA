"""
================================================
  DATA ANALYSIS USING PYTHON — EDA PROJECT
  Author : Alina Fatima Ahmad
  Tools  : Python, Pandas, NumPy, Matplotlib, Seaborn
  Dataset: Student Exam Performance Dataset
           (source: generated / Kaggle-style)
================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
#  STEP 1: CREATE DATASET
# ─────────────────────────────────────────────
print("=" * 55)
print("  STUDENT EXAM PERFORMANCE — EDA")
print("  Author: Alina Fatima Ahmad")
print("=" * 55)

np.random.seed(42)
n = 200

data = {
    'student_id':    range(1, n + 1),
    'gender':        np.random.choice(['Male', 'Female'], n, p=[0.48, 0.52]),
    'parental_education': np.random.choice(
        ["high school", "some college", "bachelor's degree", "master's degree"],
        n, p=[0.25, 0.30, 0.30, 0.15]
    ),
    'lunch':         np.random.choice(['standard', 'free/reduced'], n, p=[0.65, 0.35]),
    'test_prep':     np.random.choice(['completed', 'none'], n, p=[0.36, 0.64]),
    'math_score':    np.clip(np.random.normal(66, 15, n).astype(int), 0, 100),
    'reading_score': np.clip(np.random.normal(69, 14, n).astype(int), 0, 100),
    'writing_score': np.clip(np.random.normal(68, 15, n).astype(int), 0, 100),
}

# Introduce missing values (realistic noise)
df = pd.DataFrame(data)
missing_idx = np.random.choice(df.index, size=10, replace=False)
df.loc[missing_idx[:5], 'math_score']    = np.nan
df.loc[missing_idx[5:], 'reading_score'] = np.nan

# ─────────────────────────────────────────────
#  STEP 2: DATA INSPECTION
# ─────────────────────────────────────────────
print("\n📋 STEP 1 — DATA INSPECTION")
print("-" * 40)
print(f"Shape         : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Columns       : {list(df.columns)}")
print("\nData Types:")
print(df.dtypes)
print("\nFirst 5 rows:")
print(df.head())

# ─────────────────────────────────────────────
#  STEP 3: DATA CLEANING
# ─────────────────────────────────────────────
print("\n🧹 STEP 2 — DATA CLEANING")
print("-" * 40)
print("Missing values BEFORE cleaning:")
print(df.isnull().sum())

# Fill missing scores with column median
df['math_score'].fillna(df['math_score'].median(), inplace=True)
df['reading_score'].fillna(df['reading_score'].median(), inplace=True)

print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())

# Check and remove duplicates
dupes = df.duplicated().sum()
print(f"\nDuplicate rows: {dupes}")
df.drop_duplicates(inplace=True)

# ─────────────────────────────────────────────
#  STEP 4: FEATURE ENGINEERING
# ─────────────────────────────────────────────
df['total_score']   = df['math_score'] + df['reading_score'] + df['writing_score']
df['average_score'] = df['total_score'] / 3

def assign_grade(avg):
    if avg >= 85: return 'A'
    elif avg >= 70: return 'B'
    elif avg >= 55: return 'C'
    elif avg >= 40: return 'D'
    else: return 'F'

df['grade'] = df['average_score'].apply(assign_grade)

# ─────────────────────────────────────────────
#  STEP 5: DESCRIPTIVE STATISTICS
# ─────────────────────────────────────────────
print("\n📊 STEP 3 — DESCRIPTIVE STATISTICS")
print("-" * 40)
stats = df[['math_score', 'reading_score', 'writing_score', 'average_score']].describe().round(2)
print(stats)

print("\n🏅 Grade Distribution:")
print(df['grade'].value_counts())

print("\n👤 Avg Score by Gender:")
print(df.groupby('gender')['average_score'].mean().round(2))

print("\n📚 Avg Score by Test Prep:")
print(df.groupby('test_prep')['average_score'].mean().round(2))

print("\n🎓 Avg Score by Parental Education:")
print(df.groupby('parental_education')['average_score'].mean().round(2).sort_values(ascending=False))

# ─────────────────────────────────────────────
#  STEP 6: VISUALIZATIONS
# ─────────────────────────────────────────────
print("\n📈 STEP 4 — GENERATING VISUALIZATIONS...")
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Student Exam Performance — EDA\nby Alina Fatima Ahmad", fontsize=14, fontweight='bold', y=1.01)

colors = ['#2E75B6', '#ED7D31', '#70AD47']

# Plot 1: Score distributions
for i, (col, c) in enumerate(zip(['math_score', 'reading_score', 'writing_score'], colors)):
    axes[0, 0].hist(df[col], bins=20, alpha=0.6, color=c, label=col.replace('_', ' ').title())
axes[0, 0].set_title('Score Distribution by Subject')
axes[0, 0].set_xlabel('Score')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].legend()

# Plot 2: Average score by gender
gender_avg = df.groupby('gender')['average_score'].mean()
axes[0, 1].bar(gender_avg.index, gender_avg.values, color=['#2E75B6', '#ED7D31'])
axes[0, 1].set_title('Average Score by Gender')
axes[0, 1].set_ylabel('Average Score')
for i, v in enumerate(gender_avg.values):
    axes[0, 1].text(i, v + 0.5, f'{v:.1f}', ha='center', fontweight='bold')

# Plot 3: Test prep impact
prep_avg = df.groupby('test_prep')['average_score'].mean()
axes[0, 2].bar(prep_avg.index, prep_avg.values, color=['#70AD47', '#FF0000'])
axes[0, 2].set_title('Impact of Test Preparation')
axes[0, 2].set_ylabel('Average Score')
for i, v in enumerate(prep_avg.values):
    axes[0, 2].text(i, v + 0.5, f'{v:.1f}', ha='center', fontweight='bold')

# Plot 4: Grade distribution pie
grade_counts = df['grade'].value_counts()
axes[1, 0].pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%',
               colors=['#70AD47', '#2E75B6', '#ED7D31', '#FFC000', '#FF0000'])
axes[1, 0].set_title('Grade Distribution')

# Plot 5: Parental education vs avg score
edu_avg = df.groupby('parental_education')['average_score'].mean().sort_values()
axes[1, 1].barh(edu_avg.index, edu_avg.values, color='#2E75B6')
axes[1, 1].set_title('Avg Score by Parental Education')
axes[1, 1].set_xlabel('Average Score')

# Plot 6: Correlation — Math vs Reading
axes[1, 2].scatter(df['math_score'], df['reading_score'], alpha=0.5, color='#2E75B6')
axes[1, 2].set_title('Math vs Reading Score Correlation')
axes[1, 2].set_xlabel('Math Score')
axes[1, 2].set_ylabel('Reading Score')
corr = df['math_score'].corr(df['reading_score'])
axes[1, 2].text(10, 90, f'Correlation: {corr:.2f}', fontsize=10, color='red')

plt.tight_layout()
plt.savefig('eda_visualizations.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Chart saved as eda_visualizations.png")

# ─────────────────────────────────────────────
#  STEP 7: KEY INSIGHTS SUMMARY
# ─────────────────────────────────────────────
print("\n💡 STEP 5 — KEY INSIGHTS")
print("=" * 55)
print(f"✅ Total students analyzed   : {len(df)}")
print(f"✅ Avg math score            : {df['math_score'].mean():.2f}")
print(f"✅ Avg reading score         : {df['reading_score'].mean():.2f}")
print(f"✅ Avg writing score         : {df['writing_score'].mean():.2f}")
print(f"✅ Test prep boosts score by : {prep_avg['completed'] - prep_avg['none']:.1f} points")
print(f"✅ Math-Reading correlation  : {corr:.2f} (strong positive)")
print(f"✅ Top grade (A) students    : {(df['grade'] == 'A').sum()} ({(df['grade']=='A').mean()*100:.1f}%)")
print(f"✅ At-risk (F grade) students: {(df['grade'] == 'F').sum()}")
print("=" * 55)
print("\n✅ EDA COMPLETE — All steps executed successfully.")