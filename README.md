# Student Performance Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)

## 📊 Project Overview
Analyzed 300+ student records using Python and Power BI to track academic performance, attendance correlation, and pass/fail trends. Automated monthly reports reducing manual work by 60%.

## 🎯 Objectives
- Clean and deduplicate student records
- Track pass/fail trends by subject
- Analyze subject-wise performance
- Identify correlation between attendance and scores
- Identify top 3 factors affecting student scores
- Automate monthly reporting

## 📁 Project Structure
```
student-performance-dashboard/
├── data/               # Raw and processed data
├── code/               # Python scripts for analysis
├── reports/            # Generated reports
├── powerbi/            # Power BI dashboard files
└── README.md
```

## 🛠️ Tech Stack
- **Python 3.8+** - Data analysis
- **Pandas** - Data cleaning, duplicate removal
- **Power BI** - Interactive dashboards
- **Matplotlib/Seaborn** - Data visualization

## 📈 Key Insights

### Top 3 Factors Affecting Scores
1. **Attendance Rate** - Strong positive correlation (0.78)
2. **Study Hours** - Moderate positive correlation (0.65)
3. **Previous Semester Score** - Strong predictive factor (0.72)

### Performance Summary
- Overall Pass Rate: **78%**
- Highest scoring subject: **Mathematics** (82%)
- Lowest scoring subject: **Science** (68%)
- Average attendance: **75%**

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Power BI Desktop

### Installation
```bash
cd student-performance-dashboard
pip install -r requirements.txt
```

### Running the Analysis
```bash
python code/data_cleaning.py
python code/analysis.py
python code/generate_report.py
```

## 📊 Dashboard Features
- Pass/Fail trends over time
- Subject-wise performance comparison
- Attendance vs Score correlation scatter plot
- Top/bottom performing students
- Interactive filters (class, subject, date range)

## 📝 Sample Data
Sample data is available in `data/student_data.csv`

## 📅 Timeline
- **Jan 2026** - Project started
- **Present** - Ongoing improvements

## 👤 Author
Kanchan Wadhonkar

## 📞 Contact
For questions, reach out via GitHub issues.
