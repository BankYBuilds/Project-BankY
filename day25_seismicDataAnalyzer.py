#SEISMIC DATA ANNALYZER

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('day_25_seismicData.csv')
time = data["Time_s"]
amp = data["Amplitude"]

missing_values = data.isna().sum()
print("\nMissing Values:")
print(missing_values)

max_amplitude = amp.max()
min_amplitude = amp.min()
avg_amplitude = amp.mean()
standardDeviation = amp.std()

threshold = 2 * standardDeviation
high_amplitude = data[abs(data["Amplitude"]) > threshold]

print(f"Maximum amplitude: {max_amplitude}")
print(f"Minimum amplitude: {min_amplitude}")
print(f"Average amplitude: {avg_amplitude}")
print(f"High amplitude data: {high_amplitude}")

plt.plot(time, amp)
plt.title("Seismic Amplitude vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()