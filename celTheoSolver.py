import math
import numpy as np
import matplotlib.pyplot as plt

import celTheoData # Includes all the observations and peak data
import celTheoLib as ct

# At what delta height does the celTheo value match the raw FE angle?

################################################################################

# At what delta height does the celTheo value match the raw FE angle?
distanceSpace = np.linspace(10000, 140000, 100) # X axis 
dHeightSpace = np.linspace(0, 5000, 100) # Y axis

dataGrid = np.zeros((len(distanceSpace), len(dHeightSpace)))

for dHeightIdx in range(len(dHeightSpace)):
	for distanceIdx in range(len(distanceSpace)):

		dHeight = dHeightSpace[dHeightIdx]
		distance = distanceSpace[distanceIdx]

		rawFE = ct.flatGeometricAngle(distance, dHeight)

		celTheo = ct.celTheoAngle(distance, dHeight)
		
		dataGrid[dHeightIdx][distanceIdx] = abs(rawFE - celTheo) * 60

plt.figure(figsize=(16, 9)) # inches
plt.imshow(dataGrid, extent=[distanceSpace.min(), distanceSpace.max(),
		dHeightSpace.min(), dHeightSpace.max()],
		origin='lower', aspect='auto', cmap='inferno_r')

plt.colorbar(label='Error (in arc minutes)')
plt.xlabel('Distance (m)')
plt.ylabel('Delta Height (m)')
plt.title('The "Sweet Spot" for Distance and Height')

# Now overlay the actual distances and delta heights
peakDistances = [pk["distance"] for pk in celTheoData.peaks.values()]
peakdHeights = [pk["deltaHeight"] for pk in celTheoData.peaks.values()]
peakNames = [pk["name"] for pk in celTheoData.peaks.values()]

plt.scatter(peakDistances, peakdHeights, color='red', s=50, marker='x', label='Peaks')

# Add labels at each point
for idx in range(len(peakDistances)):
	plt.text(peakDistances[idx] + 0.25, peakdHeights[idx] + 0.25,  # small offset to avoid overlap
			peakNames[idx], color='black', fontsize=9, weight='bold')

plt.show()
