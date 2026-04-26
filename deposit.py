def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    if amount < 0:
        print("Please enter a positive amount")
        return balance
    else:
        balance += amount
        return balance 