"""
This class exists as a parent class for every other location type. Do not confuse it with the Location class, for that's the object that contains a place while the Place class serves as a blueprint for the places inside the Location object.
"""
# Internal imports
import coltext
import random
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
		self.description = None
		self.descriptions = None
		self.has_randomized = False
		self.article = "a"  # I hate grammar

		# Function calling
		self.determine_description()

	def determine_description(self):
		pass # Has to be individually defined

	def disclose(self):
		coltext.announce(self.display_name)
		print(self.description)

	def show_contents(self):
		if self.contents:  # PyCharm why
			print(coltext.colformat(f"Contents of C#{self.name.lower()}~|:"))
			for element in self.contents:
				print(element.display_name)
		else:
			print(coltext.colformat(f"You're in {self.article} C#{self.name.lower()}~|, but there's nothing here."))

	# def make_decisive(self): NOT YET
	# 	self.contents.append(WaterBottle())
