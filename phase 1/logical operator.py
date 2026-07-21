#logical operators = and,or,not

#- - - Excersise 1 - - -(or)
#   temp = 25
#   is_raining = False
#
#if temp > 35 or temp < 0 or is_raining:
#    print("the outdoor event is cancelled")
#else:
#    print("the outdoor event is not cancelled")

# - - - Excersise 2 - - -(and)

#temp = 25
#is_sunny = False

#if temp >= 28 and is_sunny:
    #   print("the day is sunny")

#elif temp >=28 and not is_sunny:
    #print("the day is hot but not sunny")

#elif temp < 28 and is_sunny:
    #print("the day is sunny but not hot")

#else:
    #print("the day is not sunny and is not hot")

# - - - excersise 3 - - -(not)

is_logged_in = False
user_is_admin = True

if not is_logged_in and not user_is_admin:
    print("you need to log in")

elif not is_logged_in and user_is_admin:
    print("you need to log in")
    
elif is_logged_in and not user_is_admin:
    print("you are not admin")

else:
    print("you are logged in and you are admin")

