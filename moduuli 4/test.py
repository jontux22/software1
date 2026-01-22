import random

dice1 = dice2 = throws = 0
while (dice1!=6 or dice2!=6):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    throws+=1

print(f"needed {throws} throws.")


