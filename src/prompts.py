import questionary
from rich import print, prompt
from .format import set_font_color, sh_col_width
from .database.db import pull_account_nums

def load_intro():
    # Print project title
    print("")
    text = set_font_color("*** Welcome to Sim BMS ***", "green")
    print(text.center(sh_col_width))

def prompt_menu():
    # Give user main menu options
    menu = questionary.select(
        "Select an action for account",
        ["Select", "Create", "Exit"]).ask()

    return menu

def account_selection():
    # Give options of accounts
    accounts: list = pull_account_nums()
    indexed_accs = [i[3:] for i in accounts]
    
    indexed_accs.append("Cancel")
    
    sel_prompt = questionary.select(
        "Select an account based on the last 4 digits",
        # Last four digits of accounts
        indexed_accs).ask()

    return sel_prompt

def error_message(message):
    print(f"[yellow]{message}[/yellow]")

def print_account_details(account):
    title = set_font_color("Account Details", "green").center(sh_col_width)

    print(title)
    print("Account Number:", account.acc_number)
    print(f"Balance: ${account.balance}")
    print(set_font_color("\nTip: Remember last four digits of account number", "red"))

def account_interface(account):
    print_account_details(account)

    prompt = questionary.select(
        "What would you like to do",
        choices=["deposit", "withdraw", "transfer", "menu"]).ask()
    
    return prompt