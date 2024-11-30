import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for rendering plots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load the datasets
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Select a feature to analyze (e.g., 'alcohol')
feature = 'alcohol'

# Quantile-Quantile Plot for Red Wine
plt.figure(figsize=(8, 6))
stats.probplot(red_wine[feature], dist="norm", plot=plt)
plt.title("Q-Q Plot for Red Wine Alcohol Content")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.savefig("./quantile-plot/red_wine_qq_plot.png")  # Save the plot as an image
plt.close()

# Quantile-Quantile Plot for White Wine
plt.figure(figsize=(8, 6))
stats.probplot(white_wine[feature], dist="norm", plot=plt)
plt.title("Q-Q Plot for White Wine Alcohol Content")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.savefig("./quantile-plot/white_wine_qq_plot.png")  # Save the plot as an image
plt.close()
