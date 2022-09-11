# Internal import
from .item import Item

# Weapon blueprint
class Weapon(Item):
    def __init__(self, holder, name, display_name, bonus):
        # Inheritance
        Item.__init__(self, holder, name, display_name)

        # Additionals
        self.atk_bonus = bonus
