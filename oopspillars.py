#SIMPLE bank amount checking
class BankAccount:
    def __init__(self,account_no,balance,account_holder):      #data
        self.account_no=account_no
        self.balance=balance
        self.account_holder=account_holder

    def deposit(self,amount):                                 #action with data
        self.balance +=amount

    def withdraw(self,amount):                                #action with data
        self.balance -= amount
personal_account=BankAccount(816401895621,4500,"AIENGshruthisha")      #create the data
personal_account.deposit(4000)
print(f"the deposit balance is :{personal_account.balance}")
personal_account.withdraw(1000)
print(f"the withdraw balance is :{personal_account.balance}")


