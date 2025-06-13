import json
import datetime
from tkinter import *

def timeNow():
    global TIME
    TIME = datetime.datetime.now()

#Blank dictionaries to import existing data from external files
accounts = {}
transactions = {}

#A helper function that makes buttons
def styled_button(parent, text, command):
    return Button(parent, text=text, command=command, #inputs the configs and returns it back to the caller
                  font=("Arial", 14, "bold"), #Customizations
                  fg="white",
                  bg="black",
                  activebackground="black",
                  activeforeground="white",
                  bd=3, relief="raised")

#Saves account details into accounts.json file
def saveAccounts():
    with open("accounts.json", "w") as accountfile: 
        json.dump(accounts, accountfile, indent=2) 

#Loads account details from accounts.json file
def loadAccounts():
    global accounts #Makes the variable 'accounts' global outside of the function
    try:
        with open("accounts.json", "r") as a:
            accounts = json.load(a)
    except (FileNotFoundError, json.decoder.JSONDecodeError): #If the accounts.json file cannot be found it will proceed with a blank dictionary
        accounts = {}

#Fuction for printing the description of the code from an external file
def description():
    window = Tk() #Creates an instance of a window
    window.title("Bank Simulation Program") #The title of the window
    icon = PhotoImage(file="logo.png")  #Converts my logo.png file into a PhotoImage usable for Tkinter
    window.iconphoto(True,icon) #Displays my logo on the window
    window.configure(bg="black") #makes my background black
    with open("description.txt","r")as f: 
            description = f.read()
    label = Label(window, 
                  text=description, #a title for the window
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    label.pack()
    next = styled_button(window, "Next", lambda: [window.destroy(), askAccount()]) #button for going next
    next.pack(padx=10,pady=10)
    window.mainloop()

#Asks if the user have a bank account
def askAccount():
    window = Tk()
    window.title("Bank Simulation Program")
    icon = PhotoImage(file="logo.png")
    window.iconphoto(True,icon)
    window.configure(bg="black")
    login_button = styled_button(window, "Login", lambda: [window.destroy(), login()]) #this button leads to a login screen
    login_button.grid(row=0, column=0, padx=10, pady=10)
    create = styled_button(window, "Create Account", lambda: [window.destroy(), createAccount()]) #this button leads to a create screen
    create.grid(row=0, column=1, padx=10, pady=10)
    exit = styled_button(window, "Exit", exit_function) #this button leads to an exit screen
    exit.grid(row=0, column=2, padx=10, pady=10)
    window.mainloop()
    

#Constants for minimum and maximum age
MIN_AGE = 13
MAX_AGE = 18

#Create account function
def createAccount():
    window = Tk()
    window.title("Bank Simulation Program")
    icon = PhotoImage(file="logo.png")
    window.iconphoto(True,icon)
    window.configure(bg="black")
    label = Label(window, 
                  text="Create New Account",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    label.grid(row=0, column=0, columnspan=3, pady=10)
    username_label = Label(window, #side label next to the input box
                  text="Username:",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    username_label.grid(row=1, column=0)
    password_label = Label(window, #side label next to the input box
                  text="Password:",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    password_label.grid(row=2, column=0)
    age_label = Label(window,
                  text="Age:",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    username_input = Entry() #A box for the user to input their username
    username_input.grid(row=1, column=1, columnspan=2, padx=10)
    password_input = Entry(show="*")#A box for the user to input their password and it is hidden with *
    password_input.grid(row=2, column=1, columnspan=2, padx=10)
    check_label = Label(window, #side label next to the input box
                  text="Confirm Password:",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    check_label.grid(row=3, column=0)
    check_input = Entry(show="*")  #another input box to confirm the password
    check_input.grid(row=3, column=1, columnspan=2, padx=10)
    age_label.grid(row=4, column=0)
    age_input = Entry() #input box for the user's age
    age_input.grid(row=4, column=1, columnspan=2, padx=10)
    back = styled_button(window, "Back", lambda:[window.destroy(),askAccount()]) #sends the user back to the main screen
    back.grid(row=5,column=0,padx=10)
    #leads to the function that processes the data and makes an account
    submit = styled_button(window, "Submit", lambda: [create_submit(username_input,password_input,age_input,label,check_input,window)])
    submit.grid(row=5, column=1, columnspan=2, pady=15, padx=10)
    window.mainloop()

def create_submit(username_input, password_input, age_input, label,check_input, window):
    #grabs the data from the input boxes and puts it in a variable for easy handling
    username = username_input.get().strip()
    password = password_input.get().strip()
    check = check_input.get()
    age = age_input.get().strip()
    #checks and returns the following text if requirements are not met
    if username == "":
        label.config(text="Please enter a username")
        return
    elif " " in username:
        label.config(text="There must not be spaces within the username.")
        return
    elif username in accounts:
        label.config(text="Username is already taken, please enter another username")
        return
    if password == "":
        label.config(text="Please enter a password")
        return
    if check != password:
        label.config(text="Both passwords are not the same")
        return
    try:
        age = int(age)
        if age < MIN_AGE:
            label.config(text=f"You cannot be younger than {MIN_AGE} years old")
            return
        elif age > MAX_AGE:
            label.config(text=f"You cannot be older than {MAX_AGE} years old")
            return
        elif username == "":
            label.config(text="Please enter an age")
    except ValueError:
        label.config(text="Please enter a valid integer for age")
        return

    accounts[username] = [password, 0] #formats the data into a dictionary/list
    saveAccounts() #calls the save account function and saves it into external file
    window.destroy() #ends the create account window
    options(username) #opens the option menu window

#Log-in function, similar to createAccount function
def login():
    window = Tk()
    window.title("Bank Simulation Program")
    icon = PhotoImage(file="logo.png")
    window.iconphoto(True,icon)
    window.configure(bg="black")
    label = Label(window,
                  text="Log-in",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    label.grid(row=0, column=0, columnspan=3, pady=10)
    username_label = Label(window,
                  text="Username:",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    username_label.grid(row=1, column=0)
    password_label = Label(window,
                  text="Password:",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    password_label.grid(row=2, column=0)
    username_input = Entry()
    username_input.grid(row=1, column=1, columnspan=2, padx=10)
    password_input = Entry(show="*")
    password_input.grid(row=2, column=1, columnspan=2, padx=10)
    back = styled_button(window, "Back", lambda:[window.destroy(),askAccount()])
    back.grid(row=3,column=0,pady=15)
    submit = styled_button(window, "Submit", lambda:[login_submit(username_input,password_input,label,window)])
    submit.grid(row=3, column=1, pady=15, padx=25)
    window.mainloop()

#same as create_submit function but for logging in
def login_submit(username_input, password_input, label, window):
    username = username_input.get().strip()
    password = password_input.get().strip()
    if username == "":
        label.config(text="Please enter a username")
        return
    elif username not in accounts:
        label.config(text="Username not found")
        return
    if password == "":
        label.config(text="Please enter a password")
        return
    elif accounts[username][0] != password:
        label.config(text="Incorrect password. Please try again.")
        return
    window.destroy()
    options(username)

#Option choosing function
def options(username):
    window = Tk()
    window.title("Bank Options")
    window.configure(bg="black")
    label = Label(window, 
                text=f"Welcome, {username}!\nChoose an option:", 
                font=("Arial", 14, "bold"),
                fg="white",
                bg="black",
                pady=10)
    label.pack(pady=10)
    balance_button = styled_button(window, "Show Balance", lambda:[showBalance(username)])
    balance_button.pack(padx=5,pady=5) #shows the user's balance
    deposit_button = styled_button(window, "Deposit", lambda:[deposit(username)])
    deposit_button.pack(padx=5,pady=5) #opens a new window and lets the user input deposit amount
    withdraw_button = styled_button(window, "Withdraw", lambda:[withdraw(username)])
    withdraw_button.pack(padx=5,pady=5) #opens a new window and lets the user input withdraw amount
    transactions_button = styled_button(window, "Show Transactions", lambda:[showTransactions(username)])
    transactions_button.pack(padx=5,pady=5) #shows the user's transactions
    logout_button = styled_button(window, "Log-out", lambda:[logout(window)])
    logout_button.pack(padx=5,pady=5) #goes to log-out confirmation
    exit_button = styled_button(window, "Exit", exit_function)
    exit_button.pack(padx=5,pady=5) #opens exit menu
    window.mainloop()
    
#Withdrawing money function
def withdraw(username):
    def process_withdraw(): #function within the function to check withdrawals
        try:
            amount = float(amount_input.get()) #puts the input into a variable
            #checks and returns the following text if requirements are not met
            if amount <= 0:
                label.config(text=f"Please enter a positive amount.\n Current Balance : ${accounts[username][1]:.2f}")
                return
            if accounts[username][1] < amount:
                label.config(text=f"You cannot withdraw more than your balance.\n Current Balance : ${accounts[username][1]:.2f}")
                return
            accounts[username][1] -= amount #subtracts the amount from the user's balance
            saveAccounts() #updates the balance in the external file
            timeNow() #gets the time of the withdrawal
            saveTransactions(username, "Withdraw", amount, TIME) #saves the transaction 
            window.destroy() #ends the withdraw window
            #Displays a window for when the withdraw is completed
            result_window = Toplevel()
            result_window.title("Withdraw Complete")
            result_window.configure(bg="black")
            result_label = Label(result_window,
                                 text=f"${amount:.2f} withdrawn.\nNew balance: ${accounts[username][1]:.2f}", #tells the user their new balance
                                 font=("Arial", 12),
                                 fg="white",
                                 bg="black")
            result_label.pack(pady=10)
            result_label.pack()
            next = styled_button(result_window, "Next", result_window.destroy)
            next.pack(pady=5)
            result_window.mainloop()

        except ValueError:
            label.config(text="Please enter a valid number.")
    window = Toplevel() #creates a new window on top of an existing one
    #prevents the user from interacting with previous window unless the new window is closed
    window.transient() 
    window.grab_set()   
    window.title("Withdraw")
    window.configure(bg="black")
    label = Label(window, text=f"Enter amount to withdraw: \n Current Balance : ${accounts[username][1]:.2f}", 
                  font=("Arial", 12), fg="white", bg="black")
    label.grid(row=0,column=0,columnspan=2,pady=5)
    amount_input = Entry(window, font=("Arial", 12)) #input box for amount 
    amount_input.grid(row=1,column=0,columnspan=2,pady=5,padx=5)
    withdraw = styled_button(window, "Withdraw", process_withdraw) 
    withdraw.grid(row=2,column=0,pady=5)
    back = styled_button(window, "Back", window.destroy)
    back.grid(row=2,column=1,pady=5)
    window.mainloop()

#Depositing money function
def deposit(username):
    def process_deposit(): #function within the function to check deposits
        try:
            amount = float(amount_input.get()) #puts the input into a variable
            #checks and returns the following text if requirements are not met
            if amount <= 0:
                label.config(text="Please enter a positive amount.")
                return
            if amount > 1000000:
                label.config(text="You cannot deposit more than $1,000,000 at once")
                return
            accounts[username][1] += amount #adds the amount from the user's balance
            saveAccounts()
            timeNow()
            saveTransactions(username, "Deposit", amount, TIME)
            window.destroy()
            result_window = Toplevel()
            result_window.title("Deposit Complete")
            result_window.configure(bg="black")
            result_label = Label(result_window,
                                 text=f"${amount:.2f} deposited.\nNew balance: ${accounts[username][1]:.2f}",
                                 font=("Arial", 12),
                                 fg="white",
                                 bg="black")
            result_label.pack(pady=10)
            result_label.pack()
            next = styled_button(result_window, "Next", result_window.destroy)
            next.pack(pady=5)
            result_window.mainloop()

        except ValueError:
            label.config(text="Please enter a valid number.")
    window = Toplevel()
    window.transient()  
    window.grab_set()   
    window.title("Deposit")
    window.configure(bg="black")
    label = Label(window, 
                  text="Enter amount to deposit:", 
                  font=("Arial", 12), 
                  fg="white", 
                  bg="black")
    label.grid(row=0,column=0,columnspan=2,pady=5)
    amount_input = Entry(window, font=("Arial", 12))
    amount_input.grid(row=1,column=0,columnspan=2,pady=5,padx=5)
    deposit = styled_button(window, "Deposit", process_deposit)
    deposit.grid(row=2,column=0,pady=5)
    back = styled_button(window, "Back", window.destroy)
    back.grid(row=2,column=1,pady=5)
    window.mainloop()

#Grabs the transactions from an external file and puts it into a dictionary
def loadTransactions():
    #Makes the variable 'transactions' global outside of the function
    global transactions
    try:
        with open("transactions.json", "r") as tfile:
            transactions = json.load(tfile)
    #If the accounts.json file cannot be found or the data is invalid, it will proceed with a blank dictionary
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        transactions = {}

#For showing transactions
def showTransactions(username):
    window = Toplevel()
    window.transient()  
    window.grab_set()   
    window.title("Transactions")
    window.configure(bg="black")
    label = Label(window, text="Transactions", 
                  font=("Arial", 12), 
                  fg="white", 
                  bg="black",
                  pady=10)
    label.pack()
    frame = Frame(window, bg="black") #a frame is made within the window
    frame.pack()
    scrollbar = Scrollbar(frame) #inserts a scrollbar on the right and scrolls vertically
    scrollbar.pack(side=RIGHT, fill=Y) 
    listbox = Listbox(frame, #kept in the frame widget, a box for listing out all the transactions
                      yscrollcommand=scrollbar.set, 
                      font=("Arial", 12), 
                      fg="white", 
                      bg="black", 
                      width=50)
    #checks for transactions and puts it into the listbox
    if username in transactions and transactions[username]:
        for t in transactions[username]:
            listbox.insert(END, f"{t['time']} {t['action']}: ${t['amount']:.2f}")
    else:
        listbox.insert(END, "No transactions found.")
    listbox.pack()
    scrollbar.config(command=listbox.yview)
    back = styled_button(window, "Back", window.destroy)
    back.pack(pady=10)
    window.mainloop()

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
    window = Toplevel()
    window.transient()  
    window.grab_set()   
    window.title("Balance")
    window.configure(bg="black")
    balance = accounts[username][1]
    label = Label(window, text=f"Your balance is: ${balance:.2f}", #f string is used to display the balance
                 font=("Arial", 14), fg="white", bg="black", pady=20)
    label.pack(padx=5)
    back = styled_button(window, "Back", window.destroy)
    back.pack(pady=10)
    window.mainloop()

#Log out function 
def logout(window):
    confirm_window = Toplevel()
    confirm_window.transient()  
    confirm_window.grab_set()   
    confirm_window.title("Bank Simulation Program")
    icon = PhotoImage(file="logo.png")
    confirm_window.iconphoto(True,icon)
    confirm_window.configure(bg="black")
    label = Label(confirm_window,
                  text="Would you like to Log-out? (Yes/No)",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10)
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    #yes button takes user back to main screen
    yes = styled_button(confirm_window, "Yes", lambda:[confirm_window.destroy(),window.destroy(),askAccount()])
    yes.grid(row=1, column=0, padx=10, pady=10)
    #no button closes this window and returns to previous process
    no = styled_button(confirm_window, "No", confirm_window.destroy)
    no.grid(row=1, column=1, padx=10, pady=10)
    confirm_window.mainloop()

#Exit function
def exit_function():
    window = Toplevel()
    window.transient()  
    window.grab_set()   
    window.title("Bank Simulation Program")
    icon = PhotoImage(file="logo.png")
    window.iconphoto(True,icon)
    window.configure(bg="black")
    label = Label(window,
                  text="Would you like to exit? (Yes/No)",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10)
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    yes = styled_button(window, "Yes", quit) #yes button ends the code
    yes.grid(row=1, column=0, padx=10, pady=10)
    no = styled_button(window, "No", window.destroy) #no button closes the window and returns to previous process
    no.grid(row=1, column=1, padx=10, pady=10)
    window.mainloop()

#Loads all of the transactions when the code starts
loadTransactions()   
#Loads all of the accounts when the code starts       
loadAccounts()
#Displays the description, and starts the bank simulation
description()
