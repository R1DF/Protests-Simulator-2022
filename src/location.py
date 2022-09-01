# Importing all places
from house import House
from parking import ParkingSpot
from office import Office
from shop import Shop
from us import UlkenSharshy

# Location class
class Location:
	def __init__(self, coords, location_type=None, ext_arg=None):
		self.location_type = location_type
		self.contents = None

	def determine_contents(self, contents_type, coords):
		if contents_type == "SHOP":
			self.contents = Shop(coords)
			
		elif contents_type == "HOSPITAL":
			self.contents = Hospital(coords)
			
		elif contents_type == "OFFICE":
			self.contents = Office(coords)
			
		elif contents_type == "ULKENSHARSHY":
			self.contents = UlkenSharshy(coords)
			
		elif contents_type == "PARKING":
			self.contents = ParkingSpot(coords)

