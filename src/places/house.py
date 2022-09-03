# Importing blueprint
from .place import Place

# House class
class House(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Getting place name
		self.name = "HOUSE"

