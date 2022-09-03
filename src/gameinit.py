# Imports
import coltext
from field import Field
from player import Player
from tracer import CommandTracer

# Game code
class Game:
	def __init__(self, player_name):
		# Making necessary attributes
		self.field = Field()
		self.player = Player(player_name, Player.make_random_coords())
		self.command_tracer = CommandTracer(self)

		# Giving help note
		coltext.announce("Enter \"HELP\" to get information on the game commands.\n\n")

		# Game loop
		self.game_loop()

	def game_loop(self):
		while self.player.get_status() != "dead":
			command = coltext.request("Enter what you'd like to do: ").strip().upper()
			self.command_tracer.trace(command)
			print("\n") # line breaker

	def return_map(self):
		# Formatting map and styling it
		formatted_map = []
		for column in self.field.field:
			formatted_map.append(["###" if location.contents == None else location.contents.name[:3] for location in column])
		formatted_map[self.player.y][self.player.x] = "YOU"

		for column in formatted_map:
			print(coltext.colformat_map(" | ".join(column)))

		# Index
		print(coltext.colformat_map("""
YOU - You are here
SHO - Shop
OFF - Office
HOS - Hospital
PAR - Parking spot
HOU - House
ULK - The Ulken Sharshy"""))


