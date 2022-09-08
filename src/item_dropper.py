"""
The ItemDropper class is used to give places an efficient way to randomize what's inside in all of them.
Note: It will raise an error if the place it generates contents in already was randomized.
"""

# Internal imports
import items
import random
from places.place import Place
from items.apple import Apple
from items.bread import Bread
from items.potato import Potato
from items.dice_of_fate import DiceOfFate


# Item Dropper blueprint
class ItemDropper:
    def __init__(self, player):
        self.player = player
        self.items = (  # Weapons and shields spawn differently, only one per random place
            ("APPLE", 2),  # the 2 signifies how much of apples can there be
            ("BREAD", 2),
            ("POTATO", 2),
            ("DICE_OF_FATE", 1)
        )

        self.rng_values = (  # out of 100
            75,
            75,
            15,
            60
        )

    def randomize(self, place: Place = None):
        # Randomizing
        randomized_contents = []
        for item, amount in self.items:
            for i in range(amount):
                throw_limit = self.rng_values[self.items.index((item, amount))]
                if random.randint(0, 100) <= throw_limit:
                    randomized_contents.append(item)

        # Appending the contents
        for item in randomized_contents:
            match item:
                case "APPLE":
                    place.contents.append(Apple(self.player))
                case "BREAD":
                    place.contents.append(Bread(self.player))
                case "POTATO":
                    place.contents.append(Potato(self.player))
                case "DICE_OF_FATE":
                    place.contents.append(DiceOfFate(self.player))
                case _:
                    pass

