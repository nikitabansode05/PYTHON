# Import libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

# -------------------------------
# Load Iris Dataset
# -------------------------------
iris = load_iris()

X = iris.data
y = iris.target

# -------------------------------
# Split Dataset
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

# -------------------------------
# Train Naive Bayes Model
# -------------------------------
model = GaussianNB()

model.fit(X_train, y_train)

# -------------------------------
# Predictions
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# Confusion Matrix
# -------------------------------
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:\n")
print(cm)

# -------------------------------
# Performance Metrics
# -------------------------------
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy

precision = precision_score(
    y_test,
    y_pred,
    average='macro'
)

recall = recall_score(
    y_test,
    y_pred,
    average='macro'
)

print("\nAccuracy :", accuracy)
print("Error Rate :", error_rate)
print("Precision :", precision)
print("Recall :", recall)

# -------------------------------
# TP, FP, TN, FN Calculation
# -------------------------------
print("\nClass-wise TP, FP, TN, FN:\n")

for i in range(len(cm)):
    
    TP = cm[i][i]
    
    FP = sum(cm[:, i]) - TP
    
    FN = sum(cm[i, :]) - TP
    
    TN = cm.sum() - (TP + FP + FN)
    
    print(f"Class {i}:")
    print("TP =", TP)
    print("FP =", FP)
    print("FN =", FN)
    print("TN =", TN)
    print()