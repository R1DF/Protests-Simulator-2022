# Importing blueprint
from place import Place

# Parking Spot class
class ParkingSpot(Place):
	def __init__(self, coords, master=None):
		Place.__init__(self, coords, master)

