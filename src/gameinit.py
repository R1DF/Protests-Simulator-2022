# Imports
import coltext
from field import Field
from player import Player
from tracer import CommandTracer

# Game code
class Game:
	def __init__(self, player_name):
		# Making necessary attributes
		self.player = Player(player_name[0].upper() + player_name[1:], Player.make_random_coords())
		self.field = Field(self.player)
		self.command_tracer = CommandTracer(self)

		# Giving help note
		coltext.announce("Enter \"HELP\" to get information on the game commands.\n\n")

		# Game loop
		self.game_loop()

		# Checking how the game went
		coltext.clear()
		if self.player.get_status() != "dead":
			coltext.colformat("M#Congratulations!~|")
			print("You successfully found a water bottle and took it with you alive.")

			print("Final statistics:")
			self.command_tracer.trace("me")
			print("Well played.\n\n")

		else:
			coltext.alarm("Game over!")
			print(f"You are dead.\nCause of death: {self.player.get_cause_of_death()}\nBetter luck next time!\n\n")

		# Game ending code
		input()
		coltext.clear()
		quit()


	def game_loop(self):
		while (self.player.get_status() != "dead") and ([self.player.x, self.player.y] != self.field.parking_spot_coords): # lose and win condition
			command = coltext.request("Enter command: ").strip().upper()
			self.command_tracer.trace(command)
			print("\n")  # line breaker

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


