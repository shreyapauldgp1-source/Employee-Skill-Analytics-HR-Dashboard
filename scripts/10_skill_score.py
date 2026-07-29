import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/processed/HR_Analytics_Final.csv")

print("=" * 60)
print("EMPLOYEE SKILL SCORE")
print("=" * 60)

# ----------------------------
# Normalize columns to 0-100
# ----------------------------

df["Performance_Score"] = (df["PerformanceRating"] / df["PerformanceRating"].max()) * 100

df["Training_Score"] = (df["TrainingTimesLastYear"] / df["TrainingTimesLastYear"].max()) * 100

df["Experience_Score"] = (df["TotalWorkingYears"] / df["TotalWorkingYears"].max()) * 100

df["JobLevel_Score"] = (df["JobLevel"] / df["JobLevel"].max()) * 100

df["Education_Score"] = (df["Education"] / df["Education"].max()) * 100


df["SkillScore"] = (
    df["Performance_Score"] * 0.30 +
    df["Training_Score"] * 0.20 +
    df["Experience_Score"] * 0.25 +
    df["JobLevel_Score"] * 0.15 +
    df["Education_Score"] * 0.10
)

print("\nTop 10 Employees by Skill Score")
print(df[["EmpID", "JobRole", "SkillScore"]].sort_values("SkillScore", ascending=False).head(10))


def skill_level(score):
    if score < 40:
        return "Beginner"
    elif score < 60:
        return "Intermediate"
    elif score < 80:
        return "Advanced"
    else:
        return "Expert"

df["SkillLevel"] = df["SkillScore"].apply(skill_level)

print("\nSkill Level Distribution")
print(df["SkillLevel"].value_counts())


skill_distribution = df["SkillLevel"].value_counts()

plt.figure(figsize=(7,5))
skill_distribution.plot(kind="bar")

plt.title("Employee Skill Level Distribution")
plt.xlabel("Skill Level")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/skills/skill_level_distribution.png", dpi=300)
plt.show()


df.to_csv("data/processed/HR_Analytics_Dashboard.csv", index=False)

print("\n✅ Dashboard dataset created successfully!")