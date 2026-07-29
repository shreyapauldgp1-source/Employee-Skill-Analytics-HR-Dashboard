import pandas as pd

# Load dataset
df = pd.read_csv("data/processed/HR_Analytics_Dashboard.csv")

print("=" * 60)
print("DASHBOARD DATASET")
print("=" * 60)

# ------------------------
# KPI Calculations
# ------------------------

total_employees = len(df)

attrition_rate = round(
    (df["Attrition"].value_counts()["Yes"] / total_employees) * 100, 2
)

average_salary = round(df["MonthlyIncome"].mean(), 2)

average_skill = round(df["SkillScore"].mean(), 2)

average_experience = round(df["TotalWorkingYears"].mean(), 2)

print("\nDashboard KPIs")

print(f"Total Employees : {total_employees}")

print(f"Attrition Rate : {attrition_rate}%")

print(f"Average Salary : ₹{average_salary}")

print(f"Average Skill Score : {average_skill}")

print(f"Average Experience : {average_experience} Years")