

#def day_week(day):
    #match day:
        #case "sunday":
           # return True
        #case "Monday":
            #return False
        #case "Tuesday":
            #return False
        #case "Wednesday":
            #return False
        #case "Thursday":
            #return False
        #case "Friday":
            #return False
        #case "Saturday":
            #return False
        #case _:
            #return "invalid day"


#print(day_week("johan"))


def is_weekend(day):
    match day:
        case "sunday" | "saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "invalid day"