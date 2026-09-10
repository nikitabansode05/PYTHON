# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------------
# Load Dataset (use your file path if local)
# -------------------------------
df = pd.read_csv("housing.csv")

# -------------------------------
# Convert column names to lowercase (IMPORTANT FIX)
# -------------------------------
df.columns = df.columns.str.lower()

# -------------------------------
# Display dataset info
# -------------------------------
print("Columns:", df.columns)
print("\nFirst 5 rows:\n", df.head())
print("\nMissing values:\n", df.isnull().sum())

# -------------------------------
# Correlation Heatmap
# -------------------------------
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# Define Features and Target
# -------------------------------
X = df.drop("medv", axis=1)
y = df["medv"]

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Train Model
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# Predictions
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# -------------------------------
# Actual vs Predicted Scatter Plot
# -------------------------------
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.show()

# -------------------------------
# Line Plot (optional)
# -------------------------------
plt.plot(range(len(y_test)), y_test.values, label="Actual")
plt.plot(range(len(y_pred)), y_pred, label="Predicted")
plt.legend()
plt.title("Actual vs Predicted Line Graph")
plt.show()

# -------------------------------
# Coefficients (Feature Importance)
# -------------------------------
coeff_df = pd.DataFrame(model.coef_, X.columns, columns=["Coefficient"])
print("\nFeature Coefficients:\n", coeff_df)

# -------------------------------
# Intercept
# -------------------------------
print("\nIntercept:", model.intercept_)