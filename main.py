# Importing
import time
from operations import *
from data_logs import *


# =======================================[ User Info ]==================================================================
ID = 1234  # --------------/////------/////-----> Ramon Ramon
PIN = 0  # default value
ID2 = 0  # default value
from time import gmtime, strftime
userday = strftime("%d", gmtime())
usertime = strftime("%H:%M:%S")
userhist = time.asctime()

# =======================================[ Window1.. Check Login ]======================================================
option1 = 0
option2 = 3

print(time.asctime())


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from time import gmtime, strftime
print strftime("%a, %d %b %Y %H:%M:%S +0000")


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

while option1 == 0 and option2 != 0:
    print "Enter ur PIN"
    PIN = int(input())  # --------------/////------/////-----> Ramon

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@               Admin Check                        @@@@@@
    if ID == 1 and PIN == 1:
        flag = 2
        break
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    UserLogin = DBOperation(ID, PIN)
    LoginCheck = UserLogin.login_check()  # Return 1 for Success Return 0 for Fail

    flag = 0  # Check if User Pass Login
    if LoginCheck == 1:
        print "Welcome To ATM"
        option1 = 1
        flag = 1

    # =========/Class DBOperation/========
    # ===      Get User Balance        ===
        UserBalance = DBOperation(ID, PIN)
        b = UserBalance.balance_check()
    # ====================================

    else:
        option2 -= 1
        print "Wrong PIN  %s Chance" % option2

# =========/Class DBOperation/========
# ===      Get User Balance        ===
    object1 = DBOperation(ID)
    atmbc = object1.atm_balance_check()
# ====================================

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@                                 [ Admin Window ]                                                       @@@@@@@

if flag == 2:
    print "press 1 to Check ATM Balnce"
    print "press 2 to  depposite Balance To ATM"
    x = int(input())
    if x == 1:
        AtmBalance = DBOperation(ID, PIN)
        balance = AtmBalance.atm_balance_check()
        print "ATM Balance Is %s" % balance
    if x == 2:
        print "Enter Cash"
        x = int(input())

        # =========/Class ATMFill/====================
        # ===      Return ATM Balnce               ===
        AtmBalanceInsert = ATMFill(x)
        existbalance = AtmBalanceInsert.filling()
        # =============================================

        print "ATM Balance Now is  %s" % existbalance

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# =======================================[ Windows2..Operations ]=======================================================

elif flag == 1:
    print "press 1 to Enter withdraw "
    print "press 2 to Enter depposite "
    print "press 3 to Enter CheckBalance "
    print "press 4 to Enter Transfer "
    print "press 5 to Check History "
    x = int(input())  # --------------/////------/////-----> Ramon (Button Return Number 1 to 4)


# ========================================[ Windows3..withdraw ]========================================================
    if x == 1:
        print "Enter Cash"
        cash = int(input())  # --------------/////------/////-----> Ramon (Get Number From Button Or Input Label)

        # ===========/Class withdraw/============
        # ===      Return 0 or 1              ===
        get_money = withdraw(ID, PIN, b, cash, atmbc, userhist, userday, usertime)
        check = get_money.gui_balance_check()
        # =======================================
        if check == 999:
            print "Srry ATM Dont Have Enought Money"
            print(time.asctime())
        elif check == 1:
            print "withdraw Done Your balance Now is %s" % get_money.b
            print(time.asctime())
        elif check == 666:
            print "Max Value To withdraw 5000"
        elif check == 222:
            print "You Cant withdraw More Than 5000 per Day"
        else:
            print "You Dont Have Enough Money"
            print(time.asctime())


# ========================================[ Windows4..depposite ]=======================================================
    elif x == 2:
        print "Enter Cash"
        cash = int(input())  # --------------/////------/////-----> Ramon (Get Number From Button Or Input Label)

    # =============/class depposite/==============
    # ====      Add Balance                    ===
        get_money2 = depposite(ID, PIN, b, cash, atmbc, userhist, userday, usertime)
        check = get_money2.add_balance()
    # ============================================
        if check == 1:
            print "Your Balance Now is %s" % get_money2.b
            print(time.asctime())
        elif check == 222:
            print "You Cant Deposite More than 40000 Per Day"
        elif check == 0:
            print "Max Value TO Deppsite 40000"


# ========================================[ Windows5..CheckBalance ]====================================================
    elif x == 3:
        pass  # Fix Comments warning

    # =============/class CheckBalance/=================
    # ====          Print balance                    ===
        UserBalanceCheck = DBOperation(ID, PIN)
        balancedChecked = UserBalanceCheck.balance_check()
    # ==================================================
        print "Your Balance is %s" % balancedChecked
        print(time.asctime())


# ========================================[ Windows6..Transfer ]========================================================
    elif x == 4:
        print "Enter ID Which U want to Trans For"
        ID2 = int(input())  # --------------/////------/////-----> Ramon (ID Of Other User)

    # =============/class DBOperation/==========
    # ====          Return 0 or 1            ===
        IdCheck = DBOperation(ID2)
        Check = IdCheck.id_check()
    # ==========================================
        if Check == 1:
            print "Enter Cash"
            cash = int(input())  # --------------/////------/////-----> Ramon (Get Number From Button Or Input Label)

        # =============/class transfer/==================
        # ====          Return 0 or 1                 ===
            UserTrans = transfer(ID, ID2, b, cash)
            check = UserTrans.transfer_balance()
        # ===============================================

            if check == 1:
                print "You Trans %s To ID = %s Your Balance Now is %s" % (UserTrans.cash, UserTrans.id2, UserTrans.b)
                print(time.asctime())
            else:
                print "You Dont Have Enought"
        else:
            print "Wrong ID"
# ========================================[ Windows7..History ]========================================================
    elif x == 5:
        datalogs = date_logs(ID)
        results = datalogs.get_history()
        # Print History
        print "---------------------------------------------------------------------------------------"
        print "|      Date               |       Operation      |  Total widthdrow | TotalDeppsite    |"
        print "---------------------------------------------------------------------------------------"
        for result in results:

            print "|%s |  %s   |        %s      |       %s        |" % (result[2], result[5], result[7], result[8])
            print "---------------------------------------------------------------------------------------"

else:
    print "You Dont Have More Chance"

