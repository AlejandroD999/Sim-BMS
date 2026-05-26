from src.utils import generate_acc_num
from src.account import Account, AccountProcessor
from src.prompts import load_intro, prompt_menu, error_message
import questionary

MINIMUM_BALANCE = 5
RUNNING = True

# Interface
while RUNNING:

    load_intro()

    menu_action = prompt_menu()

    if menu_action.lower() == "select":
        print(menu_action)

    elif menu_action.lower() == "create":
        
        try:
            starting_balance = int(input("Enter a starting balance: "))

        except ValueError:
            error_message("The Balance must be a number")
            continue    
        
        if starting_balance <= MINIMUM_BALANCE:
            error_message(f"Balance must be greater than 5")
            continue


        new_acc = Account(generate_acc_num(), starting_balance)

        # TODO save new_acc into database


    else:
        RUNNING = False
        continue

