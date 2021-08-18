

def main():
    my_message ="Common sense is not so common."
    myKey= 8
    encrypted_message = encrypt_message(my_message,myKey)
    print(encrypted_message + '|')

def encrypt_message(message, key):
    ciphertext = ['']*key
    for c in range(key):
        current_index = c
        while current_index < len(message):
            ciphertext[c] += message[current_index]
            #print(current_index)
            current_index += key
    return ''.join(ciphertext)


if __name__ == "__main__":
    main()