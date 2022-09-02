# Importing blueprint
from .place import Place

# Office class
class Office(Place):
	def __init__(self, coords, master=None):
		Place.__init__(self, coords, master)

