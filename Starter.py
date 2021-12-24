import sys
import time
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

token = input(f"{prefix}Token: ")
channeled = int(input(f"{prefix}Channel Id: "))
delay = float(input(f"{prefix}Delay (float value): "))
startValue = int(input(f"{prefix}Start value: "))
endValue = int(input(f"{prefix}End value: "))


def start():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "content-type": "application/json", "Authorization": token}
    if requests.get('https://discord.com/api/v9/users/@me', headers=headers).status_code != 200:
        print(f"{prefix}Invalid token, exit.")
        sys.exit()
        return

    i = startValue
    while i < endValue:
        time.sleep(delay)
        message = requests.post(f"https://discord.com/api/v8/channels/{channeled}/messages", headers=headers,
                                json={"content": str(f"{i}")})
        if message.status_code == 200:
            i = i + 1
            print(f"{prefix}Message sent = [i=[{i}]] [{message.status_code}]")
        else:
            print(f"{prefix}Failed to send message = [i=[{i}]] [{message.status_code}]")
            time.sleep(1)


if __name__ == '__main__':
    start()
