# Getting colorama
from colorama import init, Fore, Style
from os import name, system # For clearing
init()

# Functions
def clear():
	system("cls" if system == "nt" else "clear")

def alarm(text):
	print(Fore.RED + text + Style.RESET_ALL)

def warning(text):
	print(Fore.YELLOW + text + Style.RESET_ALL)

def request(text):
	return input(Fore.GREEN + text + Style.RESET_ALL).strip()

def force_request(text):
	query = ""
	while query == "":
		query = input(Fore.GREEN + text + Style.RESET_ALL).strip()
	return query
