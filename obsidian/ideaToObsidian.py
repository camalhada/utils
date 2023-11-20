import os
import pyperclip
import sys


def clear_screen():
    # Check the operating system and clear the screen accordingly
    os.system('cls' if os.name == 'nt' else 'clear')


def class_link(ref):
    parts = ref.split('.')
    path = ""
    for part in parts:
        path += part + "/"
    return f"- [{parts[-1]}]({path}{parts[-1]}.md)"


def method_link(ref):
    parts = ref.split('#')
    path = ""
    for part in parts[0].split('.'):
        path += part + "/"
    return f"- [{parts[1]}]({path}{parts[1]}.md)"


def attribute_link(ref):
    parts = ref.split('#')
    path = ""
    if "_" in parts[1]:
        tag = parts[1].replace("_", "-")
    else:
        tag = parts[1]
    path_parts = parts[0].split('.')
    for part in path_parts:
        path += part + "/"
    return f"- [{parts[1]}]({path}{path_parts[-1]}.md#^{tag})"


def html_link(ref):
    parts = ref.split('.')
    path = ""
    for part in parts[:-1]:
        if part == "html":
            continue
        path += part + "/"
    return f"- [{parts[-1]}]({path}{parts[-1]}.md)"


def print_menu():
    # Print Menu
    print("+-------------------------------+")
    print("| What's the type of reference? |")
    print("+-------------------------------+")
    print("| 1 | Class                     |")
    print("+-------------------------------+")
    print("| 2 | Method                    |")
    print("+-------------------------------+")
    print("| 3 | Attribute                 |")
    print("+-------------------------------+")
    print("| 4 | HTML                      |")
    print("+-------------------------------+")
    print("| 5 | Exit                      |")
    print("+-------------------------------+")


def select_checker(selection):
    # Check if user wants to exit
    if selection == '5' or selection == 'exit':
        print("<====[ Goodbye! ]====>")
        sys.exit()
    elif selection == 'clear':
        clear_screen()
        return 'skip'
    match selection:
        case 'class':
            return '1'
        case 'method':
            return '2'
        case 'attribute':
            return '3'
        case 'html':
            return '4'
        case _:
            print("[ Error ] === [ Invalid Type ]")
            return 'skip'


def valid_reference(ref, selection):
    if selection == '1' or selection == '4':
        if "." not in ref:
            return False
        return True
    elif selection == '2' or selection == '3':
        if "#" not in ref:
            return False
        elif "." not in ref:
            return False
        return True


def process_input(selection, user_input):
    # Check if user_inout is empty
    if user_input == "":
        print("[ Error ] === [ Empty Reference ]")
        return 'skip'

    # Check if the reference is a valid reference
    if not valid_reference(user_input, selection):
        print("[ Error ] === [ Invalid Reference ]")
        return 'skip'

    # Check what input was given with a match statement
    match selection:
        case '1':
            return class_link(user_input)
        case '2':
            return method_link(user_input)
        case '3':
            return attribute_link(user_input)
        case '4':
            return html_link(user_input)
        case _:
            return 'skip'


def run_loop():
    while True:
        print_menu()

        # Receive selection
        selection = input("[ Selection ] ===> ")
        # Remove Trailing and Leading Whitespace
        selection.strip()
        # Preprocess selection
        selection = select_checker(selection)
        # If selection is invalid, skip
        if selection == 'skip':
            continue

        # Receive input
        user_input = input("Enter your reference: ")
        # Remove Trailing and Leading Whitespace
        user_input.strip()
        # Process user_input and selection
        output = process_input(selection, user_input)
        # If input is invalid, skip
        if output == 'skip':
            continue

        # Print output
        print("[ Obsidian Link ] === [ ", output, " ]")
        # Copy output to clipboard
        pyperclip.copy(output)


if __name__ == "__main__":
    # Run Loop
    run_loop()
