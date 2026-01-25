import random
luku = random.randint(1,10)
while True:
    guess = int(input("Guess a number (1-10): "))
    if guess > luku:
       print("Too high")
    elif guess < luku:
       print("Too low")
    else:
      print("Correct")
      break