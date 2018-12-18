# Importing
from dbconnections import *

# ===============================================[withdraw Class ]======================================================
class withdraw:
     def __init__(self, ID , PIN , b , cash, atmbc):
        self.id = ID
        self.pin = PIN
        self.b = b
        self.cash = cash
        self.atmbc = atmbc # atm balance

     def gui_balance_check(self):
         if self.cash < self.atmbc:  # check if (atm) has enough balance
            if self.b >= self.cash:  # check if (user) has enough balance
                self.b -= self.cash
                self.atmbc -= self.cash
                insertbalance = DBOperation(self.id, self.pin)
                insertbalance.add_balance(self.b) # add New Balance To user
                insertbalance.atm_balance_update(self.atmbc) # Add New Balance To ATM
                check = 1
            else:
                check = 0
         else :
             check = 999
         return check


# ===============================================[depposite Class ]=====================================================
class depposite:

    def __init__(self, ID, PIN, b, cash, atmbc):
        self.id = ID
        self.pin = PIN
        self.b = b
        self.cash = cash
        self.atmbc = atmbc

    def showing(self):
        login1 = DBOperation(self.id, self.pin)

    def add_balance(self):
        self.b += self.cash
        self.atmbc += self.cash
        InsertBalance = DBOperation(self.id, self.pin)
        InsertBalance.add_balance(self.b)
        InsertBalance.atm_balance_update(self.atmbc)  # Add New Balance To ATM

# ===============================================[transfer Class ]=====================================================
class transfer:

    def __init__(self, ID, ID2, b, cash):
        self.id = ID  # user ID
        self.id2 = ID2  # user PIN
        self.b = b
        self.cash = cash

    def transfer_balance(self):
        if self.b >= self.cash:
            self.b -= self.cash
            InsertBalance = DBOperation(self.id)
            InsertBalance.add_balance(self.b)

            #Inster Balance To user 1
            get_user2_balance = DBOperation(self.id2)
            user2 = get_user2_balance.balance_check()

            user2 += self.cash
            # Insert Balance To user 2
            InsertBalance = DBOperation(self.id2)
            InsertBalance.add_balance(user2)

            check = 1
        else:
            check = 0
        return check


# ===============================================[Fill ATM ]=====================================================
class ATMFill:

    def __init__(self, atmfill):
        self.atmfill = atmfill

    def filling(self):
        incash = DBOperation(1)
        existbalance = incash.atm_balance_check()
        existbalance += self.atmfill
        incash.atm_balance_update(existbalance)
        return existbalance
