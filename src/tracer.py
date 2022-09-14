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
        self.last_command = None

    def trace(self, command):
        match command:
            case "HELP":
                print(coltext.colformat(open(os.getcwd() + "\\txt\\gamecommands.txt", "r").read()))
                self.last_command = "HELP"

            case "TIDY" | "CLEAR" | "CLS":
                coltext.clear()
                print(coltext.colformat("Enter \"B#HELP~|\" to get information on the game commands.")) # Help note still stays.
                self.last_command = "TIDY"

            case "MAP" | "WHERE":
                self.master.return_map()
                self.last_command = "MAP"

            case "LOOK":
                self.handle_look_query()
                self.last_command = "LOOK"

            case "TAKE":
                self.handle_take_query()
                self.last_command = "TAKE"

            case "PUT DOWN":
                self.handle_put_down_query()
                self.last_command = "PUT DOWN"

            case "USE":
                self.master.player.handle_use_query()
                self.last_command = "USE"

            case "EQUIP":
                self.master.player.handle_equip_query()
                self.last_command = "EQUIP"

            case "UNEQUIP":
                self.master.player.handle_unequip_query()
                self.last_command = "UNEQUIP"

            case "INV" | "INVENTORY":
                if self.master.player.inventory == [] and self.master.player.consumables == []:  # falsey values??? bruh I thought that was in JS only
                    print("You're not holding anything.")
                else:
                    self.master.player.get_holdings()
                self.last_command = "INV"

            case "STATUS":
                self.handle_status_query()
                self.last_command = "STATUS"

            case "ME" | "DETAILS":
                print(coltext.detformat(open(os.getcwd() + "\\txt\\details.txt", "r").read(), self.master.player))
                self.last_command = "ME"

            case "SCORE":
                coltext.announce(f"Score: {self.master.player.score}")
                self.last_command = "SCORE"

            case "MOVES":
                self.master.player.get_moves()
                self.last_command = "MOVES"

            case "QUIT":
                if coltext.confirm():
                    self.master.has_quit = True

            case _:  # match pattern doesn't work with list membership (unless I'm an imbecile)
                if command in self.compass_directions or command in self.compass_direction_contractions:  # Compass directions
                    direction = command.lower() if command in self.compass_direction_contractions else self.compass_direction_contractions[self.compass_directions.index(command)].lower()
                    contraction = self.compass_directions[self.compass_direction_contractions.index(direction.upper())].lower()

                    if self.master.player.check_movement(direction):
                        self.master.player.move(direction)
                        print(f"You moved to the {contraction}.")
                        if self.master.field.field[self.master.player.y][self.master.player.x].contents is not None:
                            print("\n")
                            self.master.field.field[self.master.player.y][self.master.player.x].contents.disclose()
                        self.last_command = "MOVE"
                    else:
                        coltext.alarm(choice(["Let's stop here.", "You can't move further.", "You have reached the map limits. Go somewhere else."]))
                        self.last_command = "MOVE-" # the minus means that the moving failed

                elif command in self.fight_words:
                    coltext.alarm("You're not fighting right now.")

                elif command in self._naughty_words:
                    coltext.alarm(choice(["Jeez...", "You ok?", "Language."]))

                elif command == "":
                    coltext.alarm(choice(["... Gonna say something?", "I'm waiting.", "Sometimes silence is louder than words...", "You sure do wait a lot."]))

                else:
                    print(coltext.colformat("R#Invalid command. Enter~| B#\"HELP\"~| R#for a list of valid commands.~|"))

    def handle_look_query(self):
        if self.master.field.field[self.master.player.y][self.master.player.x].is_place():
            print("You take a look around the place.")
            self.master.field.field[self.master.player.y][
                self.master.player.x].contents.show_contents()  # jeez this is big
        else:
            print("You're located in the streets.")

    def handle_take_query(self):
        if self.master.field.field[self.master.player.y][self.master.player.x].is_place():
            self.master.field.field[self.master.player.y][self.master.player.x].contents.show_contents()
            if self.master.field.field[self.master.player.y][self.master.player.x].contents.contents:
                print("\n")
                self.master.field.field[self.master.player.y][self.master.player.x].contents.handle_take_query(
                    self.master.player)
        else:
            coltext.alarm("There is nothing you can grab on the streets,")

    def handle_put_down_query(self):
        if self.master.player.inventory == [] and self.master.player.consumables == []:
            coltext.alarm("How can you put something down when you're not holding it?")
        elif not self.master.field.field[self.master.player.y][self.master.player.x].is_place():
            coltext.alarm("Leaving something in the streets isn't a wise decision.")
        else:
            self.master.player.handle_put_down_query(
                self.master.field.field[self.master.player.y][self.master.player.x].contents)

    def handle_status_query(self):
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
                "The game has not necessarily developed to your advantage."  # oversimplified ww2 reference
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
        print(
            f"HP: {hp}\nStatus: {status.title() if 'nde' not in status else status.title().replace('Nde', 'NDE')}\n{choice(detail) if hp < 100 else detail}")

    def enter_fight(self):
        pass
