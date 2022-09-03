# Internal imports
import coltext
import os
from random import choice

# Command tracer class
class CommandTracer:
    def __init__(self, master):
        self.master = master

    def trace(self, command):
        if command == "HELP":
            print(coltext.colformat(open(os.getcwd() + "\\txt\\gamecommands.txt", "r").read()))

        elif command in ["TIDY", "CLEAR", "CLS"]:
            coltext.clear()
            coltext.announce("Enter \"HELP\" to get information on the game commands.") # Help note still stays.

        elif command == "MAP" or command == "WHERE":
            self.master.return_map()

        elif command == "INV" or command == "INVENTORY":
            if not self.master.player.inventory:  # falsey values??? bruh I thought that was in JS only
                print("You're not holding anything.")
            else:
                print(self.master.player.name + "'s inventory:")
                for item in self.master.player.inventory:
                    print(item.name)

        elif command == "STATUS":
            # Variables to not overuse
            hp = self.master.player.health
            status = self.master.player.get_status()

            # Detail messages
            detail = {
                "healthy": [
                    "You feel fine. Sure, a bit hurt, but nonetheless you're alright.",
                    "It's just a scratch."
                ],
                "vulnerable": [
                    "You don't feel threatened but getting patched up won't feel that bad.",
                    "You can still do this. Don't worry."
                ],
                "in trouble": [
                    "You don't feel too well... Better heal yourself or get out of here faster...",
                    "The game has not necessarily developed to your advantage." # oversimplified ww2 reference
                ],
                "close to nde": [
                    "You feel like you can't take it anymore... But just a little more is all you need, right?",
                    "Might as well start praying."
                ]
            }[status]

            # Special full health statement
            if hp == 100:
                detail = "Nothing to worry about!"

            # Printing the things out
            print(f"HP: {hp}\nStatus: {status.title() if 'nde' not in status else status.title().replace('Nde', 'NDE')}\n{choice(detail) if hp < 100 else detail}")

        elif command == "SCORE":
            print("Score:", self.master.player.score)

        elif command == "":
            print(choice(["... Gonna say something?", "I'm waiting.", "Sometimes silence is louder than words...", "You sure do wait a lot."]))

        else:
            print("Invalid command. Enter \"HELP\" for a list of valid commands.")
