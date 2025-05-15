def description():
    with open('description.txt','r')as f:
            description = f.read()
            print(description)
            print()

def askAccount():
    while True:
        askaccount = input("Do you have a bank account? : (Yes/No) ").lower().strip()
        if askaccount == "yes":
            login()
        elif askaccount == "no":
            makeaccount = input("Would you like to create an account? : (Yes/No) ").lower().strip()
            if makeaccount == "yes":
                createAccount()
            elif makeaccount == "no":
                exit_option = input("Would you like to exit? (Yes/No) ").lower().strip()
                if exit_option == "yes":
                    quit()
                elif exit_option == "no":
                    continue
                else:
                    print("Please enter Yes or No")
            else:
                print("Please enter Yes or No")
        else: 
            print("Please enter Yes or No")

def createAccount():
    None

def login():
    None

def options():
    None

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
    None

description()
askAccount()