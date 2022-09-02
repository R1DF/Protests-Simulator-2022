# Imports
import json
from location import Location
from random import choice
from os import getcwd

# Constants for coordinates
coords_data = json.load(open(getcwd() + "\\coords.json", "r"))

# Field class
class Field:
	def __init__(self):
		# Initialization
		self.extent_x, self.extent_y = 8, 6
		self.field = []

		# Making field
		self.make_field()
		self.generate_places()

	def make_field(self):
		for column in range(self.extent_y):
			self.field.append([Location((x, column)) for x in range(self.extent_x)])  # Tried using a one-liner but it placed references
			# 2D lists have this order: [column][row]

	def generate_places(self):
		pass
