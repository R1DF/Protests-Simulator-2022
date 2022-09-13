# Package import
from random import randint

# Internal import
from .item import Item

# Apple class
class Potato(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "POTATO", "Potato")

    def use(self):
        self.holder.health += randint(7, 14)
        print("You ate the potato.")

        if randint(1, 2) == 1:
            self.holder.attack += randint(3, 5)
            print("You felt a bit stronger, too.")

