import tls_client
from random import choices, choice
from time import sleep
import os
from util import utils

os.system('cls')
print(utils.red + utils.w_banner)
session = tls_client.Session(

    client_identifier="chrome_108"

)
class token_raid:
    def __init__(self):
        
        mesgg = input('MESSAGE: ')
        self.msg    = mesgg
        self.send   = 0
        self.error  = 0
        self.token  = open('tokens.txt', 'r').read().splitlines()
        self.sid    = input("Enter Server ID: ")
        self.cid    = input("Enter Channel ID: ")

    async def raider(self):
        
        print('PRESS CTRL C TO STOP') # j'ai pas trouvé d'alternative et j'avais un peu la flemme donc le programme va crash il faudra le relancer

        while True:
            

            self.raa   = choice(self.token)
            headers = { 
            'authority': 'discord.com',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDQiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc1NTE3LCJuYXRpdmVfYnVpbGRfbnVtYmVyIjoyOTU4NCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
            'x-discord-locale': 'fr-EU',
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'fr-EU',
            'authorization': f'{self.raa}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9011 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
            'content-type': 'application/json',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://discord.com/channels/{self.sid}/{self.cid}',

            }

            json_data = {
                'content': self.msg,
                'tts': False,
            }

            response = session.post(f'https://discord.com/api/v9/channels/{self.cid}/messages',headers=headers,json=json_data)
            if response.status_code == 200:
                self.send += 1
                print(f"Send | Amount: {self.send}")
            else:
                self.error += 1
                print(f"Error | Amount: {self.error}")
