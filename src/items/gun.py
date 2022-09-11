# Internal import
from .weapon import Weapon

# Dagger class
class Gun(Weapon):
    def __init__(self, holder):
        # Initialization
        Weapon.__init__(self, holder, "GUN", "Gun", 9)

