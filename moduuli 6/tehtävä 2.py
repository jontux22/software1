import random
sides= int(input("Give the amount of sides"))



def roll_dice(sides):
    return random.randint(1,sides)

luku = roll_dice(sides)
print(luku)
while luku != sides:
    luku = roll_dice(sides)
    print(luku)
