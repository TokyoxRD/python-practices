

#print(main())


#python banking program

def show_balance():
   print(f"Your balance is: ${balance}")

def deposit():
    print("Deposite")
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw():
    print("Withdraw")
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("\n--- Banking Menu ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
        print("Thank you for banking with us!")
    else:
        print("Invalid choice. Please try again.")
        print("   ")