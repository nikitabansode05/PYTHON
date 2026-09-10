import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Create box plot
plt.figure(figsize=(10,6))

sns.boxplot(
    x='sex',
    y='age',
    hue='survived',
    data=titanic
)

# Add labels and title
plt.title("Age Distribution by Gender and Survival Status")
plt.xlabel("Gender")
plt.ylabel("Age")

plt.show()