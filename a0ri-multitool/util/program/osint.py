from googlesearch import search
import os
from util import utils
from util.program import *
proxy = 'http://116.203.28.43:8888' # VOUS POUVEZ CHANGER LES PROXY

directory = r'util\osint-results' 
filename = os.path.join(directory,('results') + ".txt")
async def osint():
    utils.os.system('cls')
    print(utils.red + utils.osint_banner)


    words = input('RECHERCHE : ')
    obj = search(words, num_results=40, lang='fr', proxy=proxy) 

    for i in obj:
        print(f'\n{i}')
    with open (filename, 'w') as file:
        file.write(f"{i}")

