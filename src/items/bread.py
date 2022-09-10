# Internal import
from .item import Item

# Bread class
class Bread(Item):
    def __init__(self, holder,):
        Item.__init__(self, holder, "BREAD", "Bread")
