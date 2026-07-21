#python weight convertor

import contextlib
weight = float(input("enter your weight: "))
unit = input("enter the unit (L or K): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print("Invalid unit")

print(f"your weight is {round(weight, 2)} {unit}")

    