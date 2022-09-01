# Imports
from location import Location
from random import choice

# Constants for coordinates
RAND_PLAYER_COORDS = [(0, 0), (2, 5), (5, 2)]
RAND_SHOPS_COORDS = [
	[(5, 0), (0, 4)],
	[(5, 7), (6, 0)],
	[(0, 7), (6, 5)]
]
RAND_PARKING_COORDS = [(3, 0), (7, 5)]
HOUSES_COORDS = [
	(0, 2),
	(0, 4),
	(3, 3),
	(7, 2),
	(7, 3)
]
HOSPITAL_COORDS = (4, 0)
OFFICE_COORDS = [(1, 5), (4, 5)]
ULKEN_SHARSHY_COORDS = [
	(3, 3),
	(3, 4),
	(4, 3),
	(4, 4)
]

# Field class
class Field:
	def __init__(self):
		# Initialization
		self.extent_x, self.extent_y = 8, 6
		self.field = [
			[],
			[],
			[],
			[],
			[],
			[]
		]

		# Making the field
		for column in range(len(self.field)):
			for x in range(self.extent_x):
				self.field[column].append(Location((x, column)))

