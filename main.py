# MADE BY REAPXR - purify.rip_

import requests
import threading
from colorama import *

print(f"""{Fore.BLUE}Slick Profile View Botter 
{Fore.RED}- Made By REAPXR @purify.rip_
{Fore.WHITE}""")

profile = input("Enter Profile Username: ")
viewcount = int(input("How Many Views: "))

def send_view(i):
    while True:
        try:
            response = requests.get(f"https://a.slicksmm.com/profile/{profile}")
            if response.status_code == 200:
                print(f"{Fore.GREEN}[{Fore.BLUE}+{Fore.GREEN}] {Fore.BLUE} Sent {i+1} View!{Fore.WHITE}")
                break  # Exit the loop once the request is successful
            else:
                print(f"{Fore.RED}[{Fore.BLUE}-{Fore.RED}] {Fore.BLUE} Failed to send View Number {i+1}, retrying...{Fore.WHITE}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error on view {i+1}: {e}, retrying...{Fore.WHITE}")

threads = []

for i in range(viewcount):
    t = threading.Thread(target=send_view, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("[+] All views sent!")
