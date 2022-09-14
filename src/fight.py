"""
The Fight class is used to simulate a battle between the player and an AI-controlled enemy.
"""

# Internal imports
from player import Player
from enemy import Enemy
import coltext

# Package import
import os

# Fight object
class Fight:
    def __init__(self, player: Player, enemy: Enemy):
        # Getting variables
        self.player = player
        self.enemy = enemy
        self.enemy_name = self.enemy.name
        self.commands = ["HELP", "ATK", "ATTACK", "DEF", "DEFEND", "INV", "INVENTORY", "FLEE", "RETREAT"]

        # Fight loop
        self.fight_loop()

    def fight_loop(self):
        print(f"You're in a fight with a {self.enemy_name.lower()}! Oh no!\n")
        while self.enemy.health > 0 and self.player.health > 0:
            self.trace()

    def trace(self):
        command = coltext.force_request("\nWhat would you like to do? ").strip().upper()
        match command:
            case "HELP":
                print(coltext.colformat(open(os.getcwd() + "\\txt\\fight_commands.txt", "r").read()))

            case "ATK" | "ATTACK":
                pass
            case "DEF" | "DEFEND":
                pass
            case "USE":
                pass
            case "FLEE" | "RETREAT":
                pass
            case _:
                coltext.alarm("Invalid command. Remember that you're still in a fight.")