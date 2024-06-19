def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher")
    choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
    if choice not in ('e', 'd'):
        print("Invalid choice!")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        result = caesar_cipher_encrypt(text, shift)
        print("Encrypted message:", result)
    elif choice == 'd':
        result = caesar_cipher_decrypt(text, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
