import math

while True:
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches < 0:
        print("Program ended.")
        break
    centimeter = 2.54
    print(f"{inches} inches is {inches * centimeter:.2f} centimeters")
