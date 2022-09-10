# Internal imports
from location import Location
from item_dropper import ItemDropper

# Package imports
import json
from random import choice
from os import getcwd

# Constants for coordinates
coords_data = json.load(open(getcwd() + "\\coords.json", "r"))

# Field class
class Field:
	def __init__(self, player):
		# Initialization
		self.extent_x, self.extent_y = 8, 6
		self.field = []
		self.parking_spot_coords = None  # necessary for game to end
		self.player = player  # for ItemDropper
		self.item_dropper = ItemDropper(self.player)

		# Making field
		self.make_field()
		self.make_item_distributions()
		self.generate_places()

	def make_field(self):
		for column in range(self.extent_y):
			self.field.append([Location((x, column)) for x in range(self.extent_x)])  # Tried using a one-liner but it placed references
			# 2D lists have this order: [column][row]

	def make_item_distributions(self):
		self.house_and_office_items = (  # Weapons and shields spawn differently, only one per random place
			("APPLE", 2),  # the 2 signifies how much of apples can there be
			("BREAD", 2),
			("POTATO", 2),
			("DICE_OF_FATE", 1),
			("MEDKIT", 0)
		)

		self.house_and_office_rng_values = (  # out of 100
			75,
			75,
			15,
			60,
			0
		)

		self.hospital_items = (  # Weapons and shields spawn differently, only one per random place
			("APPLE", 1),  # the 2 signifies how much of apples can there be
			("BREAD", 1),
			("POTATO", 0),
			("DICE_OF_FATE", 0),
			("MEDKIT", 2)
		)

		self.hospital_rng_values = (  # out of 100
			33,
			33,
			0,
			0,
			80
		)

	def generate_places(self):
		coords_data = json.load(open(getcwd() + "\\coords.json", "r"))

		# Shops have collections of random coordinates per place.
		for shop_coords_pack in coords_data["shops"]:
			coords = choice(shop_coords_pack)
			self.field[coords[1]][coords[0]].determine_contents("SHOP", coords)

		# Houses and offices have predetermined coordinates, but they're all over the place.
		self.item_dropper.set_items_and_rng(self.house_and_office_items, self.house_and_office_rng_values)
		for locations in ["houses", "offices"]:
			for coords in coords_data[locations]:
				self.field[coords[1]][coords[0]].determine_contents(
					"HOUSE" if locations == "houses" else "OFFICE", coords
				)
				self.item_dropper.randomize(self.field[coords[1]][coords[0]].contents)



		# There is only one hospital.
		coords = coords_data["hospital"]
		self.field[coords[1]][coords[0]].determine_contents("HOSPITAL", coords)
		self.item_dropper.set_items_and_rng(self.hospital_items, self.hospital_rng_values)
		self.item_dropper.randomize(self.field[coords[1]][coords[0]].contents)

		# There's only one parking spot, but its location is randomly picked.
		self.parking_spot_coords = choice(coords_data["parking_spots"])
		self.field[self.parking_spot_coords[1]][self.parking_spot_coords[0]].determine_contents("PARKING", self.parking_spot_coords)

		# The Ulken Sharshy is technically the same place but the code has a clever way to mask it.
		for coords in coords_data["ulken_sharshy"]:
			self.field[coords[1]][coords[0]].determine_contents("ULKEN_SHARSHY", coords)