#collection a key:values

capitals = {"USA": "Washington D.C.",
            "France": "Paris",
            "Japan": "Tokyo"}

#print(capitals.get("Japan"))

    
#if capitals.get("Japan"):
    #print(capitals.get("Japan"))
#else:
    #print("That country doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detriot"})
#capitals.pop("France")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()


#print(keys)

#for key in capitals.keys():
    #print(key)

#values = capitals.values()

#for value in values:
    #print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")





