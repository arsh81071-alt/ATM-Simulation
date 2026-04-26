from balance import show_balance
from withdraw import withdraw 
from deposit import deposit 

balance = 0 
is_running = True
while is_running:
    print("\nWelcome to the Bank's ATM")
    print("1. Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance = withdraw(balance)
        print(f"Your new balance is ${balance}")
    elif choice == "3":
        balance = deposit(balance)
        print(f"Your new balance is ${balance}")
    elif choice == "4":
        exit()
    else:
        print("Please enter a valid choice")
else:
        print("Thank you for using ATM")
