# Internal import
from .weapon import Weapon

# Dagger class
class WoodenBat(Weapon):
    def __init__(self, holder):
        # Initialization
        Weapon.__init__(self, holder, "WOODEN_BAT", "Wooden Bat", 4)
