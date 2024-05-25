import colorama
from colorama import Fore
from util import utils

async def dox():
    utils.os.system('cls')
    print(utils.blue + utils.dox_banner)
    discord_id = input(Fore.RED +  "Discord ID: ")
    username = input(Fore.CYAN +  "Username: ")
    name = input(Fore.RED +  "Name: ")
    lastname = input(Fore.BLUE + "LastName: ")
    age = input(Fore.CYAN + "Age: ")
    birth = input (Fore.BLUE +  "birthday: ")
    phone = input(Fore.RED +  "Phone: ")
    city = input(Fore.BLUE +  "City: ")
    country = input(Fore.RED +  "Country: ")
    adress = input(Fore.CYAN +  "address: ")
    snap = input(Fore.BLUE +  "Snap: ")
    insta = input(Fore.RED +  "Insta: ")
    telegram = input(Fore.BLUE +  "Telegram: ")
    youtube = input(Fore.CYAN +  "youtube: ")
    ip = input(Fore.RED +  "IP: ")
    operateur = input(Fore.BLUE +  "operator: ")
    mail = input(Fore.RED +  "mail: ")
    

    print (Fore.RED + f"""\n\n
     _________________________________
    |                                 |
    |           PERSONAL INFO         |  
    |_________________________________|

    prénom : {name}
    nom : {lastname}
    age : {age}
    date de naissance :  {birth}
    numéro de téléphone : {phone}
    ---------------------------------
    adresse : {adress}
    ville : {city}
    pays : {country}


     _________________________________
    |                                 |
    |           DISCORD INFO          |  
    |_________________________________|

    identifiant : {discord_id}
    pseudo : {username}

     _________________________________
    |                                 |
    |           RESAUX SOCIAUX        |  
    |_________________________________|

    youtube : {youtube}
    instagram : {insta}
    snapchat : {snap}
    telegram : {telegram}

     _________________________________
    |                                 |
    |              OTHER              |  
    |_________________________________|

    adresse IP : {ip}
    opérateur : {operateur}
    adresse email : {mail}


    """)