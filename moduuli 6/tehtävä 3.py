gallons = float(input(f"Enter a volume in American gallons (negative value to quit): "))


def gallons_to_liters(gallons):
    return gallons * 3.785


while gallons >= 0:
    liters = gallons_to_liters(gallons)
    print(f"{gallons:.1f} American gallons is {liters:.2f} liters.")
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

else:
    print("Program finished.")



