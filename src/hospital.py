# Importing blueprint
from place import Place

# Hospital class
class Hospital(Place):
	def __init__(self, coords, master=None):
		Place.__init__(self, coords, master)

