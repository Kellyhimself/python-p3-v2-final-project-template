#import the two classes
from models.transaction import Transaction
from models.account import Account
from helpers2 import (
    delete_account, 
    transact, 
    update_account, 
    get_balance, 
    get_transactions, 
    transactions_in_db, 
    accounts_in_db
)


def exit_program():
    print("Goodbye!")
    exit()

#Function to display all accounts in the database
def list_accounts():
    accounts = Account.get_all()
    for account in accounts:
        print(account)


#find an account by account number
def find_account_by_account_number():
    account_number = input("Enter the account number: ")
    details = Account.find_by_account_number(account_number)
    print(details) if details else print (f"account {account_number} not found")

#find an account by name
def find_by_name():
    first_name = input("Enter account's first name...: ")
    last_name = input("Enter account's last name...: ")
    details = Account.find_by_name(first_name, last_name)
    print(details) if details else print (f"account with the name {first_name} {last_name}not found")
#find an account by its id
def find_account_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the accounts's id: ")
    details = Account.find_by_id(id_)
    print(details) if details else print(f'Account {id_} not found')

#function to set our gender input
def gender():
    while True:
        gender = input("Enter your gender (male/female/others): ")
        if gender.lower() not in ["male", "female", "others"]:
            print("Invalid gender. Please enter a valid gender.")
            continue
        else:
            break
    return gender

#login function and the afterward menu display function
def logged_in_menu(account_number):
        account = Account.find_by_account_number(account_number)
        name = account.first_name
        print(f"logged in as {name}")
        print("Please select an option")
        print("1. Check account balance")
        print("2. Transact")
        print("3. Update your account details")
        print("4. Delete the account")        
        print("5. View statement")
        print("6. Transactions in the database")        
        print("7. Accounts in the database")
        print("8. Exit the program")
        print("98 More")

        choice = input("> ")
        if choice == "1":
            get_balance()
            exit_program()
        elif choice == "2":
            transact()
            exit_program()
        elif choice =="3": 
            update_account() 
            exit_program()   
        elif choice == "4":
            delete_account()
            exit_program()
        elif choice == "7":
            accounts_in_db()
            exit_program()
        elif choice == "5":
            get_transactions()
            exit_program()
        elif choice =="6":
            transactions_in_db()
            exit_program()
        elif choice =="8":
            exit_program()
        elif choice == "98":
            pass
          

def login():
    account_number = input("Enter account number: ")
    pin = input("Enter user pin: ")
    if Account.login(account_number, pin):
        logged_in_menu(account_number)        
    else:
        print("invalid credentials")

# Create an account
def create_account():
    global gender  # Declare the gender variable as global
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    account_number = input("Enter account number: ")
    pin = input("Enter a random four digit pin: ")
    gender = gender()  # Call the gender() function to get valid gender input
    initial_deposit = input("Enter initial deposit: ")

    try:
        account = Account.create(first_name, last_name, int(account_number), pin, gender, int(initial_deposit))
        print(f'Success: {account}')
        exit_program()
    except Exception as exc:
        print("Error creating the account, account can only be a number ", exc)
        exit_program()





        




