# Package import
from random import randint

# Internal import
from .item import Item

# Apple class
class Apple(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "APPLE", "Apple")

    def use(self):
        if self.holder.health >= 100:
            print("Lose some HP first, ok?")
            return

        self.holder.health += randint(7, 14)
        self.holder.attack += randint(3, 5)
        print("You ate the apple.")
        self.dispose()

