import random
throw = input("How many dice to roll: ")
sum = 0
throw = int(throw)


for i in range(throw):
    roll = random.randint(1,6)
    sum += roll
print(f"Sum of the dice: {sum}")