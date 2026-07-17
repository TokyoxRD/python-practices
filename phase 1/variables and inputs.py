#- - - -variables- - - -

#strings

name = "hansel"
last_name = "polanco"

#integers
age = 23
phone_number = 8095555555

#float
hight = 1.75
gpa = 3.9

#booleans
is_student = False


#- - - - - type casting- - - - the process to convert a varible from one data type to another data type(srt(),int(),float(),bool())- -
name2 = "hansel"
age = 24
gpa2 = 2.4
student = True

#- - - inputs - - -



#excersise 1

#lenght = float(input("Enter the lenght "))
#width = float(input("Enter the width "))

#area = lenght*width
#print("the area is", area)

#excersise 2

item = input("what item did you buy? ")
price = float(input("what is the price of the item? "))
quantity = int(input("hoy many item do you want to buy?"))

final_price = price * quantity

print(f"you bought {quantity} of {item} for a total of {final_price}$  ")
