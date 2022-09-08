# Internal imports
import coltext
import os
from random import choice

# Command tracer class
class CommandTracer:
    def __init__(self, master):
        self.master = master
        self.compass_directions = (
            "EAST",
            "WEST",
            "NORTH",
            "SOUTH",
            "NORTHEAST",
            "NORTHWEST",
            "SOUTHEAST",
            "SOUTHWEST"
        )
        self.compass_direction_contractions = (
            "E",
            "W",
            "N",
            "S",
            "NE",
            "NW",
            "SE",
            "SW"
        )
        self._naughty_words = ("FUCK", "SHIT", "ASS", "DICK", "COCK", "PUSSY", "BITCH")
        self.fight_words = ("ATK", "ATTACK", "DEF", "DEFEND", "FLEE", "RETREAT")

    def trace(self, command):
        if command == "HELP":
            print(coltext.colformat(open(os.getcwd() + "\\txt\\gamecommands.txt", "r").read()))

        elif command in ["TIDY", "CLEAR", "CLS"]:
            coltext.clear()
            coltext.announce("Enter \"HELP\" to get information on the game commands.") # Help note still stays.

        elif command == "MAP" or command == "WHERE":
            self.master.return_map()

        elif command == "LOOK":
            if self.master.field.field[self.master.player.y][self.master.player.x].contents is not None:
                print("You take a look around the place.")
                self.master.field.field[self.master.player.y][self.master.player.x].contents.show_contents()  # jeez this is big
            else:
                print("You're located in the streets.")

        elif command == "INV" or command == "INVENTORY":
            if not self.master.player.inventory:  # falsey values??? bruh I thought that was in JS only
                print("You're not holding anything.")
            else:
                print(self.master.player.name + "'s inventory:")
                for item in self.master.player.inventory:
                    print(item.display_name)

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

        elif command in ["ME", "DETAILS"]:
            print(coltext.detformat(open(os.getcwd() + "\\txt\\details.txt", "r").read(), self.master.player))

        elif command == "SCORE":
            coltext.announce(f"Score: {self.master.player.score}")

        elif command in self.compass_directions or command in self.compass_direction_contractions:  # longer to check so it goes last
            direction = command.lower() if command in self.compass_direction_contractions else self.compass_direction_contractions[self.compass_directions.index(command)].lower()
            contraction = self.compass_directions[self.compass_direction_contractions.index(direction.upper())].lower()

            if self.master.player.check_movement(direction):
                self.master.player.move(direction)
                print(f"You moved to the {contraction}.")
                if self.master.field.field[self.master.player.y][self.master.player.x].contents is not None:
                    print("\n")
                    self.master.field.field[self.master.player.y][self.master.player.x].contents.disclose()
            else:
                coltext.alarm(choice(["Let's stop here.", "You can't move further.", "You have reached the map limits. Go somewhere else."]))

        elif command in self.fight_words:
            coltext.alarm("You're not fighting right now.")

        elif command in self._naughty_words:
            coltext.alarm(choice(["Jeez...", "You ok?", "Language."]))

        elif command == "":
            coltext.alarm(choice(["... Gonna say something?", "I'm waiting.", "Sometimes silence is louder than words...", "You sure do wait a lot."]))

        else:
            print(coltext.colformat("R#Invalid command. Enter~| B#\"HELP\"~| R#for a list of valid commands.~|"))
