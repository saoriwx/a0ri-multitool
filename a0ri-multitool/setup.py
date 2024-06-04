import os
import sys
import importlib.util

os.system('color 4')
print('INSTALLING ALL REQUIREMENTS')

def is_module_installed(module_name):
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is not None:
            return True
        else:
            return False
    except ImportError:
        return False

def install_module(module_name):
    if is_module_installed(module_name):
        print(f"{module_name} is already installed.")
    else:
        if sys.platform.startswith('win'):
            os.system(f'python -m pip install {module_name} > NUL')
        elif sys.platform.startswith('linux'):
            if 'arch' in os.uname().version.lower():
                os.system(f'sudo pacman -S python-{module_name.replace("python-", "")} -y > /dev/null')
            else:
                os.system(f'pip3 install {module_name} > /dev/null')
        else:
            print(f"Système d'exploitation non pris en charge. Veuillez installer manuellement le module {module_name}.")

install_module('colorama')
install_module('requests')
install_module('whois')
install_module('datetime')
install_module('bs4')
install_module('googlesearch-python')
install_module('discord')
install_module('discord.py')
install_module('tls-client')

os.system('color reset')
