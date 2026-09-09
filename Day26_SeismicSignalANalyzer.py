#Seismic Signal Analyzer

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("day_26_seismicData.csv")

missing_values = data.isnull().sum()
print("\nMissing values:")
print(missing_values)

time = data["time"]
amp = data["amplitude"]

max_amplitude = amp.max()
min_amplitude = amp.min()
avg_amplitude = amp.mean()
standardDeviation = amp.std()
threshold = standardDeviation * 2
rms = np.sqrt(np.mean(amp ** 2))

high_amplitude = data[abs(data["amplitude"]) > threshold]

time_high_amplitude = data.loc[amp == max_amplitude, "time"].iloc[0]

print("The Average amplitude is:", f"{avg_amplitude:.2f}")
print("The Lowest amplitude is:", min_amplitude)
print("The Highest amplitude is:", max_amplitude)
print("Time of Highest amplitude:", time_high_amplitude)
print("The RMS is:", f'{rms:.2f}')

time_outliers = high_amplitude["time"]
amp_outliers = high_amplitude["amplitude"]


plt.plot(time, amp, label="Seismic waveform")

plt.scatter(
    time_outliers,
    amp_outliers,
    marker="X",
    color = "red",
    label="High-amplitude events"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Seismic Waveform with High-Amplitude Events")
plt.legend()
plt.show()