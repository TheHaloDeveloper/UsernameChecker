import itertools
import requests
import time

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
combos = itertools.product(chars, repeat=5)

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
            for error in data["errors"]:
                if error["message"] == "Too many requests":
                    print("Too many requests")
                    time.sleep(5)
                    continue
        break
    
    if len(data.get('data', [])) == 0:
        with open("unclaimed.txt", "a") as f:
            f.write(user + "\n")
            f.flush()
            print("UNCLAIMED!")