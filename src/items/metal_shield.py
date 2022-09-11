# Internal import
from .shield import Shield

# Dagger class
class MetalShield(Shield):
    def __init__(self, holder):
        # Initialization
        Shield.__init__(self, holder, "METAL_SHIELD", "Metal Shield", 8)

