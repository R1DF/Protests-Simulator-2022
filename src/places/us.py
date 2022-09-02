# Importing blueprint
from .place import Place

# Ulken Sharshy class
class UlkenSharshy(Place):
	def __init__(self, coords, master=None):
		Place.__init__(self, coords, master)

