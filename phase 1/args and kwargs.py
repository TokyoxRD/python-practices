

#def add(*args):
    #total = 0
   #for arg in args:
        #total += arg
   #return total

#print(add(3, 4 ,3))


#def add(*nums):
   # total = 0
    #for num in nums:
        #total += num
    #return total

#print(add(3, 4 ,3))



#def display_name (*args):
    #for arg in args:
        #print(arg, end =" ")

#display_name("hansel", "seok", "kim")

#def print_address(**kwargs):
    #for key, value in kwargs.items():
       # print(f"{key}: {value}")

#print_address(name = "Seokjin",
              ##zip_code="12345")


def shipping_label (*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
   
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip_code')}")

shipping_label("Dr.", "Hansel", "Polanco", "III",
                street="123 Fake St",
                city="New York",
                state="NY",
                zip_code="12345")