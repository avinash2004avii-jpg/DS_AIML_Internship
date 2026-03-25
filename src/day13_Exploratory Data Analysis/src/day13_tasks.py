#TASK--1 THE DISTRIBUTION DEEP DRIVE(UNIVARIATE ANALYSIS)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("housingg.csv")

#numerical column
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness of Price:", skewness)
print("Kurtosis of Price:", kurtosis)

#catogorical column
plt.figure(figsize=(8,5))
sns.countplot(x=df["City"])
plt.title("Count of Houses by City")
plt.xticks(rotation=45)
plt.show()

#TASK--2 THE RELETIONSHIP MAP
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Save as CSV
df.to_csv("car_sales.csv")
print("CSV file created successfully!\n")

# Step 2: Scatter Plot
plt.figure(figsize=(8,5))
sns.scatterplot(x="EngineSize", y="Price", data=df)
plt.title("Engine Size vs Car Price")
plt.xlabel("Engine Size (Liters)")
plt.ylabel("Price (INR)")
plt.show()

# Step 3: Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x="Brand", y="Price", data=df)
plt.title("Price Distribution by Brand")
plt.show()

# Step 4: Observation
print("Observation:")
print("As EngineSize increases, Price seems to increase.")
























# TASK--3 THE PATTERN FINDER


import pandas as pd

data = {
    "Price": [1500,2200,2800,3200,3500,4800,4000,4500,6200,7500,9200,2600],
    "City": ["hospet","bellary","mysuru","hubali","mysuru",
             "hospet","mysuru","mangaluru","hospet","hospet","bellary","mysuru",],
    "SquareFoot": [600,700,800,900,650,1000,850,950,1100,1300,1500,750],
    "Rooms": [1,2,2,3,2,3,3,3,3,4,4,2]
}

df = pd.DataFrame(data)

df.to_csv("housing.csv", index=False)

print("CSV file saved successfully")



















import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('housing.csv')
sns.set(style='whitegrid')

#Correlation
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot =True, cmap='coolwarm')
plt.show()

 
sns.boxplot(df['Price'])
plt.show()
corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)
print("\nSummary statistics:")
print(df.describe())





























