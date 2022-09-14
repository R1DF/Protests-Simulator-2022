# Package imports
from random import randint

# Internal imports
import coltext
from field import Field
from player import Player
from enemy import Enemy
from fight import Fight
from tracer import CommandTracer

# Game code
class Game:
	def __init__(self, player_name):
		# Making necessary attributes
		self.player = Player(player_name[0].upper() + player_name[1:], Player.make_random_coords())
		self.field = Field(self.player)
		self.command_tracer = CommandTracer(self)
		self.has_quit = False
		self.fight = None

		# Giving help note
		print(coltext.colformat("Enter \"B#HELP~|\" to get information on the game commands.\n\n"))

		# Game loop
		self.game_loop()

		# Checking how the game went
		coltext.clear()
		if self.player.get_status() != "dead" and (not self.has_quit):
			coltext.colformat("M#Congratulations!~|")
			print("You successfully found a water bottle and took it with you alive.\n")

		elif self.has_quit:
			print("You gave up.\n")

		else:
			coltext.alarm("Game over!")
			print(f"You are dead.\nCause of death: {self.player.get_cause_of_death()}\nBetter luck next time!\n")

		self.command_tracer.trace("ME")
		print("\nGood game. Press Enter to exit.\n")

		# Game ending code
		input()
		coltext.clear()
		quit()


	def game_loop(self):
		while (self.player.get_status() != "dead") and ([self.player.x, self.player.y] != self.field.parking_spot_coords) and (not self.has_quit): # lose and win condition
			command = coltext.request("Enter command: ").strip().upper()
			self.command_tracer.trace(command)

			if self.player.moves >= 10 and self.command_tracer.last_command == "MOVE":
				self.attempt_fight()

			print("\n")  # line breaker

	def attempt_fight(self):
		# Getting luck and bumping it up if there's a street
		luck = -15 #self.player.luck
		print(luck)
		if not self.field.field[self.player.y][self.player.x].is_place():
			luck += 15

		# RNG
		if randint(1, 100) > luck:
			self.fight = Fight(self.player, Enemy(self.player))



	def return_map(self):
		# Formatting map and styling it
		formatted_map = []
		for column in self.field.field:
			formatted_map.append(["###" if location.contents is None else location.contents.name[:3] for location in column])
		formatted_map[self.player.y][self.player.x] = "YOU"

		for column in formatted_map:
			print(coltext.colformat_map(" | ".join(column)))

		# Index
		print(coltext.colformat_map("""
Key:
YOU - You are here
SHO - Shop
OFF - Office
HOS - Hospital
PAR - Parking spot
HOU - House
ULK - The Ulken Sharshy"""))
		player_location = self.field.field[self.player.y][self.player.x]
		if player_location.contents is not None:
			print(f"You are in {player_location.contents.article} {player_location.contents.display_name.lower() if player_location.contents.display_name != 'Ulken Sharshy' else player_location.contents.display_name}.")
		else:
			print("You're outside.")


