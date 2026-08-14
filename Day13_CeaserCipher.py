#CEASER CIPHER

# CAESAR CIPHER

def encrypt(text, shift):
    result = ""

    for letter in text:
        if letter.isalpha():
            start = ord("A") if letter.isupper() else ord("a")

            new_number = (ord(letter) - start + shift) % 26 + start
            result += chr(new_number)
        else:
            result += letter

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


choice = input("Do you want to encrypt or decrypt? (E/D): ").strip().lower()

text = input("Enter your message: ")
shift = int(input("Enter shift amount: "))

if choice == "e":
    print("Encrypted:", encrypt(text, shift))

elif choice == "d":
    print("Decrypted:", decrypt(text, shift))

else:
    print("Invalid option")
