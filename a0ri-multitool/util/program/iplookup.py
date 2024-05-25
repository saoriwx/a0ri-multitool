import requests
import subprocess
from util import utils
from util.program import *


async def iplookup():
    print(utils.iplookup_banner)
    ip = input (f'{utils.red}[+] ENTER IP : ')
    api_key = 'c59217a31a2c34' # MERCI DE NE PAS UTILISER MA CLÉ D'API POUR VOS PROJET CRÉE VOUS UN COMPTE SUR LE SITE C'EST GRATUIT https://ipinfo.io
    url = f'https://ipinfo.io/{ip}/json?token={api_key}'
  
    try:
          response = requests.get(url)
          response.raise_for_status()
          if response.status_code == 200:
            data = response.json()
            print(utils.red + "\nIP : " + ip)
            print(utils. red + "Pays :", data.get("country"))
            print(utils.red + "Ville :", data.get("city"))
            print(utils.red + "Région :", data.get("region"))
            print(utils.red + "Code Postal :", data.get("postal"))
            print(utils.red+ "Longitude :", data.get("loc").split(",")[1])
            print(utils.red + "Latitude :", data.get("loc").split(",")[0])
            print(utils.red + "ISP :", data.get("org"))

    except Exception as e:
        print(utils.red + f"ERREUR : {str(e)}")


    ask = input("\nDO YOU WANT TO PING THE IP ? [Y/N]: ")

    if ask == 'Y':
            command = (f'ping {ip}')
            subprocess.run(command)

    else:
          pass