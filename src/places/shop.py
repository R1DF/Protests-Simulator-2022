# Importing blueprint
from .place import Place

# Shop class
class Shop(Place):
	def __init__(self, coords, master=None):
		Place.__init__(self, coords, master)

