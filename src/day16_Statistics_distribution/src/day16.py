#TASK--1 THE SHAPE SHIFTER
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
normal_data = np.random.normal(170, 10, 500)
right_skewed = np.random.exponential(2, 500) 
left_skewed = 100 - np.random.exponential(2, 500)

datasets = {
    "Normal": normal_data,
    "Right-Skewed": right_skewed,
    "Left-Skewed": left_skewed
}

plt.figure(figsize=(15, 4))  # one figure for all plots

for i, (name, data) in enumerate(datasets.items(), 1):
    df = pd.DataFrame({"Value": data})

    mean = df["Value"].mean()
    median = df["Value"].median()

    plt.subplot(1, 3, i)  # 1 row, 3 columns
    sns.histplot(df["Value"], kde=True)
    plt.title(f"{name}\nMean={mean:.2f}, Median={median:.2f}")

    print(f"{name} → Mean: {mean:.2f}, Median: {median:.2f}")

plt.tight_layout()
plt.show()

#TASK--2 THE OUTLAYER DETECTIVE
import numpy as np
import pandas as pd

np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)
data = np.append(data, [150, -20, 200])

df = pd.DataFrame(data, columns=["value"])
mu = df["value"].mean()
sigma = df["value"].std()

print("\nMean (μ):", mu)
print("\nStandard Deviation (σ):", sigma)

df["z_score"] = (df["value"] - mu) / sigma
outliers = df[np.abs(df["z_score"]) > 3]

print("\nStatistical Outliers (|Z| > 3):")
print(outliers)
print("\nTotal Outliers Found:", len(outliers))



#TASK--3 THE MAGIC OF AVERAGES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
original_data = np.random.exponential(scale=2, size=10000)

plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
sns.histplot(original_data, kde=True)
plt.title("Original Data (Right-Skewed)")

sample_means = []
for i in range(1000):
    sample = np.random.choice(original_data, size=30)
    sample_means.append(np.mean(sample))

sample_means = pd.Series(sample_means)
plt.subplot(1,2,2)
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.tight_layout()
plt.show()
print("\nOriginal Data Mean:", np.mean(original_data))
print("\nMean of Sample Means:", np.mean(sample_means))
print("\nStandard Deviation of Sample Means:", np.std(sample_means))





































































