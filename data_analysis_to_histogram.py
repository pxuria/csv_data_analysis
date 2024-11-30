import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Load the datasets
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Set the feature for the histogram (e.g., 'alcohol')
feature = 'alcohol'

# Set Seaborn style
sns.set(style="whitegrid")

# Histogram for Red Wine
plt.figure(figsize=(8, 6))
sns.histplot(red_wine[feature], kde=True, color='red', bins=20)
plt.title("Histogram of Red Wine Alcohol Content")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.savefig("./histogram/red_wine_histogram.png")  # Save the plot as an image
plt.close()

# Histogram for White Wine
plt.figure(figsize=(8, 6))
sns.histplot(white_wine[feature], kde=True, color='blue', bins=20)
plt.title("Histogram of White Wine Alcohol Content")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.savefig("./histogram/white_wine_histogram.png")  # Save the plot as an image
plt.close()
