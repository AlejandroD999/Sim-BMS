import questionary as qs
from .database import db
from .prompts import error_message 
class Account:
    def __init__(self, acc_number, balance=0):
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amt: float):
        if 0 <= amt <= 250000:
            self.balance += amt
            db.update_balance(self.acc_number, self.balance)

        else:
            error_message("Invalid deposit amount: maximum is $250,000")
    def withdraw(self, amt):

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
        if not from_acc or not to_acc:
            error_message("A sender and a receiver must be provided")
            return
        if from_acc.withdraw(amt):
            to_acc.deposit(amt)        

if __name__ == "__main__":
    acc_1 = Account(24, 54, 500)
    acc_2 = Account(293, 20384, 500)
    while True:
        menu = qs.select("Select an option", ["status", "send"]).ask()

        if menu == "status":
            print(f"Acc_1: {acc_1.balance}")        
            print(f"Acc_2: {acc_2.balance}")

        else:
            amount = float(input(f"How much would you like to send to Account_2?: "))
            service = TransferService()

            service.transfer(acc_1, acc_2, amount)










