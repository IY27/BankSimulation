import json

accounts = {}

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
    try:
        age = int(input("Enter your age : "))
        while age < MIN_AGE:
            print("You cannot be younger than 13 years old")
            age = int(input("Enter your age : "))
        while age > MAX_AGE:
            print("You cannot be older than 18 years old")
            age = int(input("Enter your age : "))
        else:
            print("You are eligible to create an account")
            return
    except ValueError:
        print("Please enter an integer")
        askAge()

def createAccount():
    makeaccount = input("Would you like to create an account? (Yes/No) :  ").lower().strip()
    if makeaccount == "no":
        exit()
    elif makeaccount == "yes":
        askAge()
        username = input("Enter Username : ").strip()
        while " " in username:
            print("There must not be spaces within the username.")
            username = input("Enter Username : ").strip()
        while username == "":
            print("Please enter an username")
            username = input("Enter Username : ").strip()
        while username in accounts:
            print("Username is already taken, please enter another username")
            username = input("Enter Username : ").strip()
        else:
            password = input("Enter Password : ").strip()
            while password == "":
                print("Please enter a password")
                password = input("Enter Password : ").strip()
            else:
                accounts[username] = [password, 0]
                saveAccounts()
                login()
    else:
        print("Please enter Yes or No")
        createAccount()

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
            options()
        else:
            print("Incorrect password. Please try again.")
            login()

def options():
    print(
    "1 - Show Balance\n" \
    "2 - Deposit\n" \
    "3 - Withdraw\n" \
    "4 - Show Transactions\n" \
    "5 - Exit")
    while True:
        print("Please choose an option :")
        try:
            select = int(input(""))
            if select == 1:
                showBalance()
                print("You have chosen to check your balance")
            elif select == 2:
                deposit() 
                print("You have chosen to deposit")
            elif select == 3:
                withdraw()  
                print("You have chosen to withdraw")
            elif select == 4:
                showTransactions() 
                print("You have chosen to check your transactions")
            elif select == 5:
                exit()
                print("You have chosen to exit")     
            else:
                print("Please enter an option 1 - 5")
        except ValueError:
            print("Please enter an option 1 - 5")

def withdraw():
    None

def deposit():
    None

def showTransactions():
    None

def saveTransactions():
    None

def showBalance():
    None

def exit():
    while True:
        exit_option = input("Would you like to exit? (Yes/No) ").lower().strip()
        if exit_option == "yes":
            quit()
        elif exit_option == "no":
            return
        else: 
            print("Please enter Yes or No")
            
loadAccounts()
description()
askAccount()

