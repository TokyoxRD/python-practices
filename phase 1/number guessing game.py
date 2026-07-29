import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("welcome to number guessing game!")
print(f"Guess the number between {lowest_num} and {highest_num}")

while is_running:
    user_input = input("Enter your guess: ")

    if user_input.isdigit():
        guess = int(user_input)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("your number is out of range")
            print(f"please enter a valid number between {lowest_num} and {highest_num}")

        elif guess > answer:
            print("Your guess is too high")
            print("Try again")

        elif guess < answer:
            print("Your guess is too low")
            print("Try again")

        else:
            print(f"YOUR ANSWER IS CORRECT! It was {answer} and you got it in {guesses} tries")
            is_running = False

    else:
        print("please enter a valid number")
