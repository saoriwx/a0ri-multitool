import time
import requests
from colorama import Fore
from util import utils

async def hypesquadchanger():
    utils.os.system('cls')
    print(utils.red + utils.hschanger_banner)
    hypetoken = input(f"\n{utils.red}Your token account: {Fore.RESET}") # OBLIGATOIRE 
    print(utils.red + f"\n[1] Bravery\n[2] Briliance\n[3] Balance\n")
    hypesquad = input(f"[+] Choice : {Fore.RESET}")
    headersosat = {
        'Authorization': str(hypetoken)
    }

    payloadsosat = {
        'house_id': str(hypesquad)
    }
    time.sleep(1)
    rep = requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headersosat)

    print(utils.red + '\nFINISH! ')
