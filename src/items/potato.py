# Internal import
from .item import Item

# Apple class
class Potato(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "POTATO", "Potato")
