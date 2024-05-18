from util import utils
from util.program import *
from bs4 import BeautifulSoup as htmlparser
import requests

def lookup(phone_number):
    http = requests.get(f"https://free-lookup.net/{phone_number}")
    html = htmlparser(http.text, "html.parser")
    infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")

    return {k.text.strip(): infos[i+1].text.strip() if infos[i+1].text.strip() else "No information" for i, k in enumerate(infos) if not i % 2}

async def phonelookup():
        utils.os.system('cls')
        print(utils.red + utils.phone_banner)
        try:
            phone_number = input("Phone number: ").strip().replace("-", "").replace(" ", "").replace("+", "")
        except KeyboardInterrupt:
            return

        try:
            infos = lookup(phone_number)
        except AttributeError:
            print("Error: Invalid phone number\n")

        [print(f"{info}: {infos[info]}") for info in infos]
        print("\n")