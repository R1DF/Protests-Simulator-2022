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
		# Consumables
		self.house_and_office_items = (2, 2, 2, 1, 0)
		self.house_and_office_rng_values = (75, 75, 15, 60, 0)

		self.hospital_items = (1, 1, 1, 0, 2)
		self.hospital_rng_values = (33, 33, 0, 0, 80)

		self.shop_items = (5, 5, 2, 1, 0)
		self.shop_rng_values = (60, 60, 50, 20, 0)

		# Equipment
		self.us_items = (1, 1, 1, 1, 1, 1)
		self.us_rng_values = (60, 40, 20, 60, 40, 20)

	def generate_places(self):
		coords_data = json.load(open(getcwd() + "\\coords.json", "r"))

		# Shops have collections of random coordinates per place.
		self.item_dropper.set_consumables_and_rng(self.shop_items, self.shop_rng_values)
		for shop_coords_pack in coords_data["shops"]:
			coords = choice(shop_coords_pack)
			self.field[coords[1]][coords[0]].determine_contents("SHOP", coords)
			self.item_dropper.randomize_consumables(self.field[coords[1]][coords[0]].contents)

		# Houses and offices have predetermined coordinates, but they're all over the place.
		self.item_dropper.set_consumables_and_rng(self.house_and_office_items, self.house_and_office_rng_values)
		for locations in ["houses", "offices"]:
			for coords in coords_data[locations]:
				self.field[coords[1]][coords[0]].determine_contents(
					"HOUSE" if locations == "houses" else "OFFICE", coords
				)
				self.item_dropper.randomize_consumables(self.field[coords[1]][coords[0]].contents)



		# There is only one hospital.
		coords = coords_data["hospital"]
		self.field[coords[1]][coords[0]].determine_contents("HOSPITAL", coords)
		self.item_dropper.set_consumables_and_rng(self.hospital_items, self.hospital_rng_values)
		self.item_dropper.randomize_consumables(self.field[coords[1]][coords[0]].contents)

		# There's only one parking spot, but its location is randomly picked.
		self.parking_spot_coords = choice(coords_data["parking_spots"])
		self.field[self.parking_spot_coords[1]][self.parking_spot_coords[0]].determine_contents("PARKING", self.parking_spot_coords)

		# The Ulken Sharshy is technically the same place but the code has a clever way to mask it. It's the only place to have weapons and shields.
		self.item_dropper.set_equipment_and_rng(self.us_items, self.us_rng_values)
		for coords in coords_data["ulken_sharshy"]:
			self.field[coords[1]][coords[0]].determine_contents("ULKEN_SHARSHY", coords)
			self.item_dropper.randomize_equipment(self.field[coords[1]][coords[0]].contents)

