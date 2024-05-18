from util import utils
from util.program import *


async def latest():
    utils.os.system('cls')
    print(f'\n{utils.red} [+] LATEST RELEASE : {utils.red}{utils.latest_release}{utils.reset}')