import questionary
from rich import print, prompt
from .format import set_font_color, sh_col_width

def load_intro():
    # Print project title
    print("")
    text = set_font_color("*** Welcome to Sim BMS ***", "green")
    print(text.center(sh_col_width))

def prompt_menu():
    # Give user main menu options
    prompt_1 = questionary.select(
        "Select an action for account",
        ["Select", "Create", "Exit"]).ask()

    return prompt_1

def account_selection():
    # Give options of accounts
    pass 

def error_message(message):
    print(f"[yellow]{message}[/yellow]")
