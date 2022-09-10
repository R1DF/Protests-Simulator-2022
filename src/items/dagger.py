# Internal import
from weapon import Weapon

# Dagger class
class Dagger(Weapon):
    def __init__(self, holder):
        # Initialization
        Weapon.__init__(self, holder, "DAGGER", "Dagger", 6)

