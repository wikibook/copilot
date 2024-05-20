# import pyperclip

# def clean_email():
#     """
#     The clipboard contains lines of text.
#     Clean up the text by removing any | or space
#     characters from the beginning of each line.
#     Replace the clipboard with the cleaned text.
#     """
#     text = pyperclip.paste()
#     lines = text.splitlines()
#     for i in range(len(lines)):
#         lines[i] = lines[i].lstrip(' |')
#     text = '
#     '.join(lines)

#     pyperclip.copy(text)

# if __name__ == '__main__':
#     clean_email()


import pyperclip


def clean_email():
    """
    The clipboard contains lines of text.
    Clean up the text by removing any | or space
    characters from the beginning of each line.
    Replace the clipboard with the cleaned text.
    """
    text = pyperclip.paste()
    lines = text.splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i].lstrip(" |")
    text = "\n".join(lines)

    pyperclip.copy(text)


if __name__ == "__main__":
    clean_email()
