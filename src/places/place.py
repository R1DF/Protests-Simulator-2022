"""
This class exists as a parent class for every other location type. Do not confuse it with the Location class, for that's the object that contains a place while the Place class serves as a blueprint for the places inside the Location object.
"""
# Internal imports
import coltext
import random
from items.item import Item, display_name_to_text
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
		pass  # Has to be individually defined

	def disclose(self):
		coltext.announce(self.display_name)
		print(self.description)

	def show_contents(self):
		if self.contents:  # PyCharm why
			items_and_amounts = {
				"APPLE": 0,
				"BREAD": 0,
				"POTATO": 0,
				"DICE_OF_FATE": 0
			}

			for item in self.contents:
				items_and_amounts[item.name] += 1

			print(coltext.colformat(f"Contents of C#{self.name.lower()}~|:"))
			for item_name in items_and_amounts:
				if items_and_amounts[item_name] != 0:
					print(f"{display_name_to_text[item_name]} x{items_and_amounts[item_name]}")

		else:
			print(coltext.colformat(f"You're in {self.article} C#{self.display_name.lower()}~|, but there's nothing here."))

	def handle_take_query(self, player):
		item = coltext.force_request("Enter the item you want to take and its amount (default is 1) (e.g. water 2): ").split()

		contents_names = [x.display_name.lower() for x in self.contents]
		# Getting item and amount from input
		if item[-1].isnumeric():
			amount = int(item[-1])
			item_name = " ".join(item[:-1])

		else:
			amount = 1
			item_name = " ".join(item)

		# Checking if item exists
		if item_name.lower() in contents_names:
			if contents_names.count(item_name.lower()) >= amount:
				# Taking the objects and placing them in the player's consumables bag
				for item_object in range(amount):
					exact_item = self.contents[contents_names.index(item_name)]
					if exact_item.item_type == "consumable":  # checking if consumable
						player.consumables.append(exact_item)
					else:
						player.inventory.append(exact_item)  # otherwise
					self.contents.remove(exact_item)

				# Notifying
				print("Taken. Your inventory has been updated.")
			else:
				coltext.alarm("That's way too much...")
		else:
			coltext.alarm("You can't pick up something that isn't here in the first place.")


	# def make_decisive(self): NOT YET
	# 	self.contents.append(WaterBottle())
