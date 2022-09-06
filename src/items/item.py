# Item blueprint
class Item:
    def __init__(self, holder, name, display_name):
        # Initialization
        self.holder = holder
        self.name = name
        self.display_name = display_name

    def use(self):
        pass

