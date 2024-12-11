def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Choose an option: (E)ncrypt, (D)ecrypt, or (Q)uit: ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice in ['E', 'D']:
            text = input("Enter the text: ").strip()
            try:
                shift = int(input("Enter the shift value (integer): "))
                if choice == 'D':
                    shift = -shift
                result = caesar_cipher(text, shift)
                print(f"Result: {result}")
            except ValueError:
                print("Shift value must be an integer. Please try again.")
        else:
            print("Invalid option. Please choose E, D, or Q.")

if __name__ == "__main__":
    main()
