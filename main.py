from src.utils import generate_acc_num
from src.acc import Account, AccountProcessor
from src.prompts import load_intro, prompt_menu, account_selection, error_message, account_details
from src.database.db import create_account

MINIMUM_BALANCE = 5
RUNNING = True

# Interface
while RUNNING:

    load_intro()

    menu_action = prompt_menu()

    if menu_action.lower() == "select":
        chosen_acc = account_selection()

        if chosen_acc == "Cancel":
            continue
        # TODO Do something with chosen acc (more menus)

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
        
        account_details(new_acc)


    else:
        RUNNING = False
        continue

