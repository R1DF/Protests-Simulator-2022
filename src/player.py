# Player class
class Player:
	def __init__(self, name, coordinates):
		# Mandatory location
		self.name = name
		self.x, self.y = coordinates # The player starts at a randomized location
		