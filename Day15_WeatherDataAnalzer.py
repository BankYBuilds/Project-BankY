#WEATHER DATA ANALYZER
import pandas as pd

data = pd.read_csv("weather_data.csv")

avg_rainfall = data['Rainfall'].mean()
avg_temperature = data['Temperature'].mean()
avg_humidity = data['Humidity'].mean()
max_temp = data["Temperature"].max()
min_temp = data['Temperature'].min()
rainy_days = (data["Rainfall"] > 0).sum()
day_maxTemp = data[data["Temperature"] == max_temp]

print(f'The average Rainfall in the dataset is: {avg_rainfall}')
print(f'The average Temperature in the dataset is: {avg_temperature}')
print(f'The average Humidity in the dataset is: {avg_humidity}')
print(f'The Highest Temperature in the dataset is: {max_temp}')
print(f'The Lowest Temperature in the dataset is: {min_temp}')
print(f"Number of rainy days: {rainy_days}")
print(f"The day with the Highest Temperature is: {day_maxTemp}")