# Importing blueprint
import random
from .place import Place

# House class
class House(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Getting place name
		self.name = "HOUSE"
		self.display_name = "House"
		self.description = random.choice((
			"An average house on the city street. It didn't fare so well with the protests and you can enter easily. "
			"At least nobody happens to live here. There's just a living room, a toilet,  a single bedroom, a kitchen "
			"and a dining room.",
			"The windows are broken. The door isn't closed. This house has definitely been abandoned... Not many rooms either. "
			"The couch was very comfortable but there's now a hole that formed. There's a staircase but it collapsed.",
			"Just a regular house. I don't know how, but it looks as if it hasn't been damaged at all yet there's "
			"no-one living there. "
			"It only has one floor and a few rooms: The living room, kitchen, dining hall, two bedrooms, and two toilets.",
			"This house has been so looted there's nothing of importance. But who knows, maybe there's at least something "
			"minimal yet useful..."
		))

