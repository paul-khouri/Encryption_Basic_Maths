
import math

def main():
    my_message ="Cenoonommstmme oo snnio. s s c"
    myKey= 8
    decrypted_message = decrypt_message(my_message,myKey)
    print(decrypted_message)

def decrypt_message(message, key):
    num_columns = int( math.ceil( len(message)/float(key) ) )
    num_rows = key
    num_shaded_boxes = (num_columns * num_rows)-len(message)

    plaintext = ['']*num_columns
    column = 0
    row = 0
    for s in message:
        plaintext[column] += s
        column += 1
        if column == num_columns:
            column = 0
            row += 1
        if column == num_columns - 1 and row >= num_rows - num_shaded_boxes:
            column = 0
    return ''.join(plaintext)

if __name__ == "__main__":
    main()



