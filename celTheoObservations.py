import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

import celTheoData # Includes all the observations and peak data
import celTheoLib as ct

# Show all the observations compared to the expect raw trig FE angle

################################################################################

peaks = celTheoData.peaks.keys()

maxRecordedAngles = [
	max(obs["recordedAngle"] for obs in celTheoData.observations if obs["peak"] == name)
	 for name in peaks]

minCelTheoAngles = [
	min(obs["celTheoAngle"] for obs in celTheoData.observations if obs["peak"] == name)
	 for name in peaks]

maxCelTheoAngles = [
	max(obs["celTheoAngle"] for obs in celTheoData.observations if obs["peak"] == name)
	 for name in peaks]

rawFEAngles = [
	ct.flatGeometricAngle(celTheoData.peaks[name]["distance"], celTheoData.peaks[name]["deltaHeight"])
	for name in peaks
]

fig, ax = plt.subplots(figsize=(16, 9))

# Plot horizontal lines (like candlesticks)
for i, (minC, maxC, rawFE) in enumerate(zip(minCelTheoAngles, maxCelTheoAngles, rawFEAngles)):
	# ax.hlines(y=i, xmin=mnR, xmax=mxR, color="green", linewidth=20)
	ax.hlines(y=i, xmin=minC, xmax=maxC, color="skyblue", linewidth=20)

	ax.plot(rawFE, i, 'x', color='red', label="Raw Flat Earth Trig" if i == 0 else "")

	# Add error labels at each point
	if (rawFE < minC):
		ctError = abs(minC - rawFE) * 60
		plt.text(maxC + 0.05, i, f"{ctError:.1f}'", color='black', fontsize=9, weight='bold')

	if (rawFE > maxC):
		ctError = abs(rawFE - maxC) * 60
		plt.text(rawFE + 0.05, i, f"{ctError:.1f}'", color='black', fontsize=9, weight='bold')


ax.minorticks_on()
ax.grid(True, which='minor', linestyle=':', color='lightgray')

# Format y-axis
ax.set_yticks(range(len(peaks)))
ax.set_yticklabels(peaks)
ax.set_xlabel("Celestial Theodolite Angle")
ax.set_title("Does the Celestial Theodolite give consistent results?")
ax.grid(True, axis='x', linestyle='--', alpha=0.5)

# Apply custom formatter on the X Axis
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(ct.degToDMS))

ax.legend()
plt.show()


