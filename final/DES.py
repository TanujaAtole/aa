from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Function to perform DES encryption
def encrypt_DES(key, plaintext):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)  # Pad plaintext to fit block size
    encrypted_text = des.encrypt(padded_text)
    return binascii.hexlify(encrypted_text)  # Return hex encoded encrypted text

# Function to perform DES decryption
def decrypt_DES(key, encrypted_text):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_text = des.decrypt(binascii.unhexlify(encrypted_text))  # Decrypt and remove hex encoding
    return unpad(decrypted_text, DES.block_size).decode()  # Unpad and return the decrypted text

# Main program
if __name__ == "__main__":
    key = input("Enter 8-byte key (e.g., '12345678'): ").encode()
    if len(key) != 8:
        print("Key must be exactly 8 bytes long!")
    else:
        message = input("Enter the plaintext message: ")

        # Encrypt the message
        encrypted = encrypt_DES(key, message)
        print("Encrypted (hex):", encrypted.decode())

        # Decrypt the message
        decrypted = decrypt_DES(key, encrypted)
        print("Decrypted:", decrypted)
