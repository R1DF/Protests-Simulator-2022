# Package import
import json
import os
import random

# Internal import
import coltext
from items.item import display_name_to_text
from config_reader import config_data
from enemy import Enemy

# Player class
class Player:
	def __init__(self, name, coordinates):
		# Initialization
		self.name = name
		self.x, self.y = coordinates  # The player starts at a randomized location but that's not done here
		self.attack, self.defense = 7, 7  # nasty def keyword forbids me from contracting the names
		self.equipped_weapon, self.equipped_shield = None, None
		self.health = 100
		self.luck = random.randint(60, 80)
		self.inventory = []  # can only hold 2 things at a time
		self.consumables = []  # extra space, only for food and other stuff
		self.score = 0
		self.moves = 0
		self.is_defending = False
		self.weapon_killed_with = "" # not None

	def attack_enemy(self, enemy: Enemy):
		if random.randint(1, 100) < self.luck and random.randint(1, 10) < 2:
			return "miss"
		else:
			if enemy.defense >= self.attack:
				return "invulnerable"

			if random.randint(1, 100) < self.luck:
				damage_dealt = self.attack - enemy.defense
				did_crit = False
			else:
				damage_dealt = self.attack - enemy.defense + random.randint(5, 15)  # adding crit
				did_crit = True

			enemy.health -= damage_dealt
			return "crit" if did_crit else "success"

	def defend(self):
		if not self.is_defending:
			self.luck += 10
			self.defense += 4
			self.is_defending = True

	def stop_defense(self):
		if self.is_defending:
			self.luck -= 10
			self.defense -= 4
			self.is_defending = False

	def get_moves(self):
		print(f"Moves: {self.moves}")

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
		self.moves += 1

	def get_inventory(self):
		print(coltext.colformat("C#Inventory:~|"))
		if not self.inventory:
			print("There is nothing in your inventory.")
		else:
			for item in self.inventory:
				print(f"{item.display_name}{' (equipped)' if item.equipped else ''}")  # status -> (equipped, not)

	def get_consumables(self):
		print(coltext.colformat("\nC#Consumables:~|"))
		if not self.consumables:
			print("You don't have any consumables.")
		else:
			items_and_amounts = {
				"APPLE": 0,
				"BREAD": 0,
				"POTATO": 0,
				"DICE_OF_FATE": 0,
				"MEDKIT": 0,
				"WATER_BOTTLE": 0
			}

			for item in self.consumables:
				items_and_amounts[item.name] += 1

			for item in items_and_amounts:
				if items_and_amounts[item] != 0:
					print(f"{display_name_to_text[item]} x{items_and_amounts[item]}")

	def get_holdings(self):
		self.get_inventory()
		self.get_consumables()

	def handle_put_down_query(self, place):
		# Showing what the person already has
		self.get_holdings()

		# Handling query
		item = coltext.force_request("\nEnter the item you want to leave and its amount (default is 1) (e.g. apple 2): ").split()
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
					exact_item = self.inventory[inventory_names.index(item_name)]
					if exact_item.equipped:
						coltext.alarm("Unequip it first.")
						return

					place.contents.append(exact_item)
					self.inventory.remove(exact_item)


				# Notifying
				print(f"You left the item{'s' if amount>1 else ''}. Your inventory has been updated.")
			else:
				coltext.alarm("Bold of you to assume you have that many.")
		else:
			coltext.alarm("You don't have anything like that.")

	def handle_equip_query(self):
		if not self.inventory:
			coltext.alarm("There's nothing you can equip. Search more and you'll find some...")
		else:
			inventory_names = [x.display_name.upper() for x in self.inventory]
			self.get_inventory()

			query = coltext.force_request("\nEnter the name of the object you'd like to equip (e.g. \"dagger\"): ").upper()
			try:
				item = self.inventory[inventory_names.index(query)]

			except ValueError:
				coltext.alarm("I don't know about such a thing.")
				return

			if item.equipped:
				coltext.alarm("You already equipped it, don't worry.\n")
			else:
				item.equip()
				print("Equipped. You feel stronger now.\n")

	def handle_unequip_query(self):
		if not self.inventory:
			coltext.alarm("You don't have anything to unequip. Chill.")
		else:
			inventory_names = [x.display_name.upper() for x in self.inventory]
			print(coltext.colformat("Your C#inventory~|:"))
			for item in self.inventory:
				print(f"{item.display_name}{' (already equipped)' if item.equipped else ''}")

			query = coltext.force_request("\nEnter the name of the object you'd like to unequip (e.g. \"wooden shield\"): ").upper()
			try:
				item = self.inventory[inventory_names.index(query)]
			except ValueError:
				coltext.alarm("I don't know about such thing.")
				return

			if not item.equipped:
				coltext.alarm("It wasn't equipped in the first place.\n")
			else:
				item.unequip()
				print("Unequipped. Whether this was a good idea or not, only you can decide.\n")

	def handle_use_query(self):
		consumables_names = [x.name for x in self.consumables]
		if self.consumables:
			print(coltext.colformat("Your C#consumables~|:"))

			items_and_amounts = {
				"APPLE": 0,
				"BREAD": 0,
				"POTATO": 0,
				"DICE_OF_FATE": 0,
				"MEDKIT": 0,
				"WATER_BOTTLE": 0
			}

			for item in self.consumables:
				items_and_amounts[item.name] += 1

			for item in items_and_amounts:
				if items_and_amounts[item] != 0:
					print(f"{display_name_to_text[item]} x{items_and_amounts[item]}\n{config_data['descriptions'][item]}\n")

			item = coltext.force_request("\nEnter the item you'd like to use (e.g. \"medkit\"): ").strip().upper().replace(" ", "_")
			if item in items_and_amounts:
				exact_item = self.consumables[consumables_names.index(item)]
				exact_item.use()
			else:
				coltext.alarm("You don't have that.")
		else:
			coltext.alarm("You have nothing to use.")

	def has_bottle(self):
		contents = [x.name for x in self.consumables]
		if "WATER_BOTTLE" in contents:
			return True
		return False

	def get_cause_of_death(self):
		try:
			self.weapon_killed_with = self.weapon_killed_with.name
		except AttributeError:
			self.weapon_killed_with = None

		match self.weapon_killed_with:
			case "DAGGER":
				return "Stabbed with a dagger."
			case "WOODEN_BAT":
				return "Clubbed with a bat."
			case "GUN":
				return "Shot with a gun."
			case None:
				return "KO'd to death."

	@staticmethod
	def make_random_coords():
		return random.choice(json.load(open(os.getcwd() + "\\coords.json", "r"))["player"])

