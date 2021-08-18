import pyperclip

def confirmation(m="Please confirm: Y/N: -> "):
    """Request confirmation from user

    :param m: string message
    :return: boolean
    """
    c = ["Y", "N"]
    while True:
        choice = input(m).upper()
        if choice not in c:
            print("Please choose from these options: {}".format(c))
        elif choice == "Y":
            return True
        else:
            return False

def get_integer(m, min_, max_, mod = 0):
    """Request valid integer from user.

    :param m: string message
    :param min_: integer
    :param max_: integer
    :return: integer
    """
    cont = True
    while cont is True:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("please enter an integer value")
            continue
        if my_integer < min_:
            print("The value you have entered is too low")
            continue
        elif my_integer > max_:
            if mod != 0:
                mod_integer = my_integer%mod
                print("The number of Symbols is {}".format(mod))
                print("Your key has been changed to {} mod {} = {}".format(my_integer, mod, mod_integer))
                return mod_integer
            print("The value you have entered is too high")
            continue
        return my_integer


def get_string(m, max_ = 300, min_=2):
    """Request and return valid string from user.

    :param m: string message
    :param max_: integer , max length of string
    :param min_: integer , min length of string
    :return: string
    """
    cont = True
    while cont is True:
        response_string = input(m)
        if len(response_string) < min_:
            print("No proper value has been entered")
            continue
        elif len(response_string) > max_:
            print("Too many characters for a fruit name")
            continue
        else:
            return response_string

def get_entry_option_list(m, o, u=True):
    """Request and return a valid entry using a list of options

    :param m: string message
    :param o: list of options
    :param u: boolean
    :return: string
    """
    cont = True
    while cont is True:
        choice = input(m)
        if u:
            choice = choice.upper()
        if choice not in o:
            print("Please choose from these options: {}".format(o))
        else:
            return choice

def print_line():
    """Print dashed line of set length

    :return: None
    """
    print("-" * 60)








def encrypt_decrypt(SYMBOLS, message, key,  encrypt = True):
    mod_val = len(SYMBOLS)
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            if encrypt:
                translatedIndex = (symbolIndex + key)%mod_val
            else:
                translatedIndex = (symbolIndex - key) % mod_val
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    return translated

def brute_force_attack(SYMBOLS, message, mod_val):
    for k in range(0, mod_val):
        decrypted_message = encrypt_decrypt(SYMBOLS, message, k, False)
        output = "k = {:<3} : {} ".format(k, decrypted_message)
        print(output)

def main():
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?"
    mode = 'encrypt'
    key = 13
    mod_val = len(SYMBOLS)

    menu = {
        "A" : "Encrypt a message",
        "B" : "Decrypt a message",
        "C" : "Choose message to decrypt",
        "D" : "Brute Force Attack Encrypted Message",
        "Q" : "Quit"
    }
    while True:
        options = []
        for x, y in menu.items():
            output = "{} : {}".format(x,y)
            options.append(x)
            print(output)
        print_line()
        choice = get_entry_option_list("Please choose an option: -> ",options)
        print_line()
        if choice == "A":
            message = get_string("Please enter your message: -> ")
            key = get_integer("Please enter your key (int): -> ", 0,mod_val,mod_val)
            encrypted_message = encrypt_decrypt(SYMBOLS, message, key)
            print("Encrypted message below (has been copied to the clipboard)")
            print_line()
            pyperclip.copy(encrypted_message)
            print(encrypted_message)
            print_line()
        elif choice == "B":
            message = get_string("Please enter your encrypted message: -> ")
            key = get_integer("Please enter your encryption key (int): -> ", 0, mod_val, mod_val)
            decrypted_message = encrypt_decrypt(SYMBOLS, message, key, False)
            print("Decrypted message below (has been copied to the clipboard)")
            print_line()
            pyperclip.copy(decrypted_message)
            print(decrypted_message)
            print_line()
        elif choice == "C":
            print("Nothing here yet")
        elif choice == "D":
            message = get_string("Please enter your encrypted message: -> ")
            brute_force_attack(SYMBOLS, message,mod_val)
            print_line()
        elif choice== "Q":
            if confirmation():
                return None
        else:
            print("Something went wrong - menu error")




if __name__ == "__main__":
    main()





