# Package import
from random import randint

# Internal import
from .item import Item

# Bread class
class Bread(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "BREAD", "Bread")

    def use(self):
        if self.holder.health >= 100:
            print("Lose some HP first, ok?")
            return

        self.holder.health += randint(10, 15)
        if randint(1, 2) == 2:
            self.holder.attack += randint(12, 15)
        else:
            self.holder.defense += randint(12, 15)
        print("You ate the loaf of bread.")
        self.dispose()

