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


def run_loop():
    while True:
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

        # Receive selection
        selection = input("[ Selection ] ===> ")

        # Check if the user wants to exit
        if selection == '5':
            print("<====[ Goodbye! ]====>")
            break
        elif selection == 'clear':
            clear_screen()
            continue

        # Receive input
        user_input = input("Enter your reference: ")
        if user_input.strip() == "":
            print("[ Error ] === [ Invalid Reference ]")
            continue

        # Check what input was given with a match statement
        match selection:
            case '1':
                if "." not in user_input:
                    print("[ Error ] === [ Invalid Reference ]")
                    continue
                output = class_link(user_input)
                print("Obsidian Link: ", output)
                pyperclip.copy(output)
            case '2':
                if "#" not in user_input:
                    print("[ Error ] === [ Invalid Reference ]")
                    continue
                elif "." not in user_input:
                    print("[ Error ] === [ Invalid Reference ]")
                    continue
                output = method_link(user_input)
                print("[ Obsidian Link ] === [ ", output, " ]")
                pyperclip.copy(output)
            case '3':
                if "#" not in user_input:
                    print("[ Error ] === [ Invalid Reference ]")
                    continue
                elif "." not in user_input:
                    print("[ Error ] === [ Invalid Reference ]")
                    continue
                output = attribute_link(user_input)
                print("[ Obsidian Link ] === [ ", output, " ]")
                pyperclip.copy(output)
            case '4':
                if "." not in user_input:
                    print("[ Error ] === [ Invalid Reference ]")
                    continue
                output = html_link(user_input)
                print("[ Obsidian Link ] === [ ", output, " ]")
                pyperclip.copy(output)
            case _:
                print("[ Error ] === [ Invalid Type ]")
                continue


if __name__ == "__main__":
    # Run Loop
    run_loop()
