import celTheoData

################################################################################

def checkAtmosphere(expected, fd):

	print(f"// Checking atmosphere", file=fd)
	print(f"if (LandscapeMgr.getFlagAtmosphere() != {expected}) {{", file=fd)
	print(f"\tcore.debug(\"Atmosphere setting (F4) is wrong, expected: {expected}\")", file=fd)
	print(f"\tquit()", file=fd)
	print(f"}}", file=fd)
	print("", file=fd)

	return

################################################################################

def pauseClock(fd):

	print(f"// Pause the clock", file=fd)
	print(f"core.setTimeRate(0)", file=fd)
	print("", file=fd)

	return

################################################################################

def resetOutput(fd):

	print(f"// Clearing the output", file=fd)
	print(f"core.resetOutput()", file=fd)
	print("", file=fd)

	return

################################################################################

# Moves the observer to the specified peak, sets the specified time, and records
# the GEOMETRIC altitude

f = open("celTheo.ssc", "w")

print("// Celestial Theodolite Angles from Stellarium", file=f)
print("", file=f)

checkAtmosphere("false", f)
pauseClock(f)
resetOutput(f)

# Now loop through the observation table
currentPeak = None
for obs in celTheoData.observations:

	if (obs["peak"] != currentPeak):
		# We have to move!
		pkData = celTheoData.peaks[obs["peak"]]
		print(f"core.setObserverLocation({pkData["lon"]}, {pkData["lat"]}, {pkData["elevation"]}, \"{pkData["name"]}\", \"Earth\")", file=f)
		print(f"core.wait(0.5)", file=f) # Give the UI time to catch up
		print("", file=f)
		currentPeak = obs["peak"]

	# Set the observation time
	print(f"core.setDate(\"{obs["timestamp"]}\", spec=\"utc\")", file=f)
	print("core.wait(0.25)", file=f)
	print(f"core.output(\"{obs["timestamp"]}\" + \",\" + core.getObjectInfo(\"{obs["star"]}\")[\"altitude-geometric\"])", file=f)
	print("core.wait(0.25)", file=f)
	print("", file=f)

print("core.saveOutputAs(\"celTheo.csv\")", file=f)

f.close()

################################################################################

# Now run Stellarium script to get the observed altitude FROM the observer, WITH an atmosphere (793 hPa)
g = open("globeApparent.ssc", "w")

print("// Apparent Angles from Stellarium", file=g)
print("", file=g)

checkAtmosphere("true", g)
pauseClock(g)
resetOutput(g)

# Move the observer to Heffron's House
observer = celTheoData.observer
print(f"core.setObserverLocation({observer["lon"]}, {observer["lat"]}, {observer["elevation"]}, \"Heffron\", \"Earth\")", file=g)
print(f"core.wait(0.5)", file=g) # Give the UI time to catch up
print("", file=g)

for obs in celTheoData.observations:

	# Set the observation time
	print(f"core.setDate(\"{obs["timestamp"]}\", spec=\"utc\")", file=g)
	print("core.wait(0.25)", file=g)
	print(f"core.output(\"{obs["timestamp"]}\" + \",\" + core.getObjectInfo(\"{obs["star"]}\")[\"altitude\"])", file=g)
	print("core.wait(0.25)", file=g)
	print("", file=g)

print("core.saveOutputAs(\"globeApparent.csv\")", file=g)

g.close()

################################################################################
