# Internal import
from .item import Item

# Apple class
class WaterBottle(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "WATER_BOTTLE", "Water Bottle")
        self.consumed = False

    def use(self):
        if self.consumed:
            print("The water bottle is empty. Tough!")
            return

        self.consumed = True
        if self.holder.health > 100:
            print("You just lost some HP. Idiot.")
        elif self.holder.health == 100:
            print("Nothing happened.")
        else:
            print("Health restored back to 100.")
        self.holder.health = 100

