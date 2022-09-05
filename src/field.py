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
		self.parking_spot_coords = None  # necessary for game to end

		# Making field
		self.make_field()
		self.generate_places()

	def make_field(self):
		for column in range(self.extent_y):
			self.field.append([Location((x, column)) for x in range(self.extent_x)])  # Tried using a one-liner but it placed references
			# 2D lists have this order: [column][row]

	def generate_places(self):
		coords_data = json.load(open(getcwd() + "\\coords.json", "r"))

		# Shops have collections of random coordinates per place.
		for shop_coords_pack in coords_data["shops"]:
			coords = choice(shop_coords_pack)
			self.field[coords[1]][coords[0]].determine_contents("SHOP", coords)

		# Houses and offices have predetermined coordinates, but they're all over the place.
		for locations in ["houses", "offices"]:
			for coords in coords_data[locations]:
				self.field[coords[1]][coords[0]].determine_contents(
					"HOUSE" if locations == "houses" else "OFFICE", coords
				)

		# There is only one hospital.
		coords = coords_data["hospital"]
		self.field[coords[1]][coords[0]].determine_contents("HOSPITAL", coords)

		# There's only one parking spot, but its location is randomly picked.
		self.parking_spot_coords = choice(coords_data["parking_spots"])
		self.field[self.parking_spot_coords[1]][self.parking_spot_coords[0]].determine_contents("PARKING", self.parking_spot_coords)

		# The Ulken Sharshy is technically the same place but the code has a clever way to mask it.
		for coords in coords_data["ulken_sharshy"]:
			self.field[coords[1]][coords[0]].determine_contents("ULKEN_SHARSHY", coords)