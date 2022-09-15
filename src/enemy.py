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
        self.attack, self.defense = random.randint(5, 7), random.randint(5, 7)
        self.name = random.choice(config_data["enemyData"]["names"])
        self.luck = random.randint(20, 40)

        # Inventory
        self.equipped_weapon = random.choice([None, Dagger(self), WoodenBat(self)])  # guns too op lmao
        self.equipped_shield = random.choice([None, WoodenShield(self), MetalShield(self), RiotShield(self)])

        for item in [self.equipped_weapon, self.equipped_shield]:
            try:
                item.equip()
            except AttributeError:
                pass

    def attack_player(self):
        """
        3 ways the attacking function will end up:
        1. crit - Critical hit
        2. success - Normal attack
        3. miss - Attack missed
        """

        if random.randint(1, 100) < self.luck and random.randint(1, 10) < 2:
            return "miss"
        else:
            if self.player.defense >= self.attack:
                return "invulnerable"

            if random.randint(1, 100) < self.luck: # crit determining
                damage_dealt = self.attack - self.player.defense
                did_crit = False
            else:
                damage_dealt = self.attack - self.player.defense + random.randint(5, 15) # adding crit
                did_crit = True

            if damage_dealt >= self.player.health:
                self.player.weapon_killed_with = self.equipped_weapon
            self.player.health -= damage_dealt
            return "crit" if did_crit else "success"

