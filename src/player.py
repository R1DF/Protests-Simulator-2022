# Imports for coords randomization
import json
import os
import random
import coltext
from items.item import display_name_to_text

# Player class
class Player:
	def __init__(self, name, coordinates):
		# Initialization
		self.name = name
		self.x, self.y = coordinates  # The player starts at a randomized location but that's not done here
		self.attack, self.defense = 7, 7  # nasty def keyword forbids me from contracting the names
		self.health = 100
		self.luck = 80  # will make your life ten times harder when you're about to die
		self.inventory = []  # can only hold 2 things at a time
		self.consumables = []  # extra space, only for food and other stuff
		self.score = 0

	def get_status(self):
		if self.health >= 75:
			return "healthy"
		elif 50 <= self.health < 75:
			return "vulnerable"
		elif 25 <= self.health < 50:
			return "facing trouble"
		elif 0 < self.health < 25:
			return "close to nde"
		else:
			return "dead"

	def check_movement(self, direction):
		match direction:
			case "e":
				return self.x != 7
			case "w":
				return self.x != 0
			case "n":
				return self.y != 0
			case "s":
				return self.y != 5
			case _:
				return self.check_movement(direction[0]) and self.check_movement(direction[1])

	def move(self, direction):
		for direction in direction:
			match direction:
				case "e":
					self.x += 1
				case "w":
					self.x -= 1
				case "n":
					self.y -= 1
				case "s":
					self.y += 1

	def get_holdings(self):
		# Weapons and shields
		print(coltext.colformat("C#Inventory:~|"))
		if not self.inventory:
			print("There is nothing in your inventory.")
		else:
			for item in self.inventory:
				print(f"{item.name}f{' (equipped)' if item.equipped else ''}")  # status -> (equipped, not)

		# Consumables
		print(coltext.colformat("\nC#Consumables:~|"))
		if not self.consumables:
			print("You don't have any consumables.")
		else:
			items_and_amounts = {
				"APPLE": 0,
				"BREAD": 0,
				"POTATO": 0,
				"DICE_OF_FATE": 0,
				"MEDKIT": 0
			}

			for item in self.consumables:
				items_and_amounts[item.name] += 1

			for item in items_and_amounts:
				if items_and_amounts[item] != 0:
					print(f"{display_name_to_text[item]} x{items_and_amounts[item]}")

	def handle_put_down_query(self, place):
		# Showing what the person already has
		self.get_holdings()

		# Handling query
		item = coltext.force_request("\nEnter the item you want to leave and its amount (default is 1) (e.g. water 2): ").split()
		inventory_names = [x.display_name.lower() for x in self.inventory]
		consumables_names = [x.display_name.lower() for x in self.consumables]
		holdings = inventory_names + consumables_names

		# Getting item and amount from input
		if item[-1].isnumeric():
			amount = int(item[-1])
			item_name = " ".join(item[:-1])

		else:
			amount = 1
			item_name = " ".join(item)

		# Checking if item exists
		if item_name.lower() in holdings:
			if holdings.count(item_name.lower()) >= amount:
				if item_name in consumables_names:
					for item_object in range(amount):
						exact_item = self.consumables[consumables_names.index(item_name)]
						place.contents.append(exact_item)
						self.consumables.remove(exact_item)

				else:
					for item_object in range(amount):
						exact_item = self.inventory[inventory_names.index(item_name)]
						place.contents.append(exact_item)
						self.consumables.remove(exact_item)

				# Notifying
				print(f"You left the item{'s' if amount>1 else ''}. Your inventory has been updated.")
			else:
				coltext.alarm("Bold of you to assume you have that many.")
		else:
			coltext.alarm("You don't have anything like that.")

	@staticmethod
	def make_random_coords():
		return random.choice(json.load(open(os.getcwd() + "\\coords.json", "r"))["player"])

