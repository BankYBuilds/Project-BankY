#TEMPERATURE DATA VISUALIZER

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperatures = [28, 30, 29, 31, 27]

plt.bar ( days, temperatures, marker = "o")
plt.xlabel("Days")
plt.ylabel("Temperatures")
plt.title("Temperature chart")

plt.show()