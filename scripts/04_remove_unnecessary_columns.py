import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/HR_Analytics_Cleaned.csv")

print("=" * 60)
print("REMOVING UNNECESSARY COLUMNS")
print("=" * 60)

# Columns to remove
columns_to_remove = [
    "EmployeeCount",
    "Over18",
    "StandardHours"
]

# Remove columns
df.drop(columns=columns_to_remove, inplace=True)

print("\nColumns removed successfully!")

print("\nRemaining Columns:", len(df.columns))

print("\nUpdated Dataset Shape:")
print(df.shape)

# Save dataset
df.to_csv(
    "data/processed/HR_Analytics_Final.csv",
    index=False
)

print("\n✅ Final cleaned dataset saved successfully!")