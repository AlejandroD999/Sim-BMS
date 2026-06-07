from src.utils import generate_acc_num
from src.acc import Account, TransferService 
from src.format import set_font_color
from src.prompts import header, prompt_menu, account_selection, error_message, print_account_details, account_interface
from src.database.db import create_account, pull_account_details
from rich import print as r_print

MINIMUM_BALANCE = 5
RUNNING = True

# Interface
while RUNNING:

    header("|_-_Welcome to Sim BMS_-_|", "yellow")

    menu_action = prompt_menu()

    if menu_action.lower() == "select":
        chosen_acc = account_selection()

        if chosen_acc == "Cancel":
            continue

        acc_details = pull_account_details(chosen_acc)
        acc = Account(acc_details[0], acc_details[1])
        transfer_service = TransferService()
        
        # Account Interface
        acc_action = account_interface(acc)

        while acc_action.lower() != "menu":

            if acc_action.lower() == "status":
                print_account_details(acc)            

            elif acc_action.lower() == "deposit":           
                try:     
                    deposit_amount = float(input("Deposit Amount: "))
                    acc.deposit(deposit_amount)

                except ValueError:
                    error_message("Amount must be a number")

            elif acc_action.lower() == "withdraw":
                try:     
                    withdrawal_amount = float(input("Withdrawal Amount: "))
                    acc.withdraw(withdrawal_amount)

                except ValueError:
                    error_message("Amount must be a number")

            elif acc_action.lower() == "transfer":
                header("Transfer Service", "yellow")

                r_print(set_font_color("Select a Receiver:", "green"))

                receiver_details = pull_account_details(account_selection([acc.acc_number]))
                receiver = Account(receiver_details[0], receiver_details[1])

                amount_to_send = input("Amount to Send: ")

                transfer_service.transfer(acc, receiver, amount_to_send)
                r_print(set_font_color(f"Successfully sent: ${amount_to_send}", "green"))

            input("\nPress Enter to continue ")
            acc_action = account_interface(acc)
        

    elif menu_action.lower() == "create":
        
        try:
            starting_balance = int(input("Enter a starting balance: "))

        except ValueError:
            error_message("The Balance must be a number")
            continue    
        
        if starting_balance <= MINIMUM_BALANCE:
            error_message(f"Balance must be greater than 5")
            continue


        new_acc =  Account(generate_acc_num(), starting_balance)
        
        # Save acc to database
        create_account(new_acc.acc_number, new_acc.balance)
        
        print_account_details(new_acc)
        # Pause
        input("Press Enter to continue")

    else:
        RUNNING = False
        continue

