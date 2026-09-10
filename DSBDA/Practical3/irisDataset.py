import pandas as pd

# Load dataset
iris = pd.read_csv("iris.csv")

print("Dataset Preview:\n", iris.head())

# Group by species
grouped = iris.groupby('species')

# Basic statistics
stats = grouped.describe()

print("\nDetailed Statistics:\n", stats)

# Custom stats (mean, std, percentiles)
for species, data in grouped:
    print(f"\nStatistics for {species}:\n")
    print("Mean:\n", data.mean(numeric_only=True))
    print("\nStandard Deviation:\n", data.std(numeric_only=True))
    numeric_data = data.select_dtypes(include=['number'])
    print("\nPercentiles:\n", numeric_data.quantile([0.25, 0.5, 0.75]))