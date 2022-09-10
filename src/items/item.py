# For algorithms
display_name_to_text = {
    "APPLE": "Apple",
    "BREAD": "Bread",
    "POTATO": "Potato",
    "DICE_OF_FATE": "Dice of Fate"
}

# Item blueprint
class Item:
    def __init__(self, holder, name, display_name):
        # Initialization
        self.holder = holder
        self.name = name
        self.display_name = display_name
        self.item_type = "consumable"  # original type is always consumable

    def use(self):
        pass

