import itertools
import requests
import time
import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
chars = ''.join(random.sample(s,len(s)))
combos = itertools.product(chars, repeat=6)

for combo in combos:
    user = ''.join(combo)
    print(user)
    
    while True:
        response = requests.post(
            'https://users.roblox.com/v1/usernames/users',
            json={
                "usernames": [user],
                "excludeBannedUsers": False
            }
        )
        data = response.json()

        if "errors" in data:
            if any(error["message"] == "Too many requests" for error in data["errors"]):
                print("Too many requests")
                time.sleep(5)
                continue
        else:
            break 

    if "data" in data and len(data["data"]) == 0:
        with open("unclaimed.txt", "a") as f:
            f.write(user + "\n")
            f.flush()
        print("UNCLAIMED!")