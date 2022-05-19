import pandas as pd

# TODO GOAL: Create a CSV file tat prunes out the follow data from the NYC Squirrel Consensus
# TODO 1: Retrieve all data from "Primary Fur Color" column.
s_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_col = s_data["Primary Fur Color"].tolist()

# TODO 2: Get the squirrel count for each of the fur colours.
b_fur = fur_col.count("Black")
c_fur = fur_col.count("Cinnamon")
g_fur = fur_col.count("Gray")

print(fur_col)
print(b_fur)
print(c_fur)
print(g_fur)

#TODO 3: Create a new CSV file with the retrieved data (Fur Color & Number of Squirrels).
sqrl_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [b_fur, c_fur, g_fur]
}

fur_data = pd.DataFrame(sqrl_dict)
fur_data.to_csv("fur_data.csv")

print(sqrl_dict)
print(f"\n{fur_data}")


# Shorter Solution for steps 2
# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
#
# print(gray_squirrel_count)
# print(cinnamon_squirrel_count)
# print(black_squirrel_count)