# 1. Simply read the data from the file
# with open("weather_data.csv", "r") as f:
#     data = f.readlines()
# for i in range(0, len(data)):
#     data[i] = data[i][:-1]
# print(data)

# 2. Read the data using the CSV library and recover the temperatures
# import csv
# with open("weather_data.csv", "r") as f:
#     data = csv.reader(f)
#     temperatures = []
#     next(data, None)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

# 3. Same but using Pandas library
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# 4. Calculate the average of the temperatures
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # temperatures = data["temp"].to_list()
# # print(round(sum(temperatures) / len(temperatures), 1))
# print(data["temp"].mean())

# 5. Print the row where the temperature was at the maximum
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data[data.temp == data.temp.max()])

# 6. Get Monday's temperature in Fahrenheit
# import pandas
# data = pandas.read_csv("weather_data.csv")
# data = data[data.day == "Monday"]
# temperature = data.temp * 1.8 + 32
# print(str(temperature[0])+"°F")

# 7. From the squirrel_data_full.csv, create a new DataFrame containing
#    the count of squirrel sorted by data fur type and make it a CSV.
import pandas
data = pandas.read_csv("squirrel_data_full.csv")
furs = data["Primary Fur Color"].to_list()

colour_list = []
for item in furs:
    if item not in colour_list:
        colour_list.append(item)
colour_list = colour_list[1:]

colour_count = [0] * len(colour_list)
for item in furs:
    for colour in colour_list:
        if colour == item:
            colour_count[colour_list.index(colour)] += 1

processed_data = {"Fur Color": colour_list, "Count": colour_count}
processed_data = pandas.DataFrame(processed_data)
processed_data.to_csv("squirrel_data.csv")
