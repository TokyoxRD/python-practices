#string methods len(length), find,rfind

#name = input("enter your name: ")

#result = len(name)
#result = name.find("a")
#result = name.rfind("a")

#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#name = name.isdigit()
#name = name.isalpha()
#result = phone.count("-")
#phone = input("enter your phone number: ")
#result = phone.replace("-","")
#print(result)




#- - - Excersise 1 - - -

#phone = input("enter your phone number: ")

#if phone.isdigit():
    #print("your phone number is valid")

#else:
    #print("your phone number is invalid")

# - - - Excersise 2 - - -

username = input("enter your username: ")

if len(username) > 12:
    print("username must contain 12 or less characters")
elif " " in username:
    print("username must not contain spaces")
elif not username.isalpha():
    print("username must only contain letters")
else:
    print("valid username")
    
    


