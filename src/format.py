import rich
import shutil

def set_font_color(text: str, color: str) -> str:
    return f"[{color}]{text}[/{color}]"

sh_col_width = shutil.get_terminal_size().columns

