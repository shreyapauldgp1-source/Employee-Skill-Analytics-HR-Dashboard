import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/HR_Analytics_Cleaned.csv")

print("=" * 60)
print("CHECKING CONSTANT COLUMNS")
print("=" * 60)

columns_to_check = ["EmployeeCount", "Over18", "StandardHours"]

for column in columns_to_check:
    print(f"\n{column}")
    print(df[column].value_counts())