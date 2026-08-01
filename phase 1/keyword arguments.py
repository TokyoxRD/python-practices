

#def hello(greeting,title,first,last):
    #print(f"{greeting} {title} {first} {last}")

#hello("Hello", "Dr.", last="Hansel", first="Seok")

#print("1", "2", "3", "4", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone("us", "444", "555", "666")
print(phone_number)
    