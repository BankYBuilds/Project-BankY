# GEOPHYSICAL DATA ANALYZER

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("geophysical_survey_data.csv")

resistivity = data["Resistivity"]
station = data["Station"]
avg_resistivity = data["Resistivity"].mean()
max_resistivity = data["Resistivity"].max()
min_resistivity = data["Resistivity"].min()
highest_resistivity = data.loc[data["Resistivity"].idxmax()]

avg_elevation = data["Elevation"].mean()
high_resistivity = data[data["Resistivity"] > 150]

print(f'The Average Resistivity is: {avg_resistivity}')
print(f"The Highest Resistivity is: {max_resistivity}")
print(f"The Lowest Resistivity is: {min_resistivity}")
print(f"The Average Elevation is: {avg_elevation}")
print(highest_resistivity[["Station", "Resistivity"]])
print(f'The stations with High resistivity are: {high_resistivity}')

plt.bar(station, resistivity)
plt.xlabel("Station")
plt.ylabel("Resistivity")
plt.title("Resistivity by Station")
plt.show()