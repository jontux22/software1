names = set()

while True:
    name = input("Enter a name")
    print(name)

    if name == "":
        break

    if name not in names:
        print("New name")
        names.add(name)
    else:
        print("Existing name")
