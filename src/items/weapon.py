# Internal import
from .item import Item

# Weapon blueprint
class Weapon(Item):
    def __init__(self, holder, name, display_name, bonus):
        # Inheritance
        Item.__init__(self, holder, name, display_name)

        # Additionals
        self.item_type = "equipment"
        self.atk_bonus = bonus
        self.equipped = False

    def equip(self):
        self.holder.equipped_weapon = self
        self.holder.attack += self.atk_bonus
        self.equipped = True

    def unequip(self):
        self.holder.equipped_weapon = None
        self.holder.attack -= self.atk_bonus
        self.equipped = False

