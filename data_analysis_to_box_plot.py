import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")  # Use the Agg backend for non-GUI rendering
import matplotlib.pyplot as plt

# Load the CSV data
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Set the style for the plot
sns.set(style="whitegrid")

# Create a box plot for alcohol content in red wine
plt.figure(figsize=(8, 6))
sns.boxplot(x='quality', y='alcohol', data=red_wine, palette='Reds')
plt.title('Box Plot of Alcohol Content in Red Wine by Quality')
plt.xlabel('Quality')
plt.ylabel('Alcohol (%)')
plt.savefig('./box-plot/red_wine_alcohol_boxplot.png')
print("Red wine alcohol box plot saved as 'red_wine_alcohol_boxplot.png'.")

# Create a box plot for alcohol content in white wine
plt.figure(figsize=(8, 6))
sns.boxplot(x='quality', y='alcohol', data=white_wine, palette='Blues')
plt.title('Box Plot of Alcohol Content in White Wine by Quality')
plt.xlabel('Quality')
plt.ylabel('Alcohol (%)')
plt.savefig('./box-plot/white_wine_alcohol_boxplot.png')
print("White wine alcohol box plot saved as 'white_wine_alcohol_boxplot.png'.")
