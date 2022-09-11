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
from items.medkit import Medkit
from items.dagger import Dagger
from items.bat import WoodenBat
from items.gun import Gun
from items.wooden_shield import WoodenShield
from items.metal_shield import MetalShield
from items.riot_shield import RiotShield


# Item Dropper blueprint
class ItemDropper:
    def __init__(self, player):
        self.player = player
        self.consumables = (
            ("APPLE", 0),
            ("BREAD", 0),
            ("POTATO", 0),
            ("DICE_OF_FATE", 0),
            ("MEDKIT", 0)
        )
        self.consumables_rng_values = (0, 0, 0, 0, 0)

        self.equipment = (
            ("DAGGER", 0),
            ("WOODEN_BAT", 0),
            ("GUN", 0),
            ("WOODEN_SHIELD", 0),
            ("METAL_SHIELD", 0),
            ("RIOT_SHIELD", 0)
        )
        self.equipment_rng_values = (0, 0, 0, 0, 0, 0)

    def set_consumables_and_rng(self, items, rng_values):
        self.consumables = (
            ("APPLE", items[0]),
            ("BREAD", items[1]),
            ("POTATO", items[2]),
            ("DICE_OF_FATE", items[3]),
            ("MEDKIT", items[4])
        )  # this part looks stupid so I'd rather get rid of it eventually and make smth better
        self.consumables_rng_values = rng_values

    def set_equipment_and_rng(self, items, rng_values):
        self.equipment = (
            ("DAGGER", items[0]),
            ("WOODEN_BAT", items[1]),
            ("GUN", items[2]),
            ("WOODEN_SHIELD", items[3]),
            ("METAL_SHIELD", items[4]),
            ("RIOT_SHIELD", items[5])
        )  # this sucks
        self.equipment_rng_values = rng_values

    def randomize_consumables(self, place: Place = None):
        # Randomizing
        randomized_contents = []
        for item, amount in self.consumables:
            for i in range(amount):
                throw_limit = self.consumables_rng_values[self.consumables.index((item, amount))]
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
                case "MEDKIT":
                    place.contents.append(Medkit(self.player))
                case _:
                    pass

    def randomize_equipment(self, place: Place = None):
        # Randomizing
        randomized_contents = []
        for item, amount in self.equipment:
            for i in range(amount):
                throw_limit = self.equipment_rng_values[self.equipment.index((item, amount))]
                if random.randint(0, 100) <= throw_limit:
                    randomized_contents.append(item)

        # Appending the contents
        for item in randomized_contents:
            match item:
                case "DAGGER":
                    place.contents.append(Dagger(self.player))
                case "WOODEN_BAT":
                    place.contents.append(WoodenBat(self.player))
                case "GUN":
                    place.contents.append(Gun(self.player))
                case "WOODEN_SHIELD":
                    place.contents.append(WoodenShield(self.player))
                case "METAL_SHIELD":
                    place.contents.append(MetalShield(self.player))
                case "RIOT_SHIELD":
                    place.contents.append(RiotShield(self.player))
                case _:
                    pass

