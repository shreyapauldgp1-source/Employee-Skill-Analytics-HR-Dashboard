import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/processed/HR_Analytics_Final.csv")

# Calculate average salary
avg_salary = df.groupby("Department")["MonthlyIncome"].mean()

print(avg_salary)

plt.figure(figsize=(8,5))
avg_salary.plot(kind="bar")

plt.title("Average Monthly Income by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Income")

plt.tight_layout()
plt.savefig("images/salary/average_salary_department.png", dpi=300)
plt.show()

# Average Salary by Job Role
avg_salary_job = df.groupby("JobRole")["MonthlyIncome"].mean().sort_values()

print("\nAverage Salary by Job Role")
print(avg_salary_job)

plt.figure(figsize=(12,6))
avg_salary_job.plot(kind="bar")

plt.title("Average Monthly Income by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Average Monthly Income")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/salary/average_salary_jobrole.png", dpi=300)
plt.show()

salary_slab = df["SalarySlab"].value_counts()

print("\nSalary Slab Distribution")
print(salary_slab)

plt.figure(figsize=(7,5))
salary_slab.plot(kind="bar")

plt.title("Salary Slab Distribution")
plt.xlabel("Salary Slab")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/salary/salary_slab_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(8,5))

df["MonthlyIncome"].plot(kind="hist", bins=15)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/salary/monthly_income_distribution.png", dpi=300)
plt.show()

print("\nHighest Monthly Income")
print(df["MonthlyIncome"].max())

print("\nLowest Monthly Income")
print(df["MonthlyIncome"].min())

print("\nAverage Monthly Income")
print(round(df["MonthlyIncome"].mean(), 2))

