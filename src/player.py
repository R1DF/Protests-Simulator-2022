# Player class
class Player:
	def __init__(self, name, coordinates):
		# Initialization
		self.name = name
		self.x, self.y = coordinates  # The player starts at a randomized location but that's not done here
		self.attack, self.defense = 7, 7  # nasty def keyword forbids me from contracting the names
		self.health = 100
		self.luck = 7 # will make your life ten times harder when you're about to die
		self.inventory = []  # can only hold 2 things at a time

	def get_status(self):
		if self.health >= 75:
			return "healthy"
		elif 50 <= self.health < 75:
			return "vulnerable"
		elif 25 <= self.health < 50:
			return "in trouble"
		elif 0 < self.health < 25:
			return "close to nde"
		else:
			return "dead"
	