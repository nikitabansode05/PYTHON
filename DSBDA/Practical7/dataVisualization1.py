import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Display first 5 rows
print(titanic.head())

# Dataset information
print("\nDataset Shape:", titanic.shape)

# Plot histogram for Fare distribution
plt.figure(figsize=(10,6))

sns.histplot(titanic['fare'], bins=30, kde=True)

plt.title("Distribution of Ticket Fare in Titanic Dataset")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")

plt.show()