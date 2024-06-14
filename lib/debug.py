
from models.__init__ import CONN, CURSOR
from models.transaction import Transaction
from models.account import Account

import ipdb


def reset_database():
    Transaction.drop_table()
    Transaction.create_table()
    Account.drop_table()
    Account.create_table()


    # Create seed data
    
    kelly2 = Account.create("Kelly", "matui", 131, 3444, "male", 5000) #admin

    kelly1 = Account.create("Kelly", "matui", 1310383499, 3444, "male", 5000)
    account2 = Account.create("Kenly", "otui", 13103834555, 3445, "female", 430)
    account3 = Account.create("daisy", "fitui", 1310385599, 2333, "female", 4600)
    account4 = Account.create("gelly", "Kigtui", 131038556499, 2334, "male", 7800)
    account5 = Account.create("anelly", "ytui", 131038333555, 3222, "male", 2300)
    

    Transaction1= Transaction.create(5005, "22/DEC", "deposit", 1310383499, 131038333555)
    Transaction2= Transaction.create(55, "22/DEC", "deposit", 13103834555, 131038556499)
    Transaction3= Transaction.create(5405, "22/DEC", "deposit", 1310385599, 1310383499)
    Transaction4= Transaction.create(6005, "22/DEC", "deposit", 131038556499, 13103834555)
    Transaction5= Transaction.create(1205, "22/DEC", "withdrawal", 131038333555, 1310383499)

    

   



reset_database()


ipdb.set_trace()
