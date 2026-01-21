name = str(input("Enter your name: "))
greet = print("Hello,", name)
balance = 1000

while True:
    print(" 1. Make a Deposit\n 2. Make a Withdrawal\n 3. Obtain Balance\n 4. Quit")
    user = str(input("Choose an option: "))

    if user == "1":
        balance += float(input("Enter Deposit amount: "))
    elif user == "2":
        amount = float(input("Enter Withdrawal amount: "))
        if amount > balance:
            print("It is not possible to withdraw beyond the account balance.")
        else: balance -= amount
    elif user == "3":
        print("Current balance is,", balance)
    elif user == "4" or user == "q" or user == "Q":
        break
    else: print("Make a selection from the menu options.")
