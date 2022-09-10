# Internal import
from .item import Item

# Package import
import coltext
from random import randint

# Bread class
class Medkit(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "MEDKIT", "Medkit")

    def use(self):
        hp_increase = randint(10, 25)
        self.holder.health += hp_increase
        print(coltext.colformat(f"You used a medkit.\nHP increased by C#{hp_increase}~| (HP: C#{self.holder.health}~|)"))

