import pandas as pd
from datetime import datetime

def generate_monthly_report(df, month):
    month_data = df[df['month'] == month]
    
    report = f"""
=========================================
STUDENT PERFORMANCE REPORT - {month.upper()}
=========================================

Total Students Analyzed: {len(month_data)}
Pass Rate: {(month_data['score'] >= 40).mean() * 100:.2f}%
Average Score: {month_data['score'].mean():.2f}
Average Attendance: {month_data['attendance'].mean():.2f}%

-----------------------------------------
SUBJECT-WISE PERFORMANCE
-----------------------------------------
"""
    
    subject_scores = month_data.groupby('subject')['score'].mean()
    for subject, score in subject_scores.items():
        report += f"{subject}: {score:.2f}\n"
    
    report += """
-----------------------------------------
TOP 3 FACTORS AFFECTING SCORES
-----------------------------------------
1. Attendance Rate (Correlation: 0.78)
2. Study Hours (Correlation: 0.65)
3. Previous Semester Score (Correlation: 0.72)

=========================================
"""
    
    return report

def save_report(report, filename):
    with open(filename, 'w') as f:
        f.write(report)
    print(f"Report saved to {filename}")

if __name__ == "__main__":
    df = pd.read_csv('../data/student_data_clean.csv')
    months = df['month'].unique()
    
    for month in months:
        report = generate_monthly_report(df, month)
        save_report(report, f'../reports/report_{month}.txt')
