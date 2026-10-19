#ABSTRACTION
#define : it is an oops concept that hide implementation details and show features/methods to user
#in abstraction mainly two parts are there (ABC :abstraction base case and @abstractmethod)

from abc import ABC ,abstractmethod
class UPI(ABC):
    def __init__(self,amount):
        self.amount=amount

    @abstractmethod                               #abstraction
    def pay_amount(self):
        print(f"THe PAYMENT APP THROUGH NET_BANKING AMOUNT ${self.amount} PAID")

class NET_BANKING(UPI):
    def pay_amount(self):
        print(f"THe PAYMENT APP THROUGH NET_BANKING AMOUNT ${self.amount} PAID")

class CREDIT_CARD(UPI):
    def pay_amount(self):
        print(f"THe PAYMENT APP THROUGH CREDIT_CARD AMOUNT ${self.amount} PAID")

class DEBIT_CARD(UPI):
    def pay_amount(self):
        print(f"THe PAYMENT APP THROUGH CREDIT_CARD AMOUNT ${self.amount} PAID")

#polymorphism
payment_modes=[NET_BANKING(500),CREDIT_CARD(500),DEBIT_CARD(500)]
for payment_mode in payment_modes:
    payment_mode.pay_amount()