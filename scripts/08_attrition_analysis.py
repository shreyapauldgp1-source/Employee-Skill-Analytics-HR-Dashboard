import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/processed/HR_Analytics_Final.csv")

print("=" * 60)
print("ATTRITION ANALYSIS")
print("=" * 60)

# -------------------------
# Overall Attrition
# -------------------------

attrition = df["Attrition"].value_counts()

print("\nOverall Attrition")
print(attrition)

plt.figure(figsize=(6,5))
attrition.plot(kind="bar")

plt.title("Overall Attrition")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/attrition/overall_attrition.png", dpi=300)
plt.show()


attrition_department = pd.crosstab(df["Department"], df["Attrition"])

print("\nAttrition by Department")
print(attrition_department)

attrition_department.plot(kind="bar", figsize=(8,5))

plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/attrition/attrition_by_department.png", dpi=300)
plt.show()


attrition_gender = pd.crosstab(df["Gender"], df["Attrition"])

print("\nAttrition by Gender")
print(attrition_gender)

attrition_gender.plot(kind="bar", figsize=(6,5))

plt.title("Attrition by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/attrition/attrition_by_gender.png", dpi=300)
plt.show()


attrition_overtime = pd.crosstab(df["OverTime"], df["Attrition"])

print("\nAttrition by Overtime")
print(attrition_overtime)

attrition_overtime.plot(kind="bar", figsize=(6,5))

plt.title("Overtime vs Attrition")
plt.xlabel("OverTime")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/attrition/overtime_vs_attrition.png", dpi=300)
plt.show()


