from googlesearch import search
from util import utils
from util.program import *
proxy = 'http://116.203.28.43:8888' # JE PENSE QU'IL FAUT CHANGER LES PROXY

async def searcher():
    utils.os.system('cls')
    print(utils.red + utils.searcher_banner)
    print('INUTILISABLE.\n')

    words = input('RECHERCHE : ')
    obj = search(words, num_results=20, lang='fr', proxy=proxy, ssl_verify=False)
    for i in obj:
        print(i)