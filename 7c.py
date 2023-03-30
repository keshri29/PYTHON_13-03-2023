 # experiment number 2c to find Area of a Sector

def AreaSector(radius, angle):
	pi = 22 / 7
	if angle >= 360:
		print("Angle not possible")
		return
	else:
		sector = (pi * radius ** 2) * (angle / 360)
		print(sector)
		return
radius = 9
angle = 60
AreaSector(radius, angle)

