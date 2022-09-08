# Importing blueprint
import random
from .place import Place

# Office class
class Office(Place):
	def __init__(self, coords, master=None):
		# Calling constructor
		Place.__init__(self, coords, master)

		# Individual attribtues
		self.name = "OFFICE"
		self.display_name = "Office"
		self.article = "an"  # Grammar rules
		self.description = random.choice((
			"The fridge is open and there's little edible left. The mug is filled with a dark-ish liquid and the table "
			"is covered in ash...",
			"This office has been empty for a long while. There's a desk with a broken laptop. A wire is also hanging "
			"from the roof and it's best not to touch it.",
			"There's lots of books on bookshelves. Most of the books were burnt at least in some way. There's no "
			"computer but there is an empty table with a fridge.",
			"The office is very terribly damaged, but some contents of the fridge are still present. The table is broken."
		))


