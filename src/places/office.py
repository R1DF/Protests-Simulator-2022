# Importing blueprint
from .place import Place

# Office class
class Office(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Getting place name
		self.name = "OFFICE"

