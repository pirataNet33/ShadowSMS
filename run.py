import os
import time
import requests
import subprocess
import readline
import colorama
from colorama import Fore

def funtion_banner():
	try:
		print(Fore.RED+"")
		subprocess.run(["cat", "./banner/banner.txt"])
		print(Fore.RESET+"")
		print(Fore.BLUE+"creador: ", Fore.RED+"pirataNet33")
		print(Fore.RED+"github : ", Fore.YELLOW+"https://github.com/pirataNet33/")
	except OSError as error_a:
		print("error al cargar banner", error)
funtion_banner()
phone = input(Fore.WHITE+"phone: "+Fore.RED+">> "+Fore.RESET)
mens = input(Fore.WHITE+"mensaje: "+Fore.RED+">> "+Fore.RESET)

resp = requests.post('https://textbelt.com/text', {
	'phone':f'{phone}',
	'message':f'{mens}',
	'key':'textbelt',
	})
print(resp.json())