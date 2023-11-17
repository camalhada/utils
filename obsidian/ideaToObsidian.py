import os
import pyperclip


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
    path_parts = parts[0].split('.')
    for part in path_parts:
        path += part + "/"
    return f"- [{parts[1]}]({path}{path_parts[-1]}.md#^{parts[1]})"


def html_link(ref):
    parts = ref.split('.')
    path = ""
    for part in parts[:-1]:
        if part == "html":
            continue
        path += part + "/"
    return f"- [{parts[-1]}]({path}{parts[-1]}.md)"


def run_loop():
    while True:
        # Print Menu
        print("What's the type of reference?")
        print("1 - Class")
        print("2 - Method")
        print("3 - Attribute")
        print("4 - HTML")
        print("5 - Exit")

        # Receive selection
        selection = input("Selection: ")

        # Check if the user wants to exit
        if selection == '5':
            print("Goodbye!")
            break

        # Receive input
        user_input = input("Enter your reference: ")

        clear_screen()

        # Check what input was given with a match statement
        match selection:
            case '1':
                output = class_link(user_input)
                print("Obsidian Link: ", output)
                pyperclip.copy(output)
            case '2':
                output = method_link(user_input)
                print("Obsidian Link: ", output)
                pyperclip.copy(output)
            case '3':
                output = attribute_link(user_input)
                print("Obsidian Link: ", output)
                pyperclip.copy(output)
            case '4':
                output = html_link(user_input)
                print("Obsidian Link: ", output)
                pyperclip.copy(output)
            case _:
                print("Invalid Type")
                continue


if __name__ == "__main__":
    # Run Loop
    run_loop()
