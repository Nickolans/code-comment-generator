import sys
import pyperclip

def generate_comment_header(title: str) -> str:
    length = len(title) + 16

    top_border = "/" + "*" * (length)
    bottom_border = "*" * (length) + "/"

    formatted_title = f" * ----- {title} ----- *"

    return f"{top_border}\n{formatted_title}\n{bottom_border}"
    
def generate_comment_headerv2(title: str) -> str:
    length = len(title) + 16

    top_border = "/*"
    bottom_border = " */"
    middle_border = " " + ("*" * length)

    formatted_title = f" * ----- {title} ----- *"

    return f"{top_border}\n{middle_border}\n{formatted_title}\n{middle_border}\n{bottom_border}"

while True:
    inp = input('Enter header comment title: ')
    if str(sys.argv[1]) == "-v2":
            pyperclip.copy(generate_comment_headerv2(inp))
    else:
            pyperclip.copy(generate_comment_header(inp))
    
    print("Comment copied to clipboard!")
