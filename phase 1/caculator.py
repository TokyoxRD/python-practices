#calculator 

operator = input("Enter operator (+,-,*,/): ")
num1 = float(input("enter the 1st number: "))
num2 = float(input("enter the 2nd number: "))

if operator == "+":
    print(round(num1 + num2, 2))
elif operator == "-":
    print(round(num1 - num2, 2))
elif operator == "*":
    print(round(num1 * num2, 2))
elif operator == "/":
    print(round(num1 / num2, 2))
else:
    print("Invalid operator")