# Importing blueprint
import random
from .place import Place

# Hospital class
class Hospital(Place):
    def __init__(self, coords, master=None):
        # Calling constructor
        Place.__init__(self, coords, master)

        # Getting place name
        self.name = "HOSPITAL"
        self.display_name = "Hospital"
        self.description = "This hospital is somehow in good shape, but every room except for one is blocked off.. " \
                           "Make the best out of the room you can still enter. "
