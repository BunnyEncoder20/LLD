from abc import ABC, abstractmethod

# define factory product's interface
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Implementations
class StripePayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} using Stripe")

class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class PayTmPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} using PayTm")

# The Factory
class PaymentFactory:
    @staticmethod
    def get_payment_method(method: str) -> PaymentProcessor:
        if method == "stripe":
            return StripePayment()
        elif method == "paypal":
            return PayPalPayment()
        elif method == "paytm":
            return PayTmPayment()
        else:
            raise ValueError("Unsupported payment method")

# Client code
# Client doesn't care about the concrete classes
payment_method = PaymentFactory.get_payment_method("stripe")
payment_method.pay(100)

payment_method = PaymentFactory.get_payment_method("paypal")
payment_method.pay(200)

payment_method = PaymentFactory.get_payment_method("paytm")
payment_method.pay(300)
