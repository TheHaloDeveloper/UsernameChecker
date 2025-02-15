import itertools

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
combos = itertools.product(chars, repeat=4)
count = 0

for combo in combos:
    print(''.join(combo))
    count += 1
    
print(f"\n\n{count}")