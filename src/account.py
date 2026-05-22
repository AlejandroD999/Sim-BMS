class Account:
    def __init__(self, acc_number, routing_number, amount=0):
        self.amount = amount
        self.acc_number = acc_number
        # For third party exchange
        self.routing_number = routing_number
    
    def deposit(self, amt: float):
        if 0 <= amt <= 250000:
            self.amount = amt
        else:
            print("Invalid Deposit Amount: Maximum is $250,000")
    
    def withdraw(self, amt):
        if amt <= self.amount and amt > 0:
            self.amount -= amt
        else:
            print("Invalid Withdrawal Amount")
        

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





