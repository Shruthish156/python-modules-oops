#INHERITANCE
#inheritance means : child class is acqiure the data and methods of the parents class (main class)
class Bank:                                       #parent class
    def __init__(self,balance,ac_holder,ac_no):
        self.balance=balance
        self.ac_holder=ac_holder
        self.ac_no=ac_no

class SBI(Bank):                                  #child class it access the information of parent class also it inherite the sbi                         
    def deposit(self,amount):
        self.balance +=amount
        print(f"the deposit amount is :{self.balance}")

class BOB(SBI):                                   #child class it access the information of class sbi and class bank  it inherite the bob
    def withdraw(self,amount):
        self.balance -=amount
        print(f"the withdraw amount is :{self.balance}")

class HDFC(BOB):                                 #child class it access the information if class bob,sbi and bank it inherite the hdfc
    def intrest(self):
        self.balance=self.balance*25
        print(f"the intrest amount is :{self.balance}")
B1=BOB(75000,"AIENGSHRUTHISHAMR","3255556255")
B1.withdraw(500)
B1.deposit(600)
#B1=Bank(75000,"AIENGSHRUTHISHAMR","3255556255")


