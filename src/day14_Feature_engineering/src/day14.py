
# DAY 12 — FEATURE ENGINEERING COMPLETE SCRIPT

# STEP 1 — Import Libraries

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# STEP 2 — Create Dataset (Salary Prediction Example)
# ----------------------------------------------------------
# In real projects: df = pd.read_csv("dataset.csv")

data = {
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Education_Level": ["Bachelors","Masters","PhD","PhD","Bachelors","Masters","PhD","Masters","Bachelors","Masters","Bachelors","PhD"],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000]
}

df = pd.DataFrame(data)

# TOPIC 1 — Inspect Dataset & Identify Feature Types
# ----------------------------------------------------------
print("\nDataset Info:")
print(df.info())

# Separate target variable
target = "Salary"

# Identify numerical & categorical columns
numerical_cols = ["Age", "Experience"]
categorical_cols = ["Education_Level", "Department"]

# TOPIC 2 — ENCODING CATEGORICAL VARIABLES
# ----------------------------------------------------------
# Label Encoding → for ORDINAL categories (Education Level has order)
le = LabelEncoder()
df["Education_Level_Encoded"] = le.fit_transform(df["Education_Level"])

# One-Hot Encoding → for NOMINAL categories (Department has no order)
df = pd.get_dummies(df, columns=["Department"], drop_first=True)

# Drop original categorical column after encoding
df = df.drop("Education_Level", axis=1)

print("\nDataset after encoding:")
print(df.head())

# Prepare Feature Matrix (X) and Target (y)
# ----------------------------------------------------------
X = df.drop(target, axis=1)
y = df[target]

# Train-Test Split BEFORE scaling (to avoid data leakage)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# BASELINE MODEL (Before Scaling & Polynomial Features)
# ----------------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)
baseline_preds = model.predict(X_test)

baseline_score = r2_score(y_test, baseline_preds)
print("\nBaseline Model R² Score:", baseline_score)

# ----------------------------------------------------------
# TOPIC 3 — FEATURE SCALING
# ----------------------------------------------------------
# Standard Scaling (mean=0, std=1)
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model on scaled features
scaled_model = LinearRegression()
scaled_model.fit(X_train_scaled, y_train)
scaled_preds = scaled_model.predict(X_test_scaled)

scaled_score = r2_score(y_test, scaled_preds)
print("Model Score After Scaling:", scaled_score)

# ----------------------------------------------------------
# TOPIC 4 — POLYNOMIAL FEATURES (Non-linear relationships)
# ----------------------------------------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)

X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Train model on engineered features
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
poly_preds = poly_model.predict(X_test_poly)

poly_score = r2_score(y_test, poly_preds)
print("Model Score After Polynomial Features:", poly_score)

# ----------------------------------------------------------
# FINAL COMPARISON
# ----------------------------------------------------------
print("\n===== PERFORMANCE COMPARISON =====")
print("Before Feature Engineering :", baseline_score)
print("After Scaling             :", scaled_score)
print("After Polynomial Features :", poly_score)

# ----------------------------------------------------------
# FINAL FEATURE MATRIX READY FOR ML PIPELINES
# ----------------------------------------------------------
print("\nFinal Feature Shape:", X_train_poly.shape)

print("\nFeature Engineering Completed Successfully!")
# ==========================================================

#TASK--1 THE CATOGORICAL CONVERTER
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#Create sample dataset
data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
}
df = pd.DataFrame(data)

print("Original Data:\n")
print(df)
#Label Encoding for Transmission (Binary)
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

#One-Hot Encoding for Color (Nominal)
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nEncoded Data:\n")
print(df)


#TASK--2 THE LEVELING FIELD
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45, 50, 29],
    "Salary": [25000, 30000, 50000, 70000, 90000, 45000, 60000, 120000, 150000, 52000]
}

df = pd.DataFrame(data)

standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

plt.figure(figsize=(15,4))

plt.subplot(1,3,1)
plt.hist(df["Salary"], bins=5)
plt.title("Original Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
 
plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Standardized Salary (Mean=0, Std=1)")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")

plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"], bins=5)
plt.title("Normalized Salary (0 to 1 Range)")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")

plt.tight_layot()
plt.show()


#TASK--3 THE COMPLEXITY CREATOR
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Create Non-Linear Data
np.random.seed(0)

X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = 3 * X**2 + 2 * X + 5 + np.random.randn(100, 1) * 8   # Quadratic relationship

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Linear Regression (Original Feature)
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

# Step 3: Polynomial Features (degree=2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)

# Step 4: Print Results
print("R² Score (Linear Regression - Original Feature):", r2_linear)
print("R² Score (Linear Regression - Polynomial Features):", r2_poly)
























































