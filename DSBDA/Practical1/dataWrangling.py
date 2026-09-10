# ==========================================
# 1. IMPORT REQUIRED LIBRARIES
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 2. LOAD DATASET
# ==========================================
# Make sure 'titanic.csv' is in the same folder
df = pd.read_csv("titanic.csv")

print("Dataset Loaded Successfully!\n")

# ==========================================
# 3. BASIC DATA EXPLORATION
# ==========================================

# Display first 5 rows
print("First 5 rows of dataset:")
print(df.head(), "\n")

# Check dimensions
print("Shape of dataset (rows, columns):")
print(df.shape, "\n")

# Check column names
print("Column Names:")
print(df.columns, "\n")

# Check data types
print("Data Types:")
print(df.dtypes, "\n")

# ==========================================
# 4. DATA PREPROCESSING
# ==========================================

# Summary statistics
print("Statistical Summary:")
print(df.describe(), "\n")

# Check missing values
print("Missing Values in each column:")
print(df.isnull().sum(), "\n")

# ==========================================
# 5. HANDLE MISSING VALUES
# ==========================================

# Fill missing Age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin column (too many missing values)
if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'], inplace=True)

print("Missing Values After Treatment:")
print(df.isnull().sum(), "\n")

# ==========================================
# 6. DATA FORMATTING (TYPE CONVERSION)
# ==========================================

# Convert to categorical
df['Survived'] = df['Survived'].astype('category')
df['Pclass'] = df['Pclass'].astype('category')

print("Data Types After Conversion:")
print(df.dtypes, "\n")

# ==========================================
# 7. DATA NORMALIZATION
# ==========================================

# Normalize Fare column using Min-Max scaling
df['Fare'] = (df['Fare'] - df['Fare'].min()) / (df['Fare'].max() - df['Fare'].min())

print("Fare column normalized.\n")

# ==========================================
# 8. CONVERT CATEGORICAL → NUMERICAL
# ==========================================

# Label Encoding for Sex
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

print("Sex column encoded.\n")

# One-Hot Encoding for Embarked
df = pd.get_dummies(df, columns=['Embarked'])

print("Embarked column one-hot encoded.\n")

# ==========================================
# 9. FINAL DATASET CHECK
# ==========================================

print("Final Dataset Info:")
print(df.info(), "\n")

print("Final Dataset Preview:")
print(df.head(), "\n")

# ==========================================
# 10. OPTIONAL: SAVE CLEANED DATA
# ==========================================

df.to_csv("cleaned_titanic.csv", index=False)
print("Cleaned dataset saved as 'cleaned_titanic.csv'")