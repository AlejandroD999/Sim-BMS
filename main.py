from src import utils
from src.account import Account, AccountProcessor
from src.prompts import load_intro, prompt_menu
import questionary

# TODO Manage accounts using SQLite3

RUNNING = True
# Interface
while RUNNING:
    load_intro()

    menu_action = prompt_menu()

    if menu_action.lower() == "select":
        print(menu_action)

    elif menu_action.lower() == "create":
        print(menu_action)

    else:
        RUNNING = False
        continue

