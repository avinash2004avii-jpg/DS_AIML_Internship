import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = [12, 7, 3, 15, 10, 18, 5, 8, 20, 11]

# Create a boxplot
sns.boxplot(data=data)

# Add title
plt.title("Boxplot Example with Seaborn")

# Show the plot
plt.show()