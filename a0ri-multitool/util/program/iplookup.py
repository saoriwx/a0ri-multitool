import whois
import whois.time_zones
import asyncio
import subprocess
from util import utils
from util.program import *

async def iplookup():
    print(utils.iplookup_banner)
    ip = input (f'{utils.red}[+] ENTER IP : ')
    obj = whois.whois(ip)
    obj2 = whois.extract_domain(ip)


    print(f"""

IP : {ip}

{obj}

REVERSE DNS : {obj2}


""")

    ask = input("DO YOU WANT TO PING THE IP ? [Y/N]: ")

    if ask == 'Y':
            command = (f'ping {ip}')
            subprocess.run(command)

    else:
          pass