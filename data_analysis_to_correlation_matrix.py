import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Use a non-interactive backend
matplotlib.use('Agg')

# Load the datasets
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Calculate the correlation matrix for red wine and white wine
correlation_red_wine = red_wine.corr()
correlation_white_wine = white_wine.corr()

# Set Seaborn style
sns.set(style="whitegrid")

# Plot the correlation matrix for Red Wine
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_red_wine, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title("Correlation Matrix of Red Wine Features")
plt.savefig("./correlation-matrix/red_wine_correlation_matrix.png")  # Save the plot as an image
plt.close()  # Close the figure to free memory

# Plot the correlation matrix for White Wine
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_white_wine, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title("Correlation Matrix of White Wine Features")
plt.savefig("./correlation-matrix/white_wine_correlation_matrix.png")  # Save the plot as an image
plt.close()  # Close the figure to free memory
