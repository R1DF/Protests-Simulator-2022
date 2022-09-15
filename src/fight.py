"""
The Fight class is used to simulate a battle between the player and an AI-controlled enemy.
"""

# Internal imports
from player import Player
from enemy import Enemy
from config_reader import config_data
import coltext

# Package import
import os
import random

# Fight object
class Fight:
    def __init__(self, player: Player, enemy: Enemy):
        # Getting variables
        self.player = player
        self.enemy = enemy
        self.enemy_name = self.enemy.name
        self.escaped = False
        self.player_weapon, self.enemy_weapon = None, None
        self.escapable = random.randint(1, 100) <= self.player.luck
        self.commands = ["HELP", "ATK", "ATTACK", "DEF", "DEFEND", "INV", "INVENTORY", "FLEE", "RETREAT"]

        # Notifying
        print(f"You're in a fight with a {self.enemy_name.lower()}! Oh no!\n")
        self.notify()
        self.get_weapons()

        # Fight loop
        self.fight_loop()
        if self.enemy.health <= 0:
            print("Your enemy puts their hands up in surrender. You get away from the scene.\nThe fight is over.")
        else:
            print("The fight is over.")

    def get_weapons(self):
        if self.player.equipped_weapon is None:
            self.player_weapon = "NONE"
        else:
            self.player_weapon = self.player.equipped_weapon.name

        if self.enemy.equipped_weapon is None:
            self.enemy_weapon = "NONE"
        else:
            self.enemy_weapon = self.enemy.equipped_weapon.name

    def fight_loop(self):
        while self.player.health > 0:
            print(f"Your HP: {self.player.health}\nYour ATK: {self.player.attack}\nYour DEF: {self.player.defense}")
            print(f"\nEnemy's HP: {self.enemy.health}\nEnemy's ATK: {self.enemy.attack}\nEnemy's DEF: {self.enemy.defense}")
            acted = self.trace()
            if acted:
                if self.escaped or self.enemy.health <= 0: # Checking goes here to not wait at the wrong moment
                    break
                self.enemy_trace()
                self.player.stop_defense()
            print("\n")

    def notify(self):
        if self.enemy.equipped_weapon is None:
            print("The (ENEMY) does not have a weapon.".replace("(ENEMY)", self.enemy_name))
        else:
            print("The (ENEMY) is equipped with a (WEAPON).".replace("(ENEMY)", self.enemy_name).replace("(WEAPON)",
                                                                                                         self.enemy.equipped_weapon.display_name))

        if self.enemy.equipped_shield is None:
            print("The (ENEMY) does not have a shield.".replace("(ENEMY)", self.enemy_name))
        else:
            print("The (ENEMY) has a (SHIELD).".replace("(ENEMY)", self.enemy_name).replace("(SHIELD)",
                                                                                            self.enemy.equipped_shield.display_name))

    def trace(self):
        command = coltext.force_request("\nWhat would you like to do? ").strip().upper()
        match command:
            case "HELP":
                print(coltext.colformat(open(os.getcwd() + "\\txt\\fight_commands.txt", "r").read()))
                return False

            case "ATK" | "ATTACK":
                attempt = self.player.attack_enemy(self.enemy)
                match attempt:
                    case "crit":
                        print(random.choice(config_data["playerData"]["critAttackNotices"][self.player_weapon]).replace(
                            "(ENEMY)", self.enemy_name))

                    case "success":
                        print(random.choice(config_data["playerData"]["attackNotices"][self.player_weapon]).replace(
                            "(ENEMY)", self.enemy_name))

                    case "miss":
                        print(random.choice(config_data["playerData"]["missNotices"][self.player_weapon]).replace("(ENEMY)", self.enemy_name))

                    case "invulnerable":
                        print(config_data["playerData"]["failureNotices"].replace("(ENEMY)", self.enemy_name))

            case "DEF" | "DEFEND":
                self.player.defend()
                print(config_data["playerData"]["defenseNotice"])

            case "USE":
                self.player.handle_use_query()

            case "FLEE" | "RETREAT":
                print("You try to run away...")
                if self.escapable:
                    print("Success! You distract the target and vanish from their sight!")
                    self.escaped = True
                else:
                    print(random.choice(["... But you lose your breath as the target you flee from catches you.", "You realize that you're backed into a corner."]))
            case _:
                coltext.alarm("Invalid command. Remember that you're still in a fight.")
        return True

    def enemy_trace(self):
        attempt = self.enemy.attack_player()
        match attempt:
            case "crit":
                print(random.choice(config_data["enemyData"]["critAttackNotices"][self.enemy_weapon]).replace("(ENEMY)", self.enemy_name))

            case "success":
                print(random.choice(config_data["enemyData"]["attackNotices"][self.enemy_weapon]).replace("(ENEMY)", self.enemy_name))

            case "miss":
                print(config_data["enemyData"]["missNotices"][self.enemy_weapon].replace("(ENEMY)", self.enemy_name))

            case "invulnerable":
                print(config_data["enemyData"]["failureNotices"].replace("(ENEMY)", self.enemy_name))

