# Importing blueprint
from .place import Place

# Parking Spot class
class ParkingSpot(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Getting place name
		self.name = "PARKING"

