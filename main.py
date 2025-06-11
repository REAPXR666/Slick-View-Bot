# MADE BY REAPXR - purify.rip_

import requests

username = input("Profile Username: ")
amount = int(input("How Many Views: "))

x = requests.get(f"https://a.slicksmm.com/api/addviews/{username}/{amount}")

print(x.text)
print("All Views Added!")

#################
# DO NOT RESELL
