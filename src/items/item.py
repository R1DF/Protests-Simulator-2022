# Internal import
from coltext import alarm

# For algorithms
display_name_to_text = {
    "APPLE": "Apple",
    "BREAD": "Bread",
    "POTATO": "Potato",
    "DICE_OF_FATE": "Dice of Fate",
    "MEDKIT": "Medkit",
    "DAGGER": "Dagger",
    "WOODEN_BAT": "Wooden Bat",
    "WATER_BOTTLE": "Water Bottle",
    "GUN": "Gun",
    "WOODEN_SHIELD": "Wooden Shield",
    "METAL_SHIELD": "Metal Shield",
    "RIOT_SHIELD": "Riot Shield"
}

# Item blueprint
class Item:
    def __init__(self, holder, name, display_name):
        # Initialization
        self.holder = holder
        self.name = name
        self.display_name = display_name
        self.item_type = "consumable"  # original type is always consumable
        self.description = ""

    def use(self):
        pass

    def dispose(self):
        if self.item_type == "consumable":
            self.holder.consumables.remove(self)
        else:
            alarm("DEBUG: You can't throw away an item. (line 35, items/item.py)")
