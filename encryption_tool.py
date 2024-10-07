# encryption_tool.py

def caesar_encrypt(plaintext, key):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():  # Check if character is an alphabet
            shift = 65 if char.isupper() else 97
            encrypted += chr((ord(char) + key - shift) % 26 + shift)
        else:
            encrypted += char  # Non-alphabet characters remain unchanged
    return encrypted

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

def vigenere_encrypt(plaintext, key):
    encrypted = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    
    for i in range(len(plaintext_int)):
        if plaintext[i].isalpha():  # Only encrypt alphabet characters
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            encrypted += chr(value + (65 if plaintext[i].isupper() else 97))
        else:
            encrypted += plaintext[i]  # Non-alphabet characters remain unchanged
    return encrypted

def vigenere_decrypt(ciphertext, key):
    decrypted = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]

    for i in range(len(ciphertext_int)):
        if ciphertext[i].isalpha():  # Only decrypt alphabet characters
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            decrypted += chr(value + (65 if ciphertext[i].isupper() else 97))
        else:
            decrypted += ciphertext[i]  # Non-alphabet characters remain unchanged
    return decrypted

def main():
    print("Select mode:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("Caesar Cipher Selected")
        message = input("Enter the message: ")
        key = int(input("Enter the key (number): "))
        operation = input("Select operation:\n1. Encrypt\n2. Decrypt\nEnter your choice (1/2): ")
        
        if operation == "1":
            encrypted_message = caesar_encrypt(message, key)
            print("Encrypted Message:", encrypted_message)
        elif operation == "2":
            decrypted_message = caesar_decrypt(message, key)
            print("Decrypted Message:", decrypted_message)
        else:
            print("Invalid operation selected.")

    elif choice == "2":
        print("Vigenère Cipher Selected")
        message = input("Enter the message: ")
        key = input("Enter the key (string): ")
        operation = input("Select operation:\n1. Encrypt\n2. Decrypt\nEnter your choice (1/2): ")

        if operation == "1":
            encrypted_message = vigenere_encrypt(message, key)
            print("Encrypted Message:", encrypted_message)
        elif operation == "2":
            decrypted_message = vigenere_decrypt(message, key)
            print("Decrypted Message:", decrypted_message)
        else:
            print("Invalid operation selected.")

    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
