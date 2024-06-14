

from helpers import (
    exit_program, 
    login,      
    create_account,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            login()
        elif choice == "2":
            create_account()


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Login")
    print("2. Create an account")


if __name__ == "__main__":
    main()
