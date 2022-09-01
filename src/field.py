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

		# Defining field locations
		## Shops
		for i in range(len(RAND_SHOPS_COORDS)):
			selected_coords = choice(RAND_SHOPS_COORDS[i])
			print(i, selected_coords)
			self.field[selected_coords[0]][selected_coords[1]].determine_contents("SHOP", selected_coords)

		## Houses
		for i in range(len(HOUSES_COORDS)):
			selected_coords = HOUSES_COORDS[i]
			self.field[selected_coords[0]][selected_coords[1]].determine_contents("HOUSE", selected_coords)

		## Offices
		for i in range(len(OFFICE_COORDS)):
			selected_coords = OFFICE_COORDS[i]
			self.field[selected_coords[0]][selected_coords[1]].determine_contents("OFFICE", selected_coords)

		## Parking spot
		parking_spot_coords = choice(RAND_PARKING_COORDS)
		self.field[parking_spot_coords[0]][parking_spot_coords[1]].determine_contents("PARKING", parking_spot_coords)

		## Hospital
		self.field[HOSPITAL_COORDS[0]][HOSPITAL_COORDS[1]].determine_contents("HOSPITAL", HOSPITAL_COORDS)

