import pandas as pd

# Load Final Dataset
df = pd.read_csv("data/processed/HR_Analytics_Final.csv")

print("="*60)
print("EXPLORATORY DATA ANALYSIS")
print("="*60)

# ------------------------
# Total Employees
# ------------------------

print("\nTotal Employees")

print(df.shape[0])

# ------------------------
# Total Columns
# ------------------------

print("\nTotal Features")

print(df.shape[1])

# ------------------------
# Gender Distribution
# ------------------------

print("\nGender Distribution")

print(df["Gender"].value_counts())

# ------------------------
# Department Distribution
# ------------------------

print("\nDepartment Distribution")

print(df["Department"].value_counts())

# ------------------------
# Job Role Distribution
# ------------------------

print("\nJob Role Distribution")

print(df["JobRole"].value_counts())