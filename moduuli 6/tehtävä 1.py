import random
luku = random.randint(1,6)
print(luku)

def roll_dice():
    return random.randint(1,6)


while luku != 6:
    luku = roll_dice()
    print(luku)
