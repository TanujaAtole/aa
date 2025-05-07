import math

def encrypt_message(message, key):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)

def decrypt_message(ciphertext, key):
    num_of_columns = math.ceil(len(ciphertext) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)

    plaintext = [''] * num_of_columns
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1

        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)

# Main Program
if __name__ == "__main__":
    message = input("Enter the message: ").replace(" ", "")  # Remove spaces for simplicity
    key = int(input("Enter the key (as a number): "))

    encrypted = encrypt_message(message, key)
    print("Encrypted Message:", encrypted)

    decrypted = decrypt_message(encrypted, key)
    print("Decrypted Message:", decrypted)
