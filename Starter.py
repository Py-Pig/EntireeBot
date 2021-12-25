import random
import sys
import time
import json

import requests
from colorama import Fore, init

init()
print(f"""
    {Fore.LIGHTBLUE_EX}███████╗███╗   ██╗████████╗██╗██████╗ ███████╗███████╗    ██████╗  ██████╗ ████████╗
    ██╔════╝████╗  ██║╚══██╔══╝██║██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
    █████╗  ██╔██╗ ██║   ██║   ██║██████╔╝█████╗  █████╗█████╗██████╔╝██║   ██║   ██║   
    ██╔══╝  ██║╚██╗██║   ██║   ██║██╔══██╗██╔══╝  ██╔══╝╚════╝██╔══██╗██║   ██║   ██║   
    ███████╗██║ ╚████║   ██║   ██║██║  ██║███████╗███████╗    ██████╔╝╚██████╔╝   ██║   
    ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
         {Fore.RESET}https://github.com/Py-Pig/EntireeBot | Py-Pig: developed by PigHax                                                            
""")

prefix = f"[=] "
cfg = open('config.json')
cfg = json.load(cfg)


def start():

    print(f"""
{prefix}current config:

{prefix}Token: *********************
{prefix}Channel id: {cfg["ChannelId"]}
{prefix}Delay: {cfg["Delay"]}
{prefix}Start Value: {cfg["StartValue"]}
{prefix}End Value: {cfg["EndValue"]}
    """)

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "content-type": "application/json", "Authorization": cfg['Token']}
    if requests.get('https://discord.com/api/v9/users/@me', headers=headers).status_code != 200:
        print(f"{prefix}Invalid token, exit.")
        time.sleep(5)
        sys.exit()
        return

    i = cfg['StartValue']
    while i < cfg['EndValue']:

        if cfg['Random']:
            msg = str(random.randint(cfg['StartValue'], cfg['EndValue']))
        else:
            msg = str(i)

        time.sleep(cfg['Delay'])
        message = requests.post(f"https://discord.com/api/v8/channels/{cfg['ChannelId']}/messages", headers=headers,
                                json={"content": msg})
        if message.status_code == 200:
            if not cfg["Random"]:
                i = i + 1
            print(f"{prefix}Message sent = [i=[{msg}]] [{message.status_code}]")
        else:
            print(f"{prefix}Failed to send message = [i=[{msg}]] [{message.status_code}]")
            time.sleep(1)


if __name__ == '__main__':
    start()
