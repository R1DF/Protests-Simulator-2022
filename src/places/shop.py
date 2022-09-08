# Importing blueprint
import random
from .place import Place

# Shop class
class Shop(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Getting place name
		self.name = "SHOP"
		self.display_name = "Shop"
		self.description = random.choice((
			"Pretty much everything has been looted here. Don't hang by for too long.",
			"There's many aisles here. Did I mention to you that they're all empty?",
			"The shop has been very violently broken into. There's nearly nothing left inside, so waste all the time you want.",
			"Barely anything useful left. Ny the way, there's no money in the cash register either, so don't even "
			"think about it."
		))

