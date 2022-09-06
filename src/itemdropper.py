"""
The ItemDropper class is used to give places an efficient way to randomize what's inside in all of them.
Note: It will raise an error if the place it generates contents in already was randomized.
"""

# Internal imports
import items
import random
from places.place import Place

# Item Dropper blueprint
class ItemDropper:
    items = (  # Weapons and shields spawn differently, only one per random place
        "APPLE",
        "BREAD",
        "DICE_OF_FATE",
        "POTATO"
    )

    rng_values = ( # out of 100
        75,
        75,
        15,
        60
    )

    @staticmethod
    def randomize(place: Place):
        pass
