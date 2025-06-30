import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

import celTheoData # Includes all the observations and peak data
import celTheoLib as ct

# Show all the observations compared to the expect raw trig FE angle

################################################################################

peaks = celTheoData.peaks.keys()

minApparentAngles = [
	min(obs["apparentAngle"] for obs in celTheoData.observations if obs["peak"] == name)
	 for name in peaks]

maxApparentAngles = [
	max(obs["apparentAngle"] for obs in celTheoData.observations if obs["peak"] == name)
	 for name in peaks]

globeRefractedAngles = [
	ct.globeRefractedAngle(celTheoData.peaks[name]["distance"], celTheoData.peaks[name]["deltaHeight"])
	for name in peaks
]

fig, ax = plt.subplots(figsize=(16, 9))

# Plot horizontal lines (like candlesticks)
for i, (minG, maxG, globeAngle) in enumerate(zip(minApparentAngles, maxApparentAngles, globeRefractedAngles)):

	ax.hlines(y=i, xmin=minG, xmax=maxG, color="skyblue", linewidth=20)
	ax.plot(globeAngle, i, 'x', color='red', label="Globe Prediction" if i == 0 else "")

	# Add error labels at each point
	if (globeAngle < minG):
		globeError = abs(minG - globeAngle) * 60
		plt.text(maxG + 0.05, i, f"{globeError:.1f}'", color='black', fontsize=9, weight='bold')

	if (globeAngle > maxG):
		globeError = abs(globeAngle - maxG) * 60
		plt.text(globeAngle + 0.05, i, f"{globeError:.1f}'", color='black', fontsize=9, weight='bold')

ax.minorticks_on()
ax.grid(True, which='minor', linestyle=':', color='lightgray')

# Format y-axis
ax.set_yticks(range(len(peaks)))
ax.set_yticklabels(peaks)
ax.set_xlabel(f"Apparent Angle ({celTheoData.HEFFRON_PRESSURE} hPa)")
ax.set_title("Does the Globe give consistent results?")
ax.grid(True, axis='x', linestyle='--', alpha=0.5)

# Apply custom formatter on the X Axis
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(ct.degToDMS))

ax.legend()
plt.show()


