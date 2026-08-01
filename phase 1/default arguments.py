import time



#def net_price(list_price, discount=0, tax=0.06):
    #return list_price * (1 - discount) * (1 + tax)

#print(net_price(100))
#print(net_price(100, 0.1))

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE")

count(10)

