import math
import celTheoData

################################################################################

def degToDMS(angle, pos):
	deg = int(angle)
	minutes = int((angle - deg) * 60)
	return f"{deg}°{minutes:02d}′"

################################################################################

def flatGeometricAngle(distance, dHeight):

	return math.degrees(math.atan(dHeight / distance))

################################################################################

def globeGeometricAngle(distance, dHeight):

	globeDrop = distance**2 / (2 * celTheoData.EARTH_RADIUS)
	return math.degrees(math.atan((dHeight - globeDrop) / distance))

################################################################################

def globeRefractedAngle(distance, dHeight):

	rawAngle = globeGeometricAngle(distance, dHeight)

	# According to wiki, it's around 1 degree every 1500 km.
	# That equates to 2.4"/km.
	refrCorrection = (2.4 / 3600) * (distance / 1000)

	return rawAngle + refrCorrection

################################################################################

def pressureTempCorrection(pressure, temp):

	return pressure / 1010 * 283 / (273 + temp) / 60

################################################################################

def bennettRefraction(observedAngle):

	ptCorr = pressureTempCorrection(celTheoData.HEFFRON_PRESSURE, 15) # Hardcoded for Heffron's position

	return ptCorr * 1.0 / math.tan((observedAngle + 7.31 / (observedAngle + 4.4)) * math.pi / 180) + 0.0013515

################################################################################

def celTheoAngle(distance, dHeight):

	# Reverse engineer the Celestial Theodolite Angle from the fact
	# That the earth is a globe, and we have an atmosphere ;)

	# Globe Predicted Angle for this observation
	globeAngle = globeRefractedAngle(distance, dHeight)
	
	# Since this value is ALSO the apparent angle at which the star
	# was occulted, lets remove the astronomical refraction component
	astroRefraction = bennettRefraction(globeAngle)

	# Now we can work out what the geometric angle for the star is
	geometricStarAngle = globeAngle - astroRefraction

	# Now move closer, and adjust the angle by 1 degree every 111,111 m
	celTheoAngle = geometricStarAngle + (distance / celTheoData.METRES_PER_DEGREE)

	return celTheoAngle

################################################################################
