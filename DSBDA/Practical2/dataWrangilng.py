import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Create Dataset
# -------------------------------

np.random.seed(42)

data = {
    "Name": [f"Student_{i}" for i in range(1, 21)],
    "Gender": np.random.choice(["Male", "Female"], 20),
    "Math": np.random.randint(40, 100, 20).astype(float),
    "Science": np.random.randint(35, 100, 20).astype(float),
    "English": np.random.randint(45, 100, 20),
    "Attendance": np.random.randint(60, 100, 20),
    "StudyHours": np.random.randint(1, 10, 20)
}

df = pd.DataFrame(data)

# Introduce Missing Values
df.loc[3, "Math"] = np.nan
df.loc[7, "Science"] = np.nan

# Introduce Inconsistency
df.loc[5, "Attendance"] = 150

print("\nOriginal Dataset:\n")
print(df)

# -------------------------------
# Step 2: Handle Missing Values
# -------------------------------

print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values with mean
df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())

# Fix inconsistency (Attendance > 100)
df.loc[df["Attendance"] > 100, "Attendance"] = 100

print("\nDataset after handling missing values and inconsistencies:\n")
print(df)

# -------------------------------
# Step 3: Detect and Handle Outliers (IQR Method)
# -------------------------------

def handle_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Detect outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"\nOutliers in {column}:\n", outliers)

    # Cap outliers
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])

# Apply for numeric columns
numeric_columns = ["Math", "Science", "English", "Attendance", "StudyHours"]

for col in numeric_columns:
    handle_outliers(col)

print("\nDataset after handling outliers:\n")
print(df)

# -------------------------------
# Step 4: Data Transformation
# -------------------------------

# Log Transformation (reduce skewness)
df["StudyHours_log"] = np.log(df["StudyHours"])

# Min-Max Scaling
scaler = MinMaxScaler()
df["Math_scaled"] = scaler.fit_transform(df[["Math"]])

print("\nDataset after transformation:\n")
print(df)

# -------------------------------
# Step 5: Visualization (Optional)
# -------------------------------

# Boxplot to visualize outliers
plt.figure()
sns.boxplot(x=df["Math"])
plt.title("Boxplot of Math Scores")
plt.show()

# Distribution plot
plt.figure()
sns.histplot(df["StudyHours"], kde=True)
plt.title("Distribution of Study Hours")
plt.show()

# -------------------------------
# Final Output
# -------------------------------

print("\nFinal Cleaned Dataset:\n")
print(df.head())