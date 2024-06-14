This is a program that mimics a banks mobile banking systems.

To have fun, kindly log in as an

                Admin: account_number = 131
                    pin = 3444

Through the cli, a user is first given 3 options;

        0. Exit the program
        1. Log in
        2. Create an account

each option has its own function.

    with option 1, a user will be prompted to enter his or her credentials an if the credentials match with what is in the database;

        a main menu function is called and more options are availble for the user, among them;
            1. Account balance check
            2. initiate a transaction
            3. Update an accounts details
            4. delete an account
            5. View statement
            6. View transactions in the database
            7. View accounts in the database
            8. Exit the program

    when a user decides to go with option 2 in the 3 options, he /she is prompted to enter details of the new account being created, every detail is validated in the code.

    Every detail of the program is persisted in the Database.

    The program's functionality is powered by Object Relational Methods/mapping using SQLite and Python
