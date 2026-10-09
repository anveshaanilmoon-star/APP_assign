from abc import ABC,abstractmethod
class Paymentstrategy(ABC):
    @abstractmethod
    def pay(self,amount:float)->None:
        """All concrete payment methods must implement this method."""
        pass

class CreditCardPayment(Paymentstrategy):
    def __init__(self,card_number:str):
        self.card_number=card_number
    def pay(self,amount:float)->None:
        print(f"Paid ${amount} using credit card ending in {self.card_number[-4:]}.")

class PayPalPayment(Paymentstrategy):
    def __init__(self,email:str):
        self.email=email
    def pay(self,amount:float)->None:
        print(f"Paid ${amount} using PayPal account:{self.email}.")

class BitcoinPayment(Paymentstrategy):
    def __init__(self,cryptographic_address:str):
        self.cryptographic_address=cryptographic_address
    def pay(self,amount:float)->None:
        print(f"Paid ${amount} using bitcoin wallet with cryptographic address:{self.cryptographic_address}.") 
class Paymentprocessor:
    def __init__(self,amount:float,Payment_strategy:Paymentstrategy):
        self.amount=amount
        self.payment_strategy=Payment_strategy
    def set_payment_strategy(self,payment_strategy=Paymentstrategy):
        """Allows swapping strategies at runtime."""
        self.payment_strategy=payment_strategy
    def checkout(self)->None:
     self.payment_strategy.pay(self.amount)

cart_total=150.00
processor=Paymentprocessor(cart_total,CreditCardPayment("1234-5678-9876-5432"))
processor.checkout()

processor.set_payment_strategy(PayPalPayment("user@example.com"))
processor.checkout()