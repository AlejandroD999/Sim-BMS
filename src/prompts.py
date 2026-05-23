import questionary
from rich import print, prompt
from format import set_font_color, sh_col_width

def load_intro():
    text = set_font_color("*** Welcome to Sim BMS ***", "green")
    print(text.center(sh_col_width))

def prompt_menu():
    prompt_1 = questionary.select(
        "What would you like to do",
        ["Option 1", "Option 2", "Option 3"]).ask()

    return prompt_1

    
    
if __name__ == "__main__":
    load_intro()
    prompt_menu()