import pandas as pd

# read red and white wine
red_wine = pd.read_csv("./dataset/winequality-red.csv", sep=";")
white_wine = pd.read_csv("./dataset/winequality-white.csv", sep=";")

# convert red and white to json
red_wine_json = red_wine.to_json(orient="records",indent=4)
white_wine_json = white_wine.to_json(orient="records",indent=4)

# craete json red and white wine
with open("./json/winequality-red.json","w") as json_file:
    json_file.write(red_wine_json)

with open("./json/winequality-white.json","w") as json_file:
    json_file.write(white_wine_json)

print("CSV file successfully converted to JSON!")

# print("Red wine data")
# print(red_wine.head())

# print("Red wine info")
# print(red_wine.info())

# print("Red wine description")
# print(red_wine.describe())
