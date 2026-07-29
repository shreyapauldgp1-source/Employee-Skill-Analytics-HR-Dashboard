import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/processed/HR_Analytics_Final.csv")

print("=" * 60)
print("PERFORMANCE ANALYSIS")
print("=" * 60)

# --------------------------
# Performance Rating
# --------------------------
performance = df["PerformanceRating"].value_counts().sort_index()

print("\nPerformance Rating")
print(performance)

plt.figure(figsize=(6,5))
performance.plot(kind="bar")

plt.title("Performance Rating Distribution")
plt.xlabel("Performance Rating")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/performance/performance_rating_distribution.png", dpi=300)
plt.show()

# --------------------------
# Training Times Last Year
# --------------------------
training = df["TrainingTimesLastYear"].value_counts().sort_index()

print("\nTraining Times Last Year")
print(training)

plt.figure(figsize=(8,5))
training.plot(kind="bar")

plt.title("Training Times Last Year")
plt.xlabel("Number of Trainings")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/performance/training_distribution.png", dpi=300)
plt.show()

# --------------------------
# Work-Life Balance
# --------------------------
worklife = df["WorkLifeBalance"].value_counts().sort_index()

print("\nWork-Life Balance")
print(worklife)

plt.figure(figsize=(6,5))
worklife.plot(kind="bar")

plt.title("Work-Life Balance")
plt.xlabel("Work-Life Balance Rating")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/performance/worklife_balance_distribution.png", dpi=300)
plt.show()

# --------------------------
# Job Satisfaction
# --------------------------
jobsat = df["JobSatisfaction"].value_counts().sort_index()

print("\nJob Satisfaction")
print(jobsat)

plt.figure(figsize=(6,5))
jobsat.plot(kind="bar")

plt.title("Job Satisfaction")
plt.xlabel("Job Satisfaction Rating")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/performance/job_satisfaction_distribution.png", dpi=300)
plt.show()

