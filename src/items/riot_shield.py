# Internal import
from shield import Shield

# Dagger class
class RiotShield(Shield):
    def __init__(self, holder):
        # Initialization
        Shield.__init__(self, holder, "RIOT_SHIELD", "Riot  Shield", 11)

