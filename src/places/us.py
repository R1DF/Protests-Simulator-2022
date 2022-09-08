# Importing blueprint
import random
from .place import Place

# Ulken Sharshy class
class UlkenSharshy(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Getting place name
		self.name = "ULKEN_SHARSHY"
		self.display_name = "Ulken Sharshy"
		self.article = "the"  # Grammar rules
		self.description = random.choice((
			"A very dangerous place. Lots of shouting, lots of protesting, lots of fire.",
			"People are chanting the anthem in their brave voices. Don't interrupt them and let the flames burn unless "
			"you have a death wish.. ",
			"You hear loud explosion noises as protestors try to intimidate the government. "
			"This is what a revolution feels like.",
			"There are posters with anti-government captions attached as people assemble in groups and yell. "
			"Stay out of their way."
		))

