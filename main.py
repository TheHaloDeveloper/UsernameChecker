import itertools
import requests

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
combos = itertools.product(chars, repeat=4)
count = 0

for combo in combos:
    user = ''.join(combo)
    print(user)
    count += 1
    
    response = requests.post(
        'https://users.roblox.com/v1/usernames/users',
        json={
            "usernames": [user],
            "excludeBannedUsers": False
        }
    )
    data = response.json()
    print(data)
    
    if len(data['data']) == 0:
        print('FOUND')
        exit(0)
    
print(f"\n\n{count}")