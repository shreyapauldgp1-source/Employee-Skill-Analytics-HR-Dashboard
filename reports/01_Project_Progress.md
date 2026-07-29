# Employee Skill Analytics & HR Dashboard using Data Analytics

## Project Progress Report

### Students Name
Shreya Paul, Anandi Debnath, Joy Sadhu, Tuhin Chakraborty, Shibam Chatterjee, Monoranjan Pal

### Project Title
Employee Skill Analytics & HR Dashboard using Data Analytics

---

# Day 1: Project Setup & Data Preparation

## Objectives

The objective of Day 1 was to set up the project environment, organize the project structure, understand the HR Analytics dataset, and perform data cleaning to prepare the data for analysis.

---

## Tasks Completed

### 1. Project Folder Structure

Created a professional project folder structure including:

- data/
  - raw/
  - processed/
- scripts/
- notebooks/
- dashboard/
- images/
- reports/
- README.md
- requirements.txt
- main.py

---

### 2. Dataset Import

- Downloaded the HR Analytics dataset.
- Stored the original dataset inside the **data/raw/** folder.
- Loaded the dataset using the Pandas library.

Python Function Used:

```python
pd.read_csv()
```

---

### 3. Dataset Exploration

Explored the dataset using:

- head()
- info()
- shape
- columns
- describe()

### Dataset Summary

- Total Records (Before Cleaning): **1480**
- Total Columns: **38**

---

### 4. Data Quality Assessment

Checked the dataset for:

- Missing Values
- Duplicate Records

#### Results

- Missing Values Found: **57**
- Column Containing Missing Values:
  - YearsWithCurrManager

- Duplicate Records Found:
  - **7**

---

### 5. Data Cleaning

Performed the following cleaning operations:

- Removed duplicate records.
- Filled missing values in the YearsWithCurrManager column with 0.
- Saved the cleaned dataset.

Python Functions Used:

```python
drop_duplicates()
fillna()
to_csv()
```

---

### 6. Constant Column Analysis

Checked columns containing only one unique value.

The following columns were identified as constant:

- EmployeeCount
- Over18
- StandardHours

These columns were removed because they did not provide any meaningful information for analysis.

---

### 7. Final Dataset

After cleaning:

- Total Records: **1473**
- Total Columns: **35**

Final dataset saved as:

```
data/processed/HR_Analytics_Final.csv
```

---

# Day 2: Exploratory Data Analysis (Started)

## Exploratory Data Analysis

Performed basic exploratory analysis on the cleaned dataset.

### Employee Summary

Total Employees:

**1473**

Total Features:

**35**

---

### Gender Distribution

| Gender | Employees |
|---------|----------:|
| Male | 884 |
| Female | 589 |

Observation:

The organization has a higher percentage of male employees compared to female employees.

---

### Department Distribution

| Department | Employees |
|------------|----------:|
| Research & Development | 963 |
| Sales | 447 |
| Human Resources | 63 |

Observation:

The Research & Development department has the largest workforce.

---

### Job Role Distribution

Top Job Roles:

- Sales Executive – 326
- Research Scientist – 292
- Laboratory Technician – 260

Observation:

Most employees work in Sales Executive and Research Scientist roles.

---

### Data Visualizations Created

The following charts were generated using Matplotlib:

- Gender Distribution
- Department Distribution
- Job Role Distribution
- Attrition Distribution
- Age Distribution
- Monthly Income Distribution

The generated charts were saved inside the **images/** folder for future use in the report and dashboard.

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- VS Code

---

# Current Project Status

✅ Project Setup Completed

✅ Dataset Imported

✅ Data Cleaning Completed

✅ Dataset Optimized

✅ Basic EDA Completed

✅ Initial Visualizations Created

⏳ Advanced EDA (In Progress)

⏳ Skill Score Calculation

⏳ Power BI Dashboard

⏳ Final Report

---

# Next Steps

- Perform advanced exploratory data analysis.
- Create Employee Skill Score.
- Classify employees into skill levels.
- Build an interactive Power BI dashboard.
- Prepare the final project report and presentation.


# Day 2: Exploratory Data Analysis & Feature Engineering

## Objectives

The objective of Day 2 was to perform Exploratory Data Analysis (EDA) on the cleaned HR dataset, identify meaningful business insights, visualize employee data, and create a custom Skill Score for each employee using feature engineering.

---

## Tasks Completed

### 1. Exploratory Data Analysis (EDA)

Performed exploratory analysis to understand employee demographics and workforce distribution.

### Employee Summary

- Total Employees: **1473**
- Total Features: **35**

---

### Gender Distribution

| Gender | Employees |
|---------|----------:|
| Male | 884 |
| Female | 589 |

**Observation:**

The organization has a male-dominated workforce, with approximately **60% male employees** and **40% female employees**.

---

### Department Distribution

| Department | Employees |
|------------|----------:|
| Research & Development | 963 |
| Sales | 447 |
| Human Resources | 63 |

**Observation:**

Research & Development is the largest department, while Human Resources has the smallest workforce.

---

### Job Role Distribution

Top Job Roles:

- Sales Executive – 326
- Research Scientist – 292
- Laboratory Technician – 260

**Observation:**

Most employees are working as Sales Executives, Research Scientists, and Laboratory Technicians.

---

## 2. Salary Analysis

Performed salary analysis to understand employee compensation across departments and job roles.

### Average Monthly Salary by Department

| Department | Average Monthly Salary (₹) |
|------------|---------------------------:|
| Sales | ₹6,950.24 |
| Human Resources | ₹6,654.51 |
| Research & Development | ₹6,281.25 |

**Observation:**

The Sales department has the highest average monthly salary.

---

### Average Monthly Salary by Job Role

Highest Paying Roles:

- Manager – ₹17,181.68
- Research Director – ₹16,033.55
- Healthcare Representative – ₹7,547.42

Lowest Paying Roles:

- Sales Representative – ₹2,630.05
- Laboratory Technician – ₹3,234.61
- Research Scientist – ₹3,239.97

**Observation:**

Salary increases with seniority and managerial responsibility.

---

### Salary Statistics

- Highest Monthly Salary: ₹19,999
- Lowest Monthly Salary: ₹1,009
- Average Monthly Salary: ₹6,500.23

---

### Salary Slab Distribution

| Salary Slab | Employees |
|-------------|----------:|
| Up to ₹5k | 751 |
| ₹5k–₹10k | 441 |
| ₹10k–₹15k | 148 |
| Above ₹15k | 133 |

**Observation:**

Most employees fall under the salary slab of **Up to ₹5,000**.

---

## 3. Attrition Analysis

Performed detailed employee attrition analysis.

### Overall Attrition

| Status | Employees |
|--------|----------:|
| Stayed | 1236 |
| Left | 237 |

### Attrition Rate

**16.09%**

**Observation:**

Approximately one out of every six employees has left the organization.

---

### Attrition by Department

| Department | Stayed | Left |
|------------|-------:|-----:|
| Human Resources | 51 | 12 |
| Research & Development | 830 | 133 |
| Sales | 355 | 92 |

**Observation:**

The Sales department has the highest attrition rate among all departments.

---

### Attrition by Gender

| Gender | Stayed | Left |
|--------|-------:|-----:|
| Male | 734 | 150 |
| Female | 502 | 87 |

**Observation:**

Male employees show a slightly higher attrition rate than female employees.

---

### Attrition by Overtime

| Overtime | Stayed | Left |
|----------|-------:|-----:|
| No | 947 | 110 |
| Yes | 289 | 127 |

**Observation:**

Employees working overtime are considerably more likely to leave the organization compared to those who do not work overtime.

---

## 4. Performance Analysis

Analysed employee performance using HR performance-related attributes.

The following parameters were analysed:

- Performance Rating
- Training Times Last Year
- Work-Life Balance
- Job Satisfaction

Visualizations were generated for each parameter using Matplotlib.

---

## 5. Feature Engineering – Employee Skill Score

A new feature named **Skill Score** was created to estimate employee skill levels using multiple HR parameters.

### Factors Used

- Performance Rating
- Training Times Last Year
- Total Working Years
- Job Level
- Education

Each factor was normalized and combined using weighted averages to generate a final Skill Score.

### Weight Distribution

| Parameter | Weight |
|-----------|-------:|
| Performance Rating | 30% |
| Total Working Years | 25% |
| Training Times Last Year | 20% |
| Job Level | 15% |
| Education | 10% |

---

## 6. Skill Level Classification

Employees were classified into four categories based on their Skill Score.

| Skill Level | Employees |
|-------------|----------:|
| Beginner | 124 |
| Intermediate | 1062 |
| Advanced | 277 |
| Expert | 10 |

**Observation:**

Most employees belong to the **Intermediate** skill category, while only a small number reached the **Expert** level.

---

## 7. Dashboard Dataset Creation

Created a new dataset containing all original employee information along with engineered features.

### Newly Added Columns

- Performance_Score
- Training_Score
- Experience_Score
- JobLevel_Score
- Education_Score
- SkillScore
- SkillLevel

The final dashboard-ready dataset was saved as:

```
data/processed/HR_Analytics_Dashboard.csv
```

---

## 8. Visualizations Created

The following charts were generated and saved inside the **images/** folder.

### Demographics

- Gender Distribution
- Department Distribution
- Job Role Distribution
- Age Distribution
- Education Distribution
- Marital Status Distribution

### Salary

- Monthly Income Distribution
- Salary Slab Distribution
- Average Salary by Department
- Average Salary by Job Role

### Attrition

- Overall Attrition
- Attrition by Department
- Attrition by Gender
- Overtime vs Attrition

### Performance

- Performance Rating Distribution
- Training Distribution
- Work-Life Balance Distribution
- Job Satisfaction Distribution

### Skill Analytics

- Skill Level Distribution

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- VS Code

---

# Current Project Status

✅ Exploratory Data Analysis Completed

✅ Salary Analysis Completed

✅ Attrition Analysis Completed

✅ Performance Analysis Completed

✅ Feature Engineering Completed

✅ Employee Skill Score Created

✅ Dashboard Dataset Prepared

⏳ Power BI Dashboard Development

⏳ Final Project Report

---

# Next Steps

- Build an interactive Power BI dashboard using the dashboard dataset.
- Create KPI cards and interactive visualizations.
- Prepare the final project report with screenshots and analysis.
- Design the project presentation.
- Practice project explanation and viva questions.


# Day 3 Progress Report

## Date
(Write the submission date)

---

## Work Completed

On Day 3, the primary focus was on developing the interactive Power BI dashboard for HR analytics.

The cleaned and processed HR dataset was imported into Power BI Desktop. Various visualizations were created to analyze employee demographics, departmental performance, skill levels, salaries, and attrition trends.

Key Performance Indicator (KPI) cards were added to display important metrics including:

- Total Employees
- Average Salary
- Average Skill Score
- Attrition Rate

Interactive slicers were implemented to enable dynamic filtering based on:

- Department
- Gender
- Skill Level
- Job Role
- Attrition

Several visualizations were created to present workforce insights, including:

- Gender Distribution
- Employees by Department
- Skill Level Distribution
- Work-Life Balance Distribution
- Average Skill Score by Department
- Department-wise Attrition
- Overtime vs Attrition

The dashboard layout was redesigned using a professional blush pink, lavender, and deep purple color theme. Consistent formatting, spacing, icons, and alignment were applied to improve readability and enhance the overall user experience.

---

## Outcome

A fully interactive HR Analytics dashboard was successfully developed in Power BI, enabling users to analyze workforce data and explore employee insights through dynamic visualizations and filters.

# Day 4 Progress Report

## Date
(Write the submission date)

---

## Work Completed

On Day 4, the project was finalized by integrating machine learning and completing all project documentation.

A Random Forest Classifier was implemented using Scikit-learn to predict employee attrition based on the processed HR dataset. The dataset was divided into training and testing sets using an 80:20 train-test split.

Categorical features were encoded using Label Encoding before training the model. After training, the model was evaluated using multiple performance metrics, including:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Feature Importance

The Random Forest model achieved an accuracy of **88.81%** in predicting employee attrition.

The trained model was saved using Joblib for future use and deployment.

Finally, all project files were organized, including the Power BI dashboard, Python scripts, processed datasets, machine learning model, dashboard images, progress reports, README file, and requirements file, preparing the project for GitHub submission.

---

## Outcome

The Employee Skill Analytics & HR Dashboard project was successfully completed with end-to-end implementation of data preprocessing, exploratory data analysis, machine learning, and interactive business intelligence visualization. The project provides meaningful workforce insights and demonstrates the practical application of data analytics techniques for HR decision-making.