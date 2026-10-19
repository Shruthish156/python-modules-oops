#POLYMORPHISM
#define: it is a oops concept same mathods/function but have different behaviour in object
class UPI:
    def pay_amount(self,acc_holder,amount):
        self.acc_holder=acc_holder
        self.amount=amount
        if  amount>0 and amount<50000:
            print(f"The paying amount {amount} is valid through UPI!!!")
        else:
            print("Payment is failed through UPI mode ")

class NET_BANKING:
    def pay_amount(self,acc_holder,amount):
        self.acc_holder=acc_holder
        self.amount=amount
        if amount>0:
            print(f"The paying mode is valid and succesfull u can pay {amount} amount!!")
        else:
            print("Not valid it is not support through NET_Banking")

class CREDIT_CARD:
    def pay_amount(self,card_holder,amount):
        self.card_holder=card_holder
        self.amount=amount
        if amount>0:
            print("U can use credit card for your payment journey!! amount is {amount}")
        else:
            print("Invalid")

payment_modes=[UPI(),NET_BANKING(),CREDIT_CARD()]
for payment_mode in payment_modes:
    payment_mode.pay_amount("shruthisha",65000)

"""
In the above example obey polymorphism because it has same methods for all calss like "pay_amount " and have different behaviour 
"""