import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

# Display first few rows
print("Dataset Preview:\n", df.head())

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing numeric values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Create Age Groups (categorical variable)
df['Age_Group'] = pd.cut(df['Age'],
                        bins=[0, 20, 30, 40, 50, 100],
                        labels=['Teen', '20s', '30s', '40s', '50+'])

# Group by Age_Group and calculate statistics for Income
grouped_stats = df.groupby('Age_Group')['Income'].agg(
    ['mean', 'median', 'min', 'max', 'std']
)

print("\nGrouped Summary Statistics:\n", grouped_stats)

# Create list of income values per category
income_list = df.groupby('Age_Group')['Income'].apply(list)

print("\nIncome List by Age Group:\n", income_list)
