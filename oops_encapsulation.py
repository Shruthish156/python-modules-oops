#OOPS : it is object oriented programing language that create object contain data and methods

#ENCAPSULATION

#defination : 
"""
 it is a oops concept that wrapping the data and methods into a sinlge class and protecting the data by restricting the direct 
access to it and improve security and maintainability

"""
class ATM:
    print("+=====WELCOME TO THE BANK OF BARODA ATM=======")
    def __init__(self,balance,atm_holder):
        self.__balance=balance                        #private -we do not direct access the data it will difficult
        self.__atm_holder=atm_holder             #private 

    def show_balance(self):
        #print(f"the total remaining balance amount in ATM is : {self.__balance}")
        return self.__balance

    def deposit(self,amount):
        if amount>0:
            print(f"the account holder name is:{self.__atm_holder}")
            self.__balance+=amount               #private
            print(f"the deposited amount $ is:{self.__balance}")
        else:
            print("this bank is not support to deposit: ")

    def withdraw(self,amount):
        if amount<50000 and amount>=500:
            self.__balance -=amount             #private
            print(f"your withdraw amount $ is : {self.__balance}")
           
           
        else:
            print("invalid withdraw this bank not support to your withdraw amount $:")
#BOB_ATM=ATM(50)
BOB_ATM=ATM(50,"AIENGSHRUTHISHA") 
BOB_ATM.deposit(8000)
BOB_ATM.withdraw(7050)
print(BOB_ATM.show_balance())                  #function calling




