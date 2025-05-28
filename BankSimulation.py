import json

accounts = {}
transactions = {}

def saveAccounts():
    with open("accounts.json", "w") as accountfile: 
        json.dump(accounts, accountfile, indent=2)

def loadAccounts():
    global accounts
    try:
        with open("accounts.json", "r") as a:
            accounts = json.load(a)
    except FileNotFoundError:
        accounts = {}

def description():
    with open("description.txt","r")as f:
            description = f.read()
            print(description)
            print()

def askAccount():
    while True:
        askaccount = input("Do you have a bank account? (Yes/No) : ").lower().strip()
        if askaccount == "yes":
            login()
        elif askaccount == "no":
            createAccount()
        else:
            print("Please enter Yes or No")
            askAccount()

MIN_AGE = 13
MAX_AGE = 18

def askAge():
    while True:
        try:
            age = int(input("Enter your age : "))
            if age < MIN_AGE:
                print("You cannot be younger than 13 years old")
            elif age > MAX_AGE:
                print("You cannot be older than 18 years old")
            else:
                print("You are eligible to create an account")
                return
        except ValueError:
            print("Please enter an integer")

def createAccount():
    while True:
        makeaccount = input("Would you like to create an account? (Yes/No) :  ").lower().strip()
        if makeaccount == "no":
            exit()
            return
        elif makeaccount == "yes":
            askAge()
            while True:
                username = input("Enter Username : ").strip()
                if " " in username:
                    print("There must not be spaces within the username.")
                    continue
                if username == "":
                    print("Please enter a username")
                    continue
                if username in accounts:
                    print("Username is already taken, please enter another username")
                    continue
                break
            while True:
                password = input("Enter Password : ").strip()
                if password == "":
                    print("Please enter a password")
                    continue
                break
            accounts[username] = [password, 0]
            saveAccounts()
            print("Account created successfully! Please log in.")
            login()
            return
        else:
            print("Please enter Yes or No")

def login():
    username = input("Enter Username: ").strip()
    while username not in accounts:
        print("Username not found. Please try again or type 'exit' to go back.")
        username = input("Enter Username: ").strip()
        if username.lower() == "exit":
            return
    else:
        password = input("Enter Password: ").strip()
        while accounts[username][0] == password:
            print(f"Welcome, {username}!")
            options(username)
        else:
            print("Incorrect password. Please try again.")
            login()

def options(username):
    while True:
        try:
            print("---------------------------------------------------")
            print(
                "1 - Show Balance\n" 
                "2 - Deposit\n" 
                "3 - Withdraw\n" 
                "4 - Show Transactions\n" 
                "5 - Exit")
            select = int(input("Please choose an option :"))
            if select == 1:
                print("---------------------------------------------------")
                print("You have chosen to check your balance")
                showBalance(username)
            elif select == 2:
                print("---------------------------------------------------")
                print("You have chosen to deposit")
                showBalance(username)
                deposit(username) 
            elif select == 3:
                print("---------------------------------------------------")
                print("You have chosen to withdraw")
                showBalance(username)
                withdraw(username)  
            elif select == 4:
                print("---------------------------------------------------")
                print("You have chosen to check your transactions")
                showTransactions(username) 
            elif select == 5:
                print("---------------------------------------------------")
                print("You have chosen to exit")  
                exit()   
            else:
                print("Please enter an option 1 - 5")
        except ValueError:
            print("Please enter an option 1 - 5")

def withdraw(username):
    action = "Withdraw"
    while True:
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            elif accounts[username][1]<= amount:
                print("You cannot withdraw more than your balance")
                continue
            elif accounts[username][1]>= amount:
                accounts[username][1] -= amount
                saveAccounts()
                print(f"${amount:.2f} deposited. New balance: ${accounts[username][1]:.2f}")
                saveTransactions(username, action, amount)
            break
        except ValueError:
            print("Please enter a valid number.")


def deposit(username):
    action = "Deposit"
    while True:
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            accounts[username][1] += amount
            saveAccounts()
            print(f"${amount:.2f} deposited. New balance: ${accounts[username][1]:.2f}")
            saveTransactions(username, action, amount)
            break
        except ValueError:
            print("Please enter a valid number.")

def loadTransactions():
    global transactions
    try:
        with open("transactions.json", "r") as tfile:
            transactions = json.load(tfile)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        transactions = {}

def showTransactions(username):
    if username in transactions and transactions[username]:
        print("Your transactions:")
        for t in transactions[username]:
            print(f"{t['action']}: ${t['amount']:.2f}")
    else:
        print("No transactions found.")

def saveTransactions(username, action, amount):
    if username not in transactions:
        transactions[username] = []
    transactions[username].append({
        "action": action,
        "amount": amount
    })
    with open("transactions.json", "a") as f:
        json.dump(transactions, f, indent=2)

def showBalance(username):
    balance = accounts[username][1]
    print(f"Your balance is [${balance}]")

def exit():
    while True:
        exit_option = input("Would you like to exit? (Yes/No) ").lower().strip()
        if exit_option == "yes":
            quit()
        elif exit_option == "no":
            return
        else: 
            print("Please enter Yes or No")

loadTransactions()          
loadAccounts()
description()
askAccount()

