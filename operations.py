# Importing
from dbconnections import *
from data_logs import *

# ===============================================[withdraw Class ]======================================================
class withdraw:
     def __init__(self, ID , PIN , b , cash, atmbc, userhist, userday, usertime):
        self.id = ID
        self.pin = PIN
        self.b = b
        self.cash = cash
        self.atmbc = atmbc # atm balance
        self.userhist = userhist
        self.userday = userday
        self.usertime = usertime

     def gui_balance_check(self):

         check1st = date_logs(self.id, self.userhist, self.userday, self.usertime)
         first = check1st.first_operation_check()  # Check if its First Operation For User
         if first == 0:  # if user First Time Per Day
             st1 = 1
             if self.cash <= 5000:  # check if input lower than 5000
                 if self.cash < self.atmbc:  # check if (atm) has enough balance
                     if self.b >= self.cash:  # check if (user) has enough balance
                         self.b -= self.cash  #suptract input cash from user
                         self.atmbc -= self.cash  #suptract input cash from atm
                         insertbalance = DBOperation(self.id, self.pin)
                         insertbalance.add_balance(self.b)  # add New Balance To user
                         insertbalance.atm_balance_update(self.atmbc)  # Add New Balance To ATM

                         # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         opertaion = "withdraw - %s" % self.cash  # Operation Row Content
                         datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, st1)
                         datalogs.insert_operation(self.cash, 0)  # Insert Values in Logs Table
                         # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                         check = 1  # SUcc
                     else:
                         check = 0  #  User Dont Have Enough Money
                 else:
                     check = 999  # ATM Dont have Enough Money
             else :
                 check = 666  # bigger than 5000
         else:
             st1 = 0  # if Not First time Per Day
             opertaion = "withdraw - %s" % self.cash  # Operation Content
             datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, st1)
             totalwith = datalogs.get_any_withdraw()  # Get Total Withdraw
             totaldep = datalogs.get_any_totaldepposite()  # Get Total Deppsite
             inputingCash = self.cash + totalwith  # Total Withdraw Per Day

             if inputingCash <= 5000:  # Check Total withdraw per Day
                 if self.cash < self.atmbc:  # check if (atm) has enough balance
                     if self.b >= self.cash:  # check if (user) has enough balance
                         self.b -= self.cash  # Suptract balance from user
                         self.atmbc -= self.cash  # Suptract balance from ATM
                         insertbalance = DBOperation(self.id, self.pin)
                         insertbalance.add_balance(self.b)  # add New Balance To user
                         insertbalance.atm_balance_update(self.atmbc)  # Add New Balance To ATM

                         datalogs.insert_operation(inputingCash, totaldep)  # Insert Values in Logs

                         check = 1  # SUcc
                     else:
                         check = 0  #  User Dont Have Enough Money
                 else :
                     check = 999  # ATM Dont have Enough Money
             else :
                 check = 222  # Check u Cant Withdrow more than 5000 Per Day

         return check


# ===============================================[depposite Class ]=====================================================
class depposite:

    def __init__(self, ID, PIN, b, cash, atmbc,userhist, userday, usertime):
        self.id = ID
        self.pin = PIN
        self.b = b
        self.cash = cash
        self.atmbc = atmbc
        self.userhist = userhist
        self.userday = userday
        self.usertime = usertime


    def add_balance(self):

        check1st = date_logs(self.id, self.userhist, self.userday, self.usertime)
        first = check1st.first_operation_check()  # Check if its First Operation For User

        if first == 0:  # check if User First Time
            st1 = 1  # First Time Per Day
            if self.cash <= 40000:  # Check if input Lower Than 40000
                self.b += self.cash
                self.atmbc += self.cash
                InsertBalance = DBOperation(self.id, self.pin)
                InsertBalance.add_balance(self.b)
                InsertBalance.atm_balance_update(self.atmbc)  # Add New Balance To ATM

                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                opertaion = "depposite + %s" % self.cash  # Operation Row Content
                datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, st1)
                datalogs.insert_operation(0, self.cash)  # insert values in logs
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                check = 1  # succ
            else:
                check = 0  # Cant Depppsite More than 40000
        else:
            st1 = 0
            datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime)
            totalwith = datalogs.get_any_withdraw()  # Get Total Withdraw
            totaldep = datalogs.get_any_totaldepposite() # Get Total depposite
            inputingCash = totaldep + self.cash

            if inputingCash <= 40000:
                self.b += self.cash
                self.atmbc += self.cash
                InsertBalance = DBOperation(self.id, self.pin)
                InsertBalance.add_balance(self.b)
                InsertBalance.atm_balance_update(self.atmbc)  # Add New Balance To ATM
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                opertaion = "depposite + %s" % self.cash
                datalogs = date_logs(self.id, self.userhist, self.userday, self.usertime, opertaion, st1)
                datalogs.insert_operation(totalwith, totaldep + self.cash)
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                check = 1
            else:
                check = 222  # Cant Add More than 40000 PerDay
        return check


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
