#Seismic Frequency Analyzer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("day_26_seismicData.csv")

time = data["time"]
amp = data["amplitude"]

dt = time.diff().dropna()
print("Time intervals:", dt.unique())

dt = dt.iloc[0]

fft_result = np.fft.fft(amp)
frequencies = np.fft.fftfreq(len(amp), d=dt)

magnitude = np.abs(fft_result)

dominant_index = np.argmax(magnitude)
dominant_frequency = frequencies[dominant_index]

print("The dominant frequency is:", f"{dominant_frequency:.2f} Hz")

plt.plot(time, amp)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Amplitude VS Time")
plt.show()

plt.plot(frequencies, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Spectrum")
plt.show()