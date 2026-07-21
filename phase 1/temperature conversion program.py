#conversion

unit = input("your unit is celcius or farenheight(C/F)? ")
temp = float(input("Enter your temperature: "))

if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "F"
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "C"
else:
    print("Invalid unit")

print(f"Your temperature is {round(temp, 2)} {unit}")
