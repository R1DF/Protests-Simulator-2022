"""
This class exists as a parent class for every other location type. Do not confuse it with the Location class, for that's the object that contains a place while the Place class serves as a blueprint for the places inside the Location object.
"""
# Internal imports
import coltext
from items.water_bottle import WaterBottle

# Place blueprint
class Place:
	def __init__(self, coords, master=None):
		# Initialization
		self.master = master
		self.location_x, self.location_y = coords
		self.name = None
		self.display_name = None
		self.contents = []
		self.description = ""
		self.has_randomized = False

	def disclose(self):
		coltext.announce(self.display_name)
		print(self.description)

	def randomize_contents(self):
		pass

	def make_decisive(self):
		self.contents.append(WaterBottle())
