#nested loops


rows = int(input("Enter the mount of rows: "))
coulmuns = int(input("Enter the mount of coulmns: "))
symbol = input("Enter the symbol you want to use: ")




for y in range(rows):
    for x in range(coulmuns):
        print(symbol, end="-")
    print()
    
    