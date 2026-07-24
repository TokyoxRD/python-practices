#compound interest calculator

import subprocess
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter your principle amount: "))

    if principle >= 0:
        print("principle cant be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter your rate: "))

    if rate >= 0:
        print(" interest rate cant be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter your time in years: "))

    if time <= 0:
        print("time cant be less than or equal to zero")
    else:
        break


#compound interest formula: A = P(1 + r/n)^(nt)

result = principle * pow((1 + rate / 100), time)

print(f"your total to pay after {time} years will be: ${result:.2f}")