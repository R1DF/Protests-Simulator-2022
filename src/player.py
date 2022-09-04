# Imports for coords randomization
import json
import os
import random

# Player class
class Player:
	def __init__(self, name, coordinates):
		# Initialization
		self.name = name
		self.x, self.y = coordinates  # The player starts at a randomized location but that's not done here
		self.attack, self.defense = 7, 7  # nasty def keyword forbids me from contracting the names
		self.health = 100
		self.luck = 7  # will make your life ten times harder when you're about to die
		self.inventory = []  # can only hold 2 things at a time
		self.score = 0

	def get_status(self):
		if self.health >= 75:
			return "healthy"
		elif 50 <= self.health < 75:
			return "vulnerable"
		elif 25 <= self.health < 50:
			return "in trouble"
		elif 0 < self.health < 25:
			return "close to nde"
		else:
			return "dead"

	def check_movement(self, direction):
		match direction:
			case "e":
				return self.x != 0

			case "w":
				return self.x != 7

			case "n":
				return self.y != 0

			case "s":
				return self.y != 5

			case _:
				return self.check_movement(direction[0]) and self.check_movement(direction[1])

		# if direction == "e":
		# 	return self.x != 0
		# elif direction == "w":
		# 	return self.x != 7
		# elif direction == "n":
		# 	return self.y != 0
		# elif direction == "s":
		# 	return self.y != 5
		# elif len(direction) == 2:  # NE, NW, SE, SW
		# 	return self.check_movement(direction[0]) and self.check_movement(direction[1])

	def move(self, direction):
		for direction in direction:
			match direction:
				case "e":
					self.x -= 1
				case "w":
					self.x += 1
				case "n":
					self.y -= 1
				case "s":
					self.y += 1

	@staticmethod
	def make_random_coords():
		return random.choice(json.load(open(os.getcwd() + "\\coords.json", "r"))["player"])

	