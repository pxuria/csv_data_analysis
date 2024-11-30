import sqlite3
import pandas as pd

# Load the CSV data
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("./database/wine_quality.db")
cursor = conn.cursor()

red_wine.to_sql("red_wine", conn, if_exists="replace", index=False)
print("Red wine data added to the database!")

# Convert White Wine Data to SQL
white_wine.to_sql("white_wine", conn, if_exists="replace", index=False)
print("White wine data added to the database!")

# Commit and close the connection
conn.commit()
conn.close()