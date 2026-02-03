month = int(input("Enter the number of a month (1-12): "))
print("You entered:", month)

def get_season(month):

    if month in [12,1,2]:
        return "winter."


    elif month in [3,4,5]:
        return "spring."

    elif month in [6,7,8]:
        return "summer."

    elif month in [9,10,11]:
        return "autumn."

if 1 <= month <= 12:
    print("The season is",get_season(month))
elif 1>month:
    print("Please enter a number between 1 and 12.")
elif 12<month:
    print("Please enter a number between 1 and 12.")
