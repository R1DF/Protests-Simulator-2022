# Getting colorama
from colorama import init, Fore, Style
from os import name, system # For clearing
init()

# Functions
def clear():
	system("cls" if name == "nt" else "clear")

def colformat(file_data):
	return file_data.replace("#", Fore.BLUE).replace("|", Style.RESET_ALL)

def colformat_map(map):
	return map.replace(
		"YOU", Fore.GREEN + "YOU" + Style.RESET_ALL
	).replace(
		"HOU", Fore.BLUE + "HOU" + Style.RESET_ALL
	).replace(
		"OFF", Fore.BLUE + "OFF" + Style.RESET_ALL
	).replace(
		"HOS", Fore.RED + "RED" + Style.RESET_ALL
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
	return query
