# Internal import
from .item import Item

# Weapon blueprint
class Shield(Item):
    def __init__(self, holder, name, display_name, bonus):
        # Inheritance
        Item.__init__(self, holder, name, display_name)

        # Additionals
        self.item_type = "equipment"
        self.def_bonus = bonus
        self.equipped = False

    def equip(self):
        self.holder.shield = self
        self.holder.defense += self.def_bonus
        self.equipped = True

    def unequip(self):
        self.holder.equipped_shield = None
        self.holder.defense -= self.def_bonus
        self.equipped = False

