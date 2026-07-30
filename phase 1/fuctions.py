
#def happy_birthday(name, age):
   # print("happy birthday", name)
    #print("You are", age, "years old")

#happy_birthday("Hansel", 21)
#happy_birthday("Yael", 22)


#def display_invoice(username,amount,due_date):
    #print(f"Hello {username},")
    #print(f"this is your invoice: {amount}")
    #display_invoice("Hansel", 100, "2022-12-01")



# - - - Return - - -


#def add(x, y):
   # z = x + y
   # return z

##def multiply(x,y):
    #return x * y

##def divide(x,y):
    #if y == 0:
        #return "Cannot divide by zero"
    #return x / y


#print(add(10, 5))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print(create_name("hansel", "Polanco"))
