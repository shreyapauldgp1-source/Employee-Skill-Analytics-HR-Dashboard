# Employee Skill Analytics & HR Dashboard

## Project Overview

The Employee Skill Analytics & HR Dashboard is a data analytics project developed to analyze employee demographics, salary, skill levels, performance, and attrition trends. The project combines Python for data preprocessing and machine learning with Power BI for interactive dashboard visualization.

The objective of this project is to help HR professionals gain valuable insights into workforce performance, identify patterns in employee attrition, and support data-driven decision-making.

---

## Objectives

- Analyze employee demographic information.
- Evaluate employee skill levels and performance.
- Monitor salary distribution across departments.
- Analyze employee attrition trends.
- Build an interactive HR analytics dashboard.
- Develop a machine learning model to predict employee attrition.

---

## Dataset

**Dataset Name:** HR Analytics Dashboard Dataset

The dataset contains employee information such as:

- Employee ID
- Age
- Gender
- Department
- Job Role
- Monthly Income
- Performance Rating
- Skill Score
- Work-Life Balance
- Overtime
- Attrition
- Years at Company
- Training Times Last Year
- Education
- Job Satisfaction
- and other HR-related attributes.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Power BI Desktop
- VS Code

---

## Data Preprocessing

The following preprocessing steps were performed:

- Removed duplicate records.
- Handled missing values.
- Detected and treated outliers.
- Encoded categorical variables.
- Performed feature engineering.
- Generated Skill Score and Skill Level features.

---

## Exploratory Data Analysis (EDA)

EDA included:

- Gender Distribution
- Department-wise Employee Distribution
- Salary Analysis
- Skill Level Distribution
- Attrition Analysis
- Work-Life Balance Distribution
- Overtime Analysis
- Performance Rating Analysis

---

## Machine Learning Model

A **Random Forest Classifier** was implemented to predict employee attrition.

### Model Details

- Algorithm: Random Forest Classifier
- Train-Test Split: 80:20
- Accuracy: **88.81%**

### Model Evaluation

- Accuracy Score
- Classification Report
- Confusion Matrix
- Feature Importance

The trained model was saved using Joblib for future predictions.

---

## Power BI Dashboard

The dashboard contains:

### KPI Cards

- Total Employees
- Average Salary
- Average Skill Score
- Attrition Rate

### Interactive Filters

- Department
- Gender
- Skill Level
- Job Role
- Attrition

### Visualizations

- Gender Distribution
- Employees by Department
- Skill Level Distribution
- Work-Life Balance Distribution
- Average Skill Score by Department
- Department-wise Attrition
- Overtime vs Attrition

---

## Project Structure

```
Employee_Skill_Analytics_HR_Dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│   └── Employee_Skill_Analytics.pbix
│
├── images/
│   └── dashboard.png
│
├── models/
│   └── random_forest_model.pkl
│
├── reports/
│   └── Progress Reports
│
├── scripts/
│
├── README.md
├── requirements.txt
└── main.py
```

---

## Key Insights

- Total Employees: **1,473**
- Average Salary: **₹6.50K**
- Average Skill Score: **52.05**
- Attrition Rate: **16.09%**
- Research & Development has the highest employee count.
- Intermediate employees represent the largest skill-level group.
- Overtime is associated with higher attrition.
- Monthly Income and Overtime are among the most important features for predicting attrition.

---

## Future Enhancements

- Deploy the machine learning model using Flask or Streamlit.
- Integrate real-time HR databases.
- Improve prediction accuracy using advanced machine learning techniques.
- Add employee recommendation and retention analysis.

---

## Project Team

This project was developed as part of a group assignment for the Data Analytics course.

