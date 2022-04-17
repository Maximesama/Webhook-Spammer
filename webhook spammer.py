import requests
import colorama
from colorama import Fore
colorama.init()

banner = """
    ___        ___        ___        ___     __  ___     __        ___
  ((   ) )   //   ) )   //___) )   //   ) )   / /      //  ) )   //___) )
   \ \      //___/ /   //         //         / /      //        //
//   ) )   //         ((____     ((____     / /      //        ((____
"""
print(Fore.RED + banner)
print(Fore.RED + '                                         Made by Maxim3sama#8381')

input()

print(Fore.RED + 'Quel est votre Webhook? ')
webhook = input("")
print("Quel est votre message? ")
mess = input("")
content = (mess)

payload = {
    'content': (content)
}
def run_loop():
    stop = False
    while not stop:

        r = requests.post(webhook, data=payload,)
run_loop()
