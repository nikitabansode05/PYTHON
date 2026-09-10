# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
iris = sns.load_dataset('iris')

# -------------------------------
# 1. Features and Data Types
# -------------------------------
print("First 5 Rows:\n")
print(iris.head())

print("\nDataset Information:\n")
print(iris.info())

print("\nFeature Names:\n")
print(iris.columns)

print("\nData Types:\n")
print(iris.dtypes)

# -------------------------------
# 2. Histograms for Each Feature
# -------------------------------
iris.hist(figsize=(10,8))

plt.suptitle("Histogram of Iris Dataset Features")
plt.show()

# -------------------------------
# 3. Box Plot for Each Feature
# -------------------------------
plt.figure(figsize=(12,8))

for i, column in enumerate(iris.columns[:-1], 1):
    plt.subplot(2,2,i)
    sns.boxplot(y=iris[column])
    plt.title(f"Box Plot of {column}")

plt.tight_layout()
plt.show()

# -------------------------------
# 4. Compare Distributions
# -------------------------------
print("\nInference:")
print("1. Most features are normally distributed.")
print("2. Sepal length and petal length show wider spread.")
print("3. Petal width has some possible outliers.")
print("4. Species column is categorical (nominal).")