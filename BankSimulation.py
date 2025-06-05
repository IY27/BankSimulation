import json
import datetime
from tkinter import *

def timeNow():
    global TIME
    TIME = datetime.datetime.now()

#Blank dictionaries to import existing data from external files
accounts = {}
transactions = {}

#Saves account details into accounts.json file
def saveAccounts():
    with open("accounts.json", "w") as accountfile: 
        json.dump(accounts, accountfile, indent=2)

#Loads account details from accounts.json file
def loadAccounts():
    #Makes the variable 'accounts' global outside of the function
    global accounts
    try:
        with open("accounts.json", "r") as a:
            accounts = json.load(a)
    #If the accounts.json file cannot be found it will proceed with a blank dictionary
    except FileNotFoundError:
        accounts = {}

#Fuction for printing the description of the code from an external file
def description():
    #Creates an instance of a window
    window = Tk()
    #The title of the window
    window.title("Bank Simulation Program")
    #Converts my logo.png file into a PhotoImage usable for Tkinter
    icon = PhotoImage(file="logo.png")
    #Displays my logo on the window
    window.iconphoto(True,icon)
    window.configure(bg="black")
    with open("description.txt","r")as f:
            description = f.read()
    label = Label(window,
                  text=description,
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    label.pack()
    button = Button(window,text="Next")
    button.config(command=lambda: [window.destroy(), askAccount()],
                  fg="white",
                  bg="black",
                  font=("Arial",15),
                  activebackground="white",
                  activeforeground="black"
                  )
    button.pack(padx=10,pady=10)
    window.mainloop()

#Asks if the user have a bank account
def askAccount():
    window = Tk()
    window.title("Bank Simulation Program")
    icon = PhotoImage(file="logo.png")
    window.iconphoto(True,icon)
    window.configure(bg="black")
    label = Label(window,
                  text="Do you have a bank account? (Yes/No)",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    label.grid(row=0, column=0, columnspan=3, pady=10)
    button1 = Button(window, text="Yes")
    button1.config(command=login,
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    button1.grid(row=1, column=0, padx=10, pady=10)
    button2 = Button(window, text="No")
    button2.config(command=createAccount,
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    button2.grid(row=1, column=1, padx=10, pady=10)
    button3 = Button(window, text="Exit")
    button3.config(command=exit,
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    button3.grid(row=1, column=2, padx=10, pady=10)
    window.mainloop()
    

#Constants for minimum and maximum age
MIN_AGE = 13
MAX_AGE = 18

#Asks the user for their age
def askAge():
    while True:
        try:
            age = int(input("Enter your age : "))
            #User less than the age of 13, loops back
            if age < MIN_AGE:
                print("You cannot be younger than 13 years old")
            #User more than the age of 18, loops back
            elif age > MAX_AGE:
                print("You cannot be older than 18 years old")
            #Entering an age between 13-18 will return the user back to the createAccount() function
            else:
                print("You are eligible to create an account")
                return
        #Captures value errors 
        except ValueError:
            print("Please enter an integer")

#Create account function
def createAccount():
    while True:
        #Asks if user wants to create an account
        makeaccount = input("Would you like to create an account? (Yes/No) :  ").lower().strip()
        #If no, the code proceeds with the exit() function
        if makeaccount == "no":
            exit()
            return
        #If yes, it will proceed with askAge() function
        elif makeaccount == "yes":
            askAge()
            while True:
                #After finishing askAge() function, it will ask user to make a username
                username = input("Enter Username : ").strip()
                #Loops the user back if username has spaces in it
                if " " in username:
                    print("There must not be spaces within the username.")
                    continue
                #Loops the user back if username is blank
                if username == "":
                    print("Please enter a username")
                    continue
                #Loops the user back if username is already in the system
                if username in accounts:
                    print("Username is already taken, please enter another username")
                    continue
                break
            #After meeting all the requirements, the code asks the user for the password
            while True:
                password = input("Enter Password : ").strip()
                #Loops the user back if password is blank
                if password == "":
                    print("Please enter a password")
                    continue
                break
            #Formats how the data will be saved into the external file
            accounts[username] = [password, 0]
            #Saves account
            saveAccounts()
            print("Account created successfully! Please log in.")
            #Proceeds with login function
            login()
            return
        else:
            print("Please enter Yes or No")

#Log-in function
def login():
    #Asks user for their username
    username = input("Enter Username: ").strip()
    #Loops back if username is not within the system
    while username not in accounts:
        print("Username not found. Please try again or type 'exit' to go back.")
        username = input("Enter Username: ").strip()
        if username.lower() == "exit":
            return
    #Meets the criteria and asks the password
    else:
        password = input("Enter Password: ").strip()
        #If the password matches with the associated username, it proceeds to option function
        while accounts[username][0] == password:
            print(f"Welcome, {username}!")
            options(username)
        #If the password does not match it loops back
        else:
            print("Incorrect password. Please try again.")
            login()

#Option choosing function
def options(username):
    while True:
        try:
            #Displays all the options the user can make
            print("---------------------------------------------------")
            print(
                "1 - Show Balance\n" 
                "2 - Deposit\n" 
                "3 - Withdraw\n" 
                "4 - Show Transactions\n" 
                "5 - Exit")
            select = int(input("Please choose an option :"))
            #If statements for which option the user chooses
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
                #Loops back if user inputs something that is not an option
                print("Please enter an option 1 - 5")
        except ValueError:
            #Loops back if input is not an integer
            print("Please enter an option 1 - 5")

#Withdrawing money function
def withdraw(username):
    #Checks if the user balance is = 0 if so returns back to the option menu
    if accounts[username][1] == 0:
        print("You cannot make any withdrawals as your bank balance is at $0")
        return
    #Variable for the transaction function to identify the action
    action = "Withdraw"
    while True:
        try:
            #Asks for how much the user wants to withdraw
            amount = float(input("Enter amount to withdraw: $"))
            #Loops back if amount is less than 0
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            #Loops back if amount is more than the current balance
            elif accounts[username][1]< amount:
                print("You cannot withdraw more than your balance")
                continue
            #If amount is less than the current balance 
            elif accounts[username][1]>= amount:
                #Actual process where the balance is being subtracted
                accounts[username][1] -= amount
                #Renews the account balance 
                saveAccounts()
                print(f"${amount:.2f} withdrawed. New balance: ${accounts[username][1]:.2f}")
                timeNow()
                #Saves this transaction to the external file
                saveTransactions(username, action, amount, TIME)
            break
        except ValueError:
            #Prints this if the input is not a number
            print("Please enter a valid number.")

#Depositing money function
def deposit(username):
    #Variable for the transaction function to identify the action
    action = "Deposit"
    while True:
        try:
            #Asks for how much the user wants to deposit
            amount = float(input("Enter amount to deposit: $"))
            #Loops back if amount is less than 0
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            #Process for adding the amount to the balance
            accounts[username][1] += amount
            #Renews the account balance 
            saveAccounts()
            print(f"${amount:.2f} deposited. New balance: ${accounts[username][1]:.2f}")
            timeNow()
            #Saves this transaction to the external file
            saveTransactions(username, action, amount, TIME)
            break
        except ValueError:
            #Prints this if the input is not a number
            print("Please enter a valid number.")

#
def loadTransactions():
    #Makes the variable 'transactions' global outside of the function
    global transactions
    try:
        with open("transactions.json", "r") as tfile:
            transactions = json.load(tfile)
    #If the accounts.json file cannot be found or the data is invalid, it will proceed with a blank dictionary
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        transactions = {}

#Shows transactions function
def showTransactions(username):
    #Checks if there is an existing transaction for the username
    if username in transactions and transactions[username]:
        print("Your transactions:")
        for t in transactions[username]:
            print(f"{t["time"]} {t["action"]}: ${t["amount"]:.2f}")
    else:
        #Prints this if no exisitng transactions are found
        print("No transactions found.")

#Saves transaction function
def saveTransactions(username, action, amount, TIME):
    #Checks existing username is not in transactions, it will create a new dictionary for that username
    if username not in transactions:
        transactions[username] = []
    transactions[username].append({
        "time": TIME.strftime("%c"),
        "action": action,
        "amount": amount
    })
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=2)

#Show balance function
def showBalance(username):
    balance = accounts[username][1]
    #Displays balance
    print(f"Your balance is [${balance}]")

#Exit function
def exit():
    while True:
        #Asks user if they want to exit
        exit_option = input("Would you like to exit? (Yes/No) ").lower().strip()
        #Ends the code if input is yes
        if exit_option == "yes":
            quit()
        #Returns to previous operations if input is no
        elif exit_option == "no":
            return
        else: 
            #Prints this if input is neither yes or no
            print("Please enter Yes or No")

#Loads all of the transactions when the code starts
loadTransactions()   
#Loads all of the accounts when the code starts       
loadAccounts()
#Prints the description, and starts the bank simulation
description()
