import requests
import os
from pystyle import Colors, Colorate
import time

def ngl():
    
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'

    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colorate.Vertical(Colors.blue_to_purple,"""
        ░██████╗███╗░░░███╗░█████╗░██╗░░██╗███████╗
        ██╔════╝████╗░████║██╔══██╗██║░██╔╝██╔════╝
        ╚█████╗░██╔████╔██║███████║█████═╝░█████╗░░
        ░╚═══██╗██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░
        ██████╔╝██║░╚═╝░██║██║░░██║██║░╚██╗███████╗
        ╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  
    """))

    nglusername = input(Colorate.Vertical(Colors.blue_to_purple,"Username: "))
    message = input(Colorate.Vertical(Colors.blue_to_purple,"Message: "))
    Count = int(input(Colorate.Vertical(Colors.blue_to_purple,"Count:")))

    print(Colorate.Vertical(Colors.green_to_blue,"**********************************************************"))

    value =0
    notsend =0
    while value < Count:
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{nglusername}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': f'{nglusername}',
            'question': f'{message}',
            'deviceId': '0',
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
        else:
            notsend += 1
            print(R+"[-]"+W+"Not Send")
        if notsend == 10:
            print(R+"[!]"+W+"Wait 5 Seconds")
            time.sleep(5)
            notsend = 0
ngl()
