# Internal import
from .item import Item

# Apple class
class Apple(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "APPLE", "Apple")
