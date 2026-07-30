import random
DICE_FACES = {
    1: [
        "+---------+",
        "|         |",
        "|    o    |",
        "|         |",
        "+---------+"
    ],
    2: [
        "+---------+",
        "|  o      |",
        "|         |",
        "|      o  |",
        "+---------+"
    ],
    3: [
        "+---------+",
        "|  o      |",
        "|    o    |",
        "|      o  |",
        "+---------+"
    ],
    4: [
        "+---------+",
        "|  o   o  |",
        "|         |",
        "|  o   o  |",
        "+---------+"
    ],
    5: [
        "+---------+",
        "|  o   o  |",
        "|    o    |",
        "|  o   o  |",
        "+---------+"
    ],
    6: [
        "+---------+",
        "|  o   o  |",
        "|  o   o  |",
        "|  o   o  |",
        "+---------+"
    ],
}


dice = []
total = 0 
num_of_dice = int(input("How many dice ?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for line in range(5):
    for die in dice:
        print(DICE_FACES.get(die)[line], end=" ")
    print()



for die in dice:
    total += die
    print(f"total: {total}")

