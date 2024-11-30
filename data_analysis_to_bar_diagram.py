import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt  # Import pyplot explicitly

# Use a non-interactive backend to avoid Tkinter issues
matplotlib.use('Agg')

# Load the CSV data
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Set the style for the plot
sns.set(style="whitegrid")

# Create a barplot for red wine quality distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='quality', data=red_wine, palette='Reds')
plt.title('Distribution of Red Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.savefig('./bar-diagram/red_wine_quality.png')  # Save the plot to a file
print("Red wine quality distribution plot saved as 'red_wine_quality.png'.")

# Create a barplot for white wine quality distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='quality', data=white_wine, palette='Blues')
plt.title('Distribution of White Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.savefig('./bar-diagram/white_wine_quality.png')  # Save the plot to a file
print("White wine quality distribution plot saved as 'white_wine_quality.png'.")
