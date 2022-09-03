# Importing blueprint
from .place import Place

# Ulken Sharshy class
class UlkenSharshy(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Getting place name
		self.name = "ULKEN_SHARSHY"

