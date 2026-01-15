import math
talents=float(input("Enter talents: "))
pounds=float(input("Enter pounds: "))
lots=float(input("Enter lots: "))
talents_in_grams=20*32*13.3*talents
pounds_in_grams=32*13.3*pounds
lots_in_grams=13.3*lots
total_grams=talents_in_grams+pounds_in_grams+lots_in_grams
kilograms=int(total_grams//1000)
remaining_grams=total_grams % 1000
print(f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams:6.2f} grams.")