from googlesearch import search
from util import utils
from util.program import *
proxy = 'http://116.203.28.43:8888' # VOUS POUVEZ CHANGER LES PROXY

async def searcher():
    utils.os.system('cls')
    print(utils.red + utils.searcher_banner)


    words = input('RECHERCHE : ')
    obj = search(words, num_results=40, lang='fr', proxy=proxy) # VOUS POUVEZ CHANGER LE NOMBRE DE RESULTAT QUI APPARAISSENT en modifiant la ligne : num_results=LE_NOMBRE_QUE_TU_VEUX  (MAX 49)
    for i in obj:
        print(f'\n{i}')