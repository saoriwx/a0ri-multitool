import util
from util import utils
from util.program import *
import asyncio
import util.program
import util.program.stealer

while True:

    async def menu():
            utils.os.system('cls')

            print(utils.banner)


        

            choice = input(f"""{utils.red}┌───({utils.reset}{utils.hostname}@a0ri{utils.red})─[{utils.reset}~{utils.red}]
└──{utils.reset}$ {utils.reset}""")
            


            if choice =='1':
                utils.os.system('cls')
                from util.program.iplookup import iplookup
                await iplookup()

                input(f'\n{utils.blue}press enter to exit')

            elif choice == '2':
                 from util.program.stealer import stealer
                 await stealer()
                 input(f'\n{utils.blue}press enter to exit')

            elif choice == '3':
                 from util.program.searcher import searcher
                 await searcher()
                 input(f'\n{utils.blue}press enter to exit')

            else:
                 print(f'{utils.red}[+] INVALID CHOICE')
                 utils.time.sleep(2)


    asyncio.run(menu())