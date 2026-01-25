real_username = "python"
real_password = "rules"
tries = 0
max_tries = 5

while tries < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == real_username and password == real_password:
        print("Welcome")
        break
    else:
        tries += 1
        if tries < max_tries:
            print("Incorrect username or password. Please try again.")

if tries == max_tries:
    print("Access denied")

