# Importing blueprint
from place import Place

# House class
class House(Place):
	def __init__(self, coords, master=None):
		Place.__init__(self, coords, master)

