import questionary
from rich import print
from .format import set_font_color, sh_col_width
from .database.db import pull_account_nums

def header(message, color):
    # Print project title
    print("")
    text = set_font_color(message, color)
    print(text.center(sh_col_width))

def prompt_menu():
    # Give user main menu options
    menu = questionary.select(
        "Select an action for account",
        ["Select", "Create", "Exit"]).ask()

    return menu

def account_selection(exceptions: list = None):
    # Give options of accounts
    accounts: list = pull_account_nums()

    if exceptions:
        for exception in exceptions:
            if exception in accounts:
                accounts.remove(exception)
            else:
                error_message("Invalid Exception")
    
    indexed_accs = [i[3:] for i in accounts]
    
    indexed_accs.append("Cancel")
    
    sel_prompt = questionary.select(
        "Last 4 digits of account",
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
        choices=["Deposit", "Withdraw", "Transfer", "Menu"]).ask()
    
    return prompt