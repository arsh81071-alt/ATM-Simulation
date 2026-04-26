def withdraw(balance):
    amount = float(input("Enter withdraw amount:"))

    if balance < amount:
        print("Insufficient funds")
        return balance
    elif amount<0:
        print("Amount can't be negative")
        return balance
    else:
        balance -= amount
        print(f"Withdraw amount is ${amount}")
        return balance 

