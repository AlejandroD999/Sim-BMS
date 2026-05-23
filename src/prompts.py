import questionary
from rich import print
from format import set_font_color, sh_col_width

def load_intro():
    text = set_font_color("*** Welcome to Sim BMS ***", "green")
    print(text.center(sh_col_width))


if __name__ == "__main__":
    load_intro()