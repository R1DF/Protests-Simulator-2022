# Getting colorama
from colorama import init, Fore, Style
from os import name, system  # For clearing
init()

# Functions
def clear():
	system("cls" if name == "nt" else "clear")

def colformat(file_data):
	return file_data.replace(
		"B#", Fore.BLUE
	).replace(
		"R#", Fore.RED
	).replace(
		"G#", Fore.GREEN
	).replace(
		"Y#", Fore.YELLOW
	).replace(
		"M#", Fore.MAGENTA
	).replace(
		"C#", Fore.CYAN
	).replace(
		"~|", Style.RESET_ALL
	)

def detformat(file_data, player):
	return colformat(file_data).replace(
		"(USER)", player.name
	).replace(
		"(HP)", str(player.health)
	).replace(
		"(SCORE)", str(player.score)
	).replace(
		"(LUCK)", str(player.luck)
	).replace(
		"(ATK)", str(player.attack)
	).replace(
		"(DEF)", str(player.defense)
	).replace(
		"(X)", str(player.x + 1)
	).replace(
		"(Y)", str(player.y + 1)
	)

def colformat_map(map):
	return map.replace(
		"YOU", Fore.GREEN + "YOU" + Style.RESET_ALL
	).replace(
		"HOU", Fore.BLUE + "HOU" + Style.RESET_ALL
	).replace(
		"OFF", Fore.BLUE + "OFF" + Style.RESET_ALL
	).replace(
		"HOS", Fore.RED + "HOS" + Style.RESET_ALL
	).replace(
		"SHO", Fore.CYAN + "SHO" + Style.RESET_ALL
	).replace(
		"PAR", Fore.YELLOW + "PAR" + Style.RESET_ALL
	).replace(
		"ULK", Fore.MAGENTA + "ULK" + Style.RESET_ALL
	)

def alarm(text):
	print(Fore.RED + text + Style.RESET_ALL)

def warning(text):
	print(Fore.YELLOW + text + Style.RESET_ALL)

def announce(text):
	print(Fore.BLUE + text + Style.RESET_ALL)

def request(text):
	return input(Fore.GREEN + text + Style.RESET_ALL).strip()

def force_request(text):
	query = ""
	while query == "":
		query = input(Fore.GREEN + text + Style.RESET_ALL).strip()
		if query == "":
			alarm("Enter something.\n")

	return query
