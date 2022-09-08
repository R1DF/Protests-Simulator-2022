# Internal import
from .item import Item

# Apple class
class DiceOfFate(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "DICE_OF_FATE", "Mysterious Dice of Fate")
