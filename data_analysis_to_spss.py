import pandas as pd
import pyreadstat

# Load the CSV data
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Rename columns to replace spaces with underscores
red_wine.columns = red_wine.columns.str.replace(' ', '_')
white_wine.columns = white_wine.columns.str.replace(' ', '_')

# Convert Red Wine DataFrame to SPSS .sav format
pyreadstat.write_sav(red_wine, "./spss/red_wine.sav")
pyreadstat.write_sav(white_wine, "./spss/white_wine.sav")
print("Red and White wine data saved as SPSS file!")