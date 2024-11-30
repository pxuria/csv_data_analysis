import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Use a non-interactive backend
matplotlib.use('Agg')

# Load the datasets
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Select the features to calculate the correlation (e.g., 'alcohol' and 'quality')
feature_x = 'alcohol'
feature_y = 'quality'

# Calculate the correlation coefficient (Pearson's correlation)
correlation_red_wine = red_wine[feature_x].corr(red_wine[feature_y])
correlation_white_wine = white_wine[feature_x].corr(white_wine[feature_y])

# Set Seaborn style
sns.set(style="whitegrid")

# Scatter Plot for Red Wine with Regression Line
plt.figure(figsize=(8, 6))
sns.regplot(x=feature_x, y=feature_y, data=red_wine, scatter_kws={'color': 'red'}, line_kws={'color': 'black'})
plt.title(f"Correlation between {feature_x} and {feature_y} in Red Wine\nCorrelation Coefficient: {correlation_red_wine:.2f}")
plt.xlabel(feature_x)
plt.ylabel(feature_y)
plt.savefig("./correlation/red_wine_correlation.png")  # Save the plot as an image
plt.close()  # Close the figure to free memory

# Scatter Plot for White Wine with Regression Line
plt.figure(figsize=(8, 6))
sns.regplot(x=feature_x, y=feature_y, data=white_wine, scatter_kws={'color': 'blue'}, line_kws={'color': 'black'})
plt.title(f"Correlation between {feature_x} and {feature_y} in White Wine\nCorrelation Coefficient: {correlation_white_wine:.2f}")
plt.xlabel(feature_x)
plt.ylabel(feature_y)
plt.savefig("./correlation/white_wine_correlation.png")  # Save the plot as an image
plt.close()  # Close the figure to free memory

# Print the correlation coefficients
print(f"Red Wine {feature_x} vs {feature_y} Correlation: {correlation_red_wine:.2f}")
print(f"White Wine {feature_x} vs {feature_y} Correlation: {correlation_white_wine:.2f}")
