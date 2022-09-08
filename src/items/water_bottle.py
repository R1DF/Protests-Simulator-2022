# Internal import
from .item import Item

# Apple class
class WaterBottle(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "WATER_BOTTLE", "Water Bottle")
