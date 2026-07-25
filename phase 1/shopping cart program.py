#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to add to the cart(q to exit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("------Your items------")
for food in foods:
    print(food, end=" ")

print()

for price in prices:
    print(price, end=" ")

print()
total = sum(prices)
print("------Your total------")
print(f"${total: .2f}")
  

        