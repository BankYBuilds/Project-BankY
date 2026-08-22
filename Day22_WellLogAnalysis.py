#WELL LOG ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("well_log.csv")

depth = data["Depth"]
gr = data["Gamma Ray (GR)"]
resistivity = data["Resistivity"]
density = data["Density"]
porosity = data["Porosity"]

max_depth = depth.max()
min_depth = depth.min()
avg_depth = depth.mean()

max_gr = gr.max()
min_gr = gr.min()
avg_gr = gr.mean()

max_resistivity = resistivity.max()
min_resistivity = resistivity.min()
avg_resistivity = resistivity.mean()

max_density = density.max()
min_density = density.min()
avg_density = density.mean()

max_porosity = porosity.max()
min_porosity = porosity.min()
avg_porosity = porosity.mean()

shale_rich = data[data["Gamma Ray (GR)"] > 70]
high_resistivity = data[data["Resistivity"] > 15]
cleaner = data[data["Gamma Ray (GR)"] < 50]


print("=== WELL LOG ANALYSIS ===")

print(f"Depth: Min = {min_depth}, Max = {max_depth}, Average = {avg_depth:.2f}")

print(f"Gamma Ray: Min = {min_gr}, Max = {max_gr}, Average = {avg_gr:.2f}")

print(f"Resistivity: Min = {min_resistivity}, Max = {max_resistivity}, Average = {avg_resistivity:.2f}")

print(f"Density: Min = {min_density}, Max = {max_density}, Average = {avg_density:.2f}")

print(f"Porosity: Min = {min_porosity}, Max = {max_porosity}, Average = {avg_porosity:.2f}")


print("\n=== POSSIBLE SHALE-RICH INTERVALS ===")
print(shale_rich[["Depth", "Gamma Ray (GR)"]])


print("\n=== POSSIBLE CLEANER INTERVALS ===")
print(cleaner[["Depth", "Gamma Ray (GR)"]])


print("\n=== HIGH-RESISTIVITY INTERVALS ===")
print(high_resistivity[["Depth", "Resistivity"]])

plt.plot(gr, depth)
plt.xlabel("Gamma Ray (GR)")
plt.ylabel("Depth")
plt.title("Gamma Ray vs Depth")
plt.gca().invert_yaxis()
plt.show()

plt.plot(resistivity, depth)
plt.xlabel("Resistivity")
plt.ylabel("Depth")
plt.title("Resistivity vs Depth")
plt.gca().invert_yaxis()
plt.show()