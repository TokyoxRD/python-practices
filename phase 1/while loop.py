#while loop = excecute while conditions remains true

#- - - excersise 1 - - -
#name = input("enter your name: ")

#while name == "":
#    print("please enter your name: ")
#    name = input("enter your name: ")
#print(f"hello, {name}")

# - - - excersise 2 - - -

#age = int(input("enter your age: "))

#while age < 0:
#    print("age cant be negative")
#    age = int(input("enter your age: "))
#print(f"you are, {age} years old")


# - - - excersise 3 - - -
#food = input("Enter a food you like, or 'q' to exit: ")

#while food != "q":
#    print(f"you like {food}")
#    food = input("Enter a food you like, or 'q' to exit: ")

#print("bye")


# - - - excersise 4 - - -

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print("number must be beetwen 1 and 10")
    num = int(input("Enter a number between 1 and 10: "))

print(f"You number is: {num}")
