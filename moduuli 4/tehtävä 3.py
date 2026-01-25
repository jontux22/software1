times = 0

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        if times > 0:
            print(f"Smallest number: {small}")
            print(f"Largest number: {big}")
        break

    luku = float(user_input)

    if times == 0:
        big = luku
        small = luku
        times += 1
    else:
        if luku > big:
            big = luku
        if luku < small:
            small = luku