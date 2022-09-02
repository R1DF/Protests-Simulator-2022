"""
This class exists as a parent class for every other location type. Do not confuse it with the Location class, for that's the object that contains a place while the Place class serves as a blueprint for the places inside the Location object.
"""

class Place:
	def __init__(self, coords, master=None):
		self.master = master
		self.location_x, self.location_y = coords
