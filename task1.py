letters = 'abcdefghijklmnopqrstuvwxyz'
size = len(letters)

def caesar_cipher(text, key, mode):
    result = ''
    for letter in text:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter) # returns -1 if not found
            if index == -1:
                result += letter
            else:
                if mode == 'e':
                    new = (index + key) % size
                elif mode == 'd':
                    new = (index - key) % size
                result += letters[new]
        else:
            result += ' '

    return result

print("---------------------Caesar Cipher Program---------------------")
print()
print("Do you want to Encrypt or Decrypt?")
user = input("(E)ncrypt/ (D)ecrypt: ").lower()
print()
if user == "e":
    print("Encryption ")
    print()
    key = int(input("Enter your Encryption key (1-26): "))
    text = input("Enter Your Text: ")
    encrypted = caesar_cipher(text, key, 'e')
    print("Encrypted Text:", encrypted)

elif user == "d":
    print("Decryption ")
    print()
    key = int(input("Enter your Decryption key (1-26): "))
    text = input("Enter Your Text: ")
    decrypted = caesar_cipher(text, key,'d')
    print("Decrypted Text:", decrypted)

else:
    print("Invalid. Please enter 'E' to Encrypt or 'D' to Decrypt.")
