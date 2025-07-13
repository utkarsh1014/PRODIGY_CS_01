def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_message():
    message = input("Enter the message to encrypt: ")
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Shift value must be an integer. Please try again.")
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)

def decrypt_message():
    message = input("Enter the message to decrypt: ")
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Shift value must be an integer. Please try again.")
    decrypted_message = caesar_cipher(message, -shift)
    print("Decrypted message:", decrypted_message)

# Main menu
while True:
    print("\nCaesar Cipher Menu:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        encrypt_message()
    elif choice == '2':
        decrypt_message()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")