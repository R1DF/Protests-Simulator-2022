"""
PROTESTS SIMULATOR
R1DF 2022

Making this small text-based game as a CS project. Your job is simple: Get a water bottle while the population causes havoc.
"""

# Internal imports
from coltext import *
from gameinit import Game

# Debug - write below this comment for any debugging and set the "debug" variable to True
debug = False

# Program code
if debug:
    quit()

clear()
print("""
Protests Simulator 2022
Your objective throughout this game is to get a water bottle while mass protests happen around the city.
""")
input("\nPress Enter to begin.\n")
clear()

# Making the player
name = force_request("Enter your name: ")

# Game loop
game = Game()
