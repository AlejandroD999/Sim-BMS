import questionary as qs
from .database import db
from .prompts import error_message 

class Account:
    def __init__(self, acc_number, balance=0):
            self.acc_number: str = str(acc_number)

            try:
                self.balance: float = float(balance)
            except ValueError:
                error_message("Balance must be a number")
        
    def deposit(self, amt: float):
        if 0 <= amt <= 250000:
            self.balance += amt
            db.update_balance(self.acc_number, self.balance)

        else:
            error_message("Invalid deposit amount: maximum is $250,000")
    def withdraw(self, amt):
        if type(amt) != float:
            try:
                amt = float(amt)
            except ValueError:
                error_message("Amount must be a number")
                return
            
        if amt <= self.balance and amt > 0:
            self.balance -= amt
            db.update_balance(self.acc_number, self.balance)
            return True
        
        else:
            error_message("Invalid withdrawal amount")
            return False
        
class AccountProcessor:
    def __init__(self, account: Account):
        self.account = account

    def display_balance(self):
        return self.account.balance

class TransferService:
    def transfer(self, from_acc, to_acc, amt):
        try:
            amt = float(amt)
        except ValueError:
            error_message("Amount must be a number")
            return

        if not from_acc or not to_acc:
            error_message("A sender and a receiver must be provided")
            return

        if from_acc == to_acc:
            error_message("Sender and receiver can't be the same")    
    
        if from_acc.withdraw(amt):
            to_acc.deposit(amt)        