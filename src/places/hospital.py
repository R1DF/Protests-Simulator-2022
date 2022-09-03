# Importing blueprint
from .place import Place

# Hospital class
class Hospital(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Getting place name
		self.name = "HOSPITAL"

