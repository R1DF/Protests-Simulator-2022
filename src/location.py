# Importing all places
from places.hospital import Hospital
from places.parking import ParkingSpot
from places.office import Office
from places.shop import Shop
from places.us import UlkenSharshy
from places.house import House

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

		elif contents_type == "HOUSE":
			self.contents = House(coords)
			
		elif contents_type == "ULKEN_SHARSHY":
			self.contents = UlkenSharshy(coords)

		elif contents_type == "PARKING":
			self.contents = ParkingSpot(coords)

