import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Use a non-interactive backend
matplotlib.use('Agg')

# Load the datasets
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Set the feature for the scatter plot (e.g., 'alcohol')
feature = 'alcohol'

# Set Seaborn style
sns.set(style="whitegrid")

# Scatter plot for Red Wine
plt.figure(figsize=(8, 6))
sns.scatterplot(x=red_wine.index, y=red_wine[feature], color='red', alpha=0.6)
plt.title("Scatter Plot of Red Wine Alcohol Content")
plt.xlabel("Index")
plt.ylabel("Alcohol")
plt.savefig("./scatter/red_wine_scatter_plot.png")  # Save the plot as an image
plt.close()  # Close the figure to free memory

# Scatter plot for White Wine
plt.figure(figsize=(8, 6))
sns.scatterplot(x=white_wine.index, y=white_wine[feature], color='blue', alpha=0.6)
plt.title("Scatter Plot of White Wine Alcohol Content")
plt.xlabel("Index")
plt.ylabel("Alcohol")
plt.savefig("./scatter/white_wine_scatter_plot.png")  # Save the plot as an image
plt.close()  # Close the figure to free memory
