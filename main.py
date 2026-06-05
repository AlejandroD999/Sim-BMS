from src.utils import generate_acc_num
from src.acc import Account, TransferService 
from src.prompts import load_intro, prompt_menu, account_selection, error_message, print_account_details, selection_menu
from src.database.db import create_account, pull_account_details

MINIMUM_BALANCE = 5
RUNNING = True

def test_transfer():
    acc_1_dets = pull_account_details("7194")
    acc_2_dets = pull_account_details("6001")

    acc_1 = Account(acc_1_dets[0], acc_1_dets[1])
    acc_2 = Account(acc_2_dets[0], acc_2_dets[1])

    service = TransferService()

    service.transfer(acc_1, acc_2, 20)

    print_account_details(acc_1)
    print("======================================")
    print_account_details(acc_2)

# Interface
while RUNNING:

    load_intro()

    menu_action = prompt_menu()

    if menu_action.lower() == "select":
        chosen_acc = account_selection()

        if chosen_acc == "Cancel":
            continue

        acc_details = pull_account_details(chosen_acc)
        acc = Account(acc_details[0], acc_details[1])

        print_account_details(acc)
        
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
        
        print_account_details(new_acc)
        # Pause
        input("Press Enter to continue")


    else:
        RUNNING = False
        continue

