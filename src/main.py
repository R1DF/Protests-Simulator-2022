"""
PROTESTS SIMULATOR
R1DF 2022

Making this small text-based game as a CS project. Your job is simple: Get a water bottle while the population causes havoc.
"""

# Internal imports
from coltext import *
from gameinit import Game

# Package imports
import os

# Debug - write below this comment for any debugging and set the "debug" variable to True
debug = False

# Program code
if debug:
    quit()

# Try-except statement so the game doesn't close on a weird note when you hit Ctrl+C
try:
    os.system("title Protests Simulator 2022")
    clear()
    print("""\
 Protests Simulator 2022 (running v1.0.0 indefinite)
    Your objective throughout this game is to get a water bottle while mass protests happen around the city. Beware enemies and get back safely.
    This game was based on the January 2022 unrest that occurred in Kazakhstan and has been made as a Computer Science project.
    """)

    # Making the player
    name = force_request("Enter your name: ")
    clear()

    # Game loop
    game = Game(name)

except KeyboardInterrupt:
    clear()
    print("Game closed due to Keyboard Interrupt exception.")  # this will be turn-offable later

