class Account:
    def __init__(self, acc_number, routing_number, amount=0):
        self.amount = amount
        self.acc_number = acc_number
        # For third party exchange
        self.routing_number = routing_number
    
    def deposit(self):
        pass
    
    def withdraw(self):
        pass

class AccountProcessor:
    def __init__(self, account: Account):
        self.account = account
    def display_balance(self):
        return self.account.amount



"""
class TransferService:
    def transfer(self, from_acc, to_acc, amount):
        pass
"""





