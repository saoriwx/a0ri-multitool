import whois
import subprocess
from util import utils
from util.program import *

async def domainlookup():
    utils.os.system('cls')
    print(utils.red + utils.domain_banner)
    domain = input (f'{utils.red}[+] ENTER DOMAIN NAME : ') # EX : google.com
    obj = whois.whois(domain)
    obj2 = whois.extract_domain(domain)


    print(f"""

IP : {domain}

{obj}

REVERSE DNS : {obj2}


""")

    ask = input("DO YOU WANT TO PING THE IP ? [Y/N]: ")

    if ask == 'Y':
            command = (f'ping {domain}')
            subprocess.run(command)

    else:
          pass