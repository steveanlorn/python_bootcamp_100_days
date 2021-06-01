data = []

"""Read CSV data with readline()"""
# with open("weather_data.csv") as weather_file:
#     weather_file.readline()
#
#     while True:
#         line = weather_file.readline()
#         if not line:
#             break
#
#         split_data = line.split(",")
#         data.append(
#             {
#                 "day": split_data[0],
#                 "temp": split_data[1],
#                 "condition": split_data[2].rstrip(),
#             }
#         )

"""Read CSV data with CSV package"""
# import csv
#
# with open("weather_data.csv") as weather_file:
#     csv_reader = csv.reader(weather_file)
#
#     for reader in csv_reader:
#         if reader[0] == "day":
#             continue
#
#         data.append(
#             {
#                 "day": reader[0],
#                 "temp": reader[1],
#                 "condition": reader[2],
#             }
#         )
#
# print(data)

"""Read CSV data with Pandas package"""
import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()

temp_average = sum(temp_list) / len(temp_list)
print(f"temp average {temp_average}")
print(f"temp average {data['temp'].mean()}")
print(f"Max value: {data['temp'].max()}")

# Get weather data with maximum temp
print(data[data.temp == data.temp.max()])

# Get monday temp and convert it into Fahrenheit
monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32)