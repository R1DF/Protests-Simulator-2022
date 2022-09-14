# Package import
import random

# Internal import
from config_reader import config_data
from items.dagger import Dagger
from items.bat import WoodenBat
from items.wooden_shield import WoodenShield
from items.metal_shield import MetalShield
from items.riot_shield import RiotShield

# Enemy object
class Enemy:
    def __init__(self, player):
        # Predefined
        self.player = player
        self.health = 100
        self.attack, self.defense = random.randint(5, 10), random.randint(5, 10)
        self.name = random.choice(config_data["enemyData"]["names"])
        self.luck = random.randint(10, 80)

        # Inventory
        self.equipped_weapon = random.choice([None, Dagger(self), WoodenBat(self)])  # guns too op lmao
        self.equipped_shield = random.choice([None, WoodenShield(self), MetalShield(self), RiotShield(self)])

        for item in [self.equipped_weapon, self.equipped_shield]:
            try:
                item.equip()
            except AttributeError:
                pass

