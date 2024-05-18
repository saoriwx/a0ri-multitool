import whois
import whois.time_zones
import colorama
from colorama import *
import os
import subprocess
import socket
import time
import util
from util import utils
from util.program import *
from util import utils


red = Fore.RED
reset = Fore.RESET
pink = Fore.MAGENTA
green = Fore.GREEN
blue = Fore.CYAN
cyan = Fore.BLUE


author = "saori.wx"
github = "https://github.com/saoriwx"
discord = "https://discord.gg/GDcuZgyPKN"


hostname = socket.gethostname()


banner = f"""

                         {red}                █████╗  ██████╗ ██████╗ ██╗{reset}
                         {red}               ██╔══██╗██╔═████╗██╔══██╗██║{reset}
                         {red}               ███████║██║██╔██║██████╔╝██║{reset}  {red}MADE BY {red}{author}{reset}
                         {red}               ██╔══██║████╔╝██║██╔══██╗██║{reset} 
                         {red}               ██║  ██║╚██████╔╝██║  ██║██║{reset}
                         {red}               ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
                                                
                                                                    {red} [+] GITHUB :       {red}{github}{reset}
                                                                    {red} [+] SUPPORT :     {red} {discord} {reset}

{red}                                                                                              
 __________________________________________________________________
/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/       
  
{red}[1] IPLOOKUP{reset}      {red}[3] SEARCHER{reset}

{red}[2] STEALER{reset}       {red}[4] PHONE LOOKUP{reset}


{red} __________________________________________________________________
/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/


"""


iplookup_banner = f"""
{red}



    ________     __    ____  ____  __ ____  ______ 
   /  _/ __ \   / /   / __ \/ __ \/ //_/ / / / __ \\
   / // /_/ /  / /   / / / / / / / ,< / / / / /_/ /
 _/ // ____/  / /___/ /_/ / /_/ / /| / /_/ / ____/ 
/___/_/      /_____/\____/\____/_/ |_\____/_/      
                                                  
 


                                                {reset}


"""

stealer_banner = r"""

  _______________________________   _____  .____     _____________________ 
 /   _____/\__    ___/\_   _____/  /  _  \ |    |    \_   _____/\______   \
 \_____  \   |    |    |    __)_  /  /_\  \|    |     |    __)_  |       _/
 /        \  |    |    |        \/    |    \    |___  |        \ |    |   \
/_______  /  |____|   /_______  /\____|__  /_______ \/_______  / |____|_  /
        \/                    \/         \/        \/        \/         \/ 

"""


searcher_banner = """



                                                                                                                                                                
███████ ███████  █████  ██████   ██████ ██   ██ ███████ ██████  
██      ██      ██   ██ ██   ██ ██      ██   ██ ██      ██   ██ 
███████ █████   ███████ ██████  ██      ███████ █████   ██████  
     ██ ██      ██   ██ ██   ██ ██      ██   ██ ██      ██   ██ 
███████ ███████ ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██ 
                                                                
"""

phone_banner = """


__________.__                           .__                 __                 
\______   \  |__   ____   ____   ____   |  |   ____   ____ |  | ____ ________  
 |     ___/  |  \ /  _ \ /    \_/ __ \  |  |  /  _ \ /  _ \|  |/ /  |  \____ \ 
 |    |   |   Y  (  <_> )   |  \  ___/  |  |_(  <_> |  <_> )    <|  |  /  |_> >
 |____|   |___|  /\____/|___|  /\___  > |____/\____/ \____/|__|_ \____/|   __/ 
               \/            \/     \/                          \/     |__|    




"""


