#PRODUCTION DATA ANALYZER

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("day_24_production_data.csv")

date = data["Date"]
oil = data["Oil (bbl)"]
gas = data["Gas (Mcf)"]
water = data["Water (bbl)"]

missing_values = data.isna().sum()
print("\nMissing Values:")
print(missing_values)


total_oil_production = oil.sum()
average_oil_production = oil.mean()
maximum_oil_production = oil.max()
total_gas_production = gas.sum()
average_water_production = water.mean()
average_gas_production = gas.mean()

day_maxOil = data.loc[data["Oil (bbl)"] == maximum_oil_production, "Date"].iloc[0]

high_threshold = 850
high_threshold_count = (oil > high_threshold).sum()


print("\nProduction Statistics:")
print("Total Oil Production:", total_oil_production, "bbl")
print("Average Oil Production:", f"{average_oil_production:.2f}", "bbl/day")
print("Maximum Oil Production:", maximum_oil_production, "bbl")
print("Total Gas Production:", total_gas_production, "Mcf")
print("Average Gas Production:", f"{average_gas_production:.2f}", "Mcf/day")
print("Average Water Production:", f"{average_water_production:.2f}", "bbl/day")

print("\nProduction Findings:")
print("Day of Maximum Oil Production:", day_maxOil)
print("Days Above 850 bbl:", high_threshold_count)

plt.plot(date, oil)
plt.xlabel("Date")
plt.ylabel("Oil (bbl)")
plt.title("Oil Production Trend")
plt.xticks(rotation=45)
plt.show()