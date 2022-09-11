# Internal import
from .shield import Shield

# Dagger class
class WoodenShield(Shield):
    def __init__(self, holder):
        # Initialization
        Shield.__init__(self, holder, "WOODEN_SHIELD", "Wooden Shield", 6)

