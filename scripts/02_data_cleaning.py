import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/HR_Analytics.csv")

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

# ----------------------------
# 1. Remove duplicate records
# ----------------------------
duplicates_before = df.duplicated().sum()
print(f"Duplicate records before cleaning: {duplicates_before}")

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()
print(f"Duplicate records after cleaning: {duplicates_after}")

# ----------------------------
# 2. Handle missing values
# ----------------------------
missing_before = df["YearsWithCurrManager"].isnull().sum()
print(f"\nMissing values before cleaning: {missing_before}")

df["YearsWithCurrManager"] = df["YearsWithCurrManager"].fillna(0)

missing_after = df["YearsWithCurrManager"].isnull().sum()
print(f"Missing values after cleaning: {missing_after}")

# ----------------------------
# 3. Save cleaned dataset
# ----------------------------
df.to_csv("data/processed/HR_Analytics_Cleaned.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")