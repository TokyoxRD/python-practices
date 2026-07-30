import random

options = ("rock", "paper", "scissors")
computer = random.choice(options)
player = None
running = True

while running:
    while player not in options:
        player = input(f"Enter a choice {options}: ").lower()

    print(f"Player choise: {player}")
    print(f"Computer choise: {computer}")

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        running = False
    else:
        player = None
        computer = random.choice(options)
