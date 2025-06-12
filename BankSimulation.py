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
    except (FileNotFoundError, json.decoder.JSONDecodeError):
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
    button1 = Button(window, text="Login")
    button1.config(command=lambda: [window.destroy(), login()],
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    button1.grid(row=0, column=0, padx=10, pady=10)
    button2 = Button(window, text="Create Account")
    button2.config(command=lambda: [window.destroy(), createAccount()],
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    button2.grid(row=0, column=1, padx=10, pady=10)
    button3 = Button(window, text="Exit")
    button3.config(command= exit,
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    button3.grid(row=0, column=2, padx=10, pady=10)
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
    age_label = Label(window,
                  text="Age:",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    username_input = Entry()
    username_input.grid(row=1, column=1, columnspan=2, padx=10)
    password_input = Entry(show="*")
    password_input.grid(row=2, column=1, columnspan=2, padx=10)
    check_label = Label(window,
                  text="Confirm Password:",
                  font=("Arial",12),
                  fg="white",
                  bg="black",
                  padx=10,
                  pady=10
                  )
    check_label.grid(row=3, column=0)
    check_input = Entry(show="*")
    check_input.grid(row=3, column=1, columnspan=2, padx=10)
    age_label.grid(row=4, column=0)
    age_input = Entry()
    age_input.grid(row=4, column=1, columnspan=2, padx=10)
    back = Button(window,text="Back")
    back.config(font=("Arial", 14, "bold"),
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white",
                bd=3,
                relief="raised",
                padx=5,
                pady=5,
                command=lambda:[window.destroy(),askAccount()])
    back.grid(row=5,column=0,padx=10)
    submit = Button(window,text="Submit")
    submit.config(font=("Arial", 14, "bold"),
                  fg="white",
                  bg="black",
                  activebackground="black",
                  activeforeground="white",
                  bd=3,
                  relief="raised",
                  padx=5,
                  pady=5,
                  command=lambda: [create_submit(username_input,password_input,age_input,label,check_input,window)])
    submit.grid(row=5, column=1, columnspan=2, pady=15, padx=10)
    window.mainloop()

def create_submit(username_input, password_input, age_input, label,check_input, window):
    username = username_input.get().strip()
    password = password_input.get().strip()
    check = check_input.get()
    age = age_input.get().strip()
    if " " in username:
        label.config(text="There must not be spaces within the username.")
        return
    if username == "":
        label.config(text="Please enter a username")
        return
    if username in accounts:
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

    accounts[username] = [password, 0]
    saveAccounts()
    window.destroy()
    options(username)

#Log-in function
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
    back = Button(window,text="Back")
    back.config(font=("Arial", 14, "bold"),
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white",
                bd=3,
                relief="raised",
                padx=5,
                pady=5,
                command=lambda:[window.destroy(),askAccount()])
    back.grid(row=3,column=0,pady=15)
    submit = Button(window,text="Submit")
    submit.config(font=("Arial", 14, "bold"),
                  fg="white",
                  bg="black",
                  activebackground="black",
                  activeforeground="white",
                  bd=3,
                  relief="raised",
                  padx=5,
                  pady=5,
                  command=lambda: [login_submit(username_input,password_input,label,window)])
    submit.grid(row=3, column=1, pady=15, padx=25)
    window.mainloop()

def login_submit(username_input, password_input, label, window):
    username = username_input.get().strip()
    password = password_input.get().strip()
    if username not in accounts:
        label.config(text="Username not found")
        return
    if username == "":
        label.config(text="Please enter a username")
        return
    if accounts[username][0] != password:
        label.config(text="Incorrect password. Please try again.")
        return
    if password == "":
        label.config(text="Please enter a password")
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
    balance_button = Button(window, text="Show Balance")
    balance_button.config(font=("Arial", 12, "bold"),
                          fg="white",
                          bg="black",
                          activebackground="black",
                          activeforeground="white",
                          bd=3,
                          relief="raised",
                          width=20,
                          command=lambda: [showBalance(username)])
    balance_button.pack(padx=5,pady=5)
    deposit_button = Button(window, text="Deposit")
    deposit_button.config(font=("Arial", 12, "bold"),
                          fg="white",
                          bg="black",
                          activebackground="black",
                          activeforeground="white",
                          bd=3,
                          relief="raised",
                          width=20,
                          command=lambda: [deposit(username)])
    deposit_button.pack(padx=5,pady=5)
    withdraw_button = Button(window, text="Withdraw")
    withdraw_button.config(font=("Arial", 12, "bold"),
                          fg="white",
                          bg="black",
                          activebackground="black",
                          activeforeground="white",
                          bd=3,
                          relief="raised",
                          width=20,
                          command=lambda: [withdraw(username)])
    withdraw_button.pack(padx=5,pady=5)
    transactions_button = Button(window, text="Show Transactions")
    transactions_button.config(font=("Arial", 12, "bold"),
                          fg="white",
                          bg="black",
                          activebackground="black",
                          activeforeground="white",
                          bd=3,
                          relief="raised",
                          width=20,
                          command=lambda: [showTransactions(username)])
    transactions_button.pack(padx=5,pady=5)
    logout_button = Button(window, text="Log-out")
    logout_button.config(font=("Arial", 12, "bold"),
                          fg="white",
                          bg="black",
                          activebackground="black",
                          activeforeground="white",
                          bd=3,
                          relief="raised",
                          width=20,
                          command=lambda: [logout(window)])
    logout_button.pack(padx=5,pady=5)
    exit_button = Button(window, text="Exit")
    exit_button.config(font=("Arial", 12, "bold"),
                          fg="white",
                          bg="black",
                          activebackground="black",
                          activeforeground="white",
                          bd=3,
                          relief="raised",
                          width=20,
                          command=exit)
    exit_button.pack(padx=5,pady=5)
    window.mainloop()
    
#Withdrawing money function
def withdraw(username):
    def process_withdraw():
        try:
            amount = float(amount_input.get())
            if amount <= 0:
                label.config(text=f"Please enter a positive amount.\n Current Balance : ${accounts[username][1]:.2f}")
                return
            if accounts[username][1] < amount:
                label.config(text=f"You cannot withdraw more than your balance.\n Current Balance : ${accounts[username][1]:.2f}")
                return
            accounts[username][1] -= amount
            saveAccounts()
            timeNow()
            saveTransactions(username, "Withdraw", amount, TIME)
            window.destroy()
            result_window = Toplevel()
            result_window.title("Withdraw Complete")
            result_window.configure(bg="black")
            result_label = Label(result_window,
                                 text=f"${amount:.2f} withdrawn.\nNew balance: ${accounts[username][1]:.2f}",
                                 font=("Arial", 12),
                                 fg="white",
                                 bg="black")
            result_label.pack(pady=10)
            result_label.pack()
            next = Button(result_window, text="Next")
            next.config(font=("Arial", 12, "bold"),
                        fg="white",
                        bg="black",
                        activebackground="black",
                        activeforeground="white",
                        bd=3,
                        relief="raised",
                        command=result_window.destroy)
            next.pack(pady=5)
            result_window.mainloop()

        except ValueError:
            label.config(text="Please enter a valid number.")
    window = Toplevel()
    window.transient()  
    window.grab_set()   
    window.title("Withdraw")
    window.configure(bg="black")
    label = Label(window, text=f"Enter amount to withdraw: \n Current Balance : ${accounts[username][1]:.2f}", 
                  font=("Arial", 12), fg="white", bg="black")
    label.grid(row=0,column=0,columnspan=2,pady=5)
    amount_input = Entry(window, font=("Arial", 12))
    amount_input.grid(row=1,column=0,columnspan=2,pady=5,padx=5)
    withdraw = Button(window,text="Withdraw")
    withdraw.config(font=("Arial", 12, "bold"),
                    fg="white",
                    bg="black",
                    activebackground="black",
                    activeforeground="white",
                    bd=3,
                    relief="raised",
                    command=process_withdraw)
    withdraw.grid(row=2,column=0,pady=5)
    back = Button(window,text="Back")
    back.config(font=("Arial", 12, "bold"),
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white",
                bd=3,
                relief="raised",
                command=window.destroy)
    back.grid(row=2,column=1,pady=5)
    window.mainloop()

#Depositing money function
def deposit(username):
    def process_deposit():
        try:
            amount = float(amount_input.get())
            if amount <= 0:
                label.config(text="Please enter a positive amount.")
                return
            if amount > 1000000:
                label.config(text="You cannot deposit more than $1,000,000 at once")
                return
            accounts[username][1] += amount
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
            next = Button(result_window,text="Next")
            next.config(font=("Arial", 12, "bold"),
                        fg="white",
                        bg="black",
                        activebackground="black",
                        activeforeground="white",
                        bd=3,
                        relief="raised",
                        command=result_window.destroy)
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
    deposit = Button(window,text="Deposit")
    deposit.config(font=("Arial", 12, "bold"),
                   fg="white",
                   bg="black",
                   activebackground="black",
                   activeforeground="white",
                   bd=3,
                   relief="raised",
                   command=process_deposit)
    deposit.grid(row=2,column=0,pady=5)
    back = Button(window,text="Back",)
    back.config(font=("Arial", 12, "bold"),
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white",
                bd=3,
                relief="raised",
                command=window.destroy)
    back.grid(row=2,column=1,pady=5)
    window.mainloop()

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
    frame = Frame(window, bg="black")
    frame.pack()
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(frame, 
                      yscrollcommand=scrollbar.set, 
                      font=("Arial", 12), 
                      fg="white", 
                      bg="black", 
                      width=50)
    if username in transactions and transactions[username]:
        for t in transactions[username]:
            listbox.insert(END, f"{t['time']} {t['action']}: ${t['amount']:.2f}")
    else:
        listbox.insert(END, "No transactions found.")
    listbox.pack()
    scrollbar.config(command=listbox.yview)
    back = Button(window, 
                  text="Back", 
                  command=window.destroy, 
                  fg="white", 
                  bg="black", 
                  font=("Arial",15))
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
    label = Label(window, text=f"Your balance is: ${balance:.2f}",
          font=("Arial", 14), fg="white", bg="black", pady=20)
    label.pack(padx=5)
    back = Button(window, text="Back")
    back.config(fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black",
                command=window.destroy)
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
    yes = Button(confirm_window, text="Yes")
    yes.config(command=lambda: [confirm_window.destroy(),window.destroy(),askAccount()],
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    yes.grid(row=1, column=0, padx=10, pady=10)
    no = Button(confirm_window, text="No")
    no.config(command=confirm_window.destroy,
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    no.grid(row=1, column=1, padx=10, pady=10)
    confirm_window.mainloop()

#Exit function
def exit():
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
    yes = Button(window, text="Yes")
    yes.config(command=quit,
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    yes.grid(row=1, column=0, padx=10, pady=10)
    no = Button(window, text="No")
    no.config(command=window.destroy,
                fg="white",
                bg="black",
                font=("Arial",15),
                activebackground="white",
                activeforeground="black")
    no.grid(row=1, column=1, padx=10, pady=10)
    window.mainloop()

#Loads all of the transactions when the code starts
loadTransactions()   
#Loads all of the accounts when the code starts       
loadAccounts()
#Prints the description, and starts the bank simulation
description()
