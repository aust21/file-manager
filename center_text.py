import os

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80

def center_text(text):
    terminal_width = get_terminal_width()
    text_width = len(text)
    if text_width >= terminal_width:
        return text
    padding = (terminal_width - text_width) // 2
    centered_text = ' ' * padding + text
    return centered_text

def center(text):
    centered_text = center_text(text)
    return centered_text
