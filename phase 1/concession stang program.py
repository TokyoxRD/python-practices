#concession stand program

print("Welcome to the concession stand!")

menu = {"Popcorn": 2.50, 
        "Nachos": 3.00, 
        "Pretzels": 2.00, 
        "Drinks": 1.50, 
        "Candy": 1.00}

cart = []
total = 0

for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Enter the food you want to buy (or q to quit): ").lower()
    if food == "q":
        break

    food_key = food.capitalize()
    if food_key in menu:
        cart.append(food_key)
        total += menu.get(food_key)
    else:
        print("Sorry, that item is not on the menu.")

print(f"Your cart: {cart}")
print(f"Your total: ${total:.2f}")

    

