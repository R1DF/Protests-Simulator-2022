# Game imports

# Item blueprint
class Item:
    def __init__(self, holder):
        # Initialization
        self.holder = holder
        self.name = self.display_name = None

