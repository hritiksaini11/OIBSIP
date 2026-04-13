import secrets
import string
import sys

def generate_password():
    print("--- 🛡️ Python Password Generator ---")

   
    try:
        length = int(input("Enter password length (e.g., 12): "))
        if length < 4:
            print("Error: Password should be at least 4 characters for better security.")
            return
    except ValueError:
        print("Error: Please enter a valid number for the length.")
        return

    
    print("\nSelect character types to include:")
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'


    chars = ""
    if use_letters:
        chars += string.ascii_letters  # abc...XYZ
    if use_numbers:
        chars += string.digits         # 0123456789
    if use_symbols:
        chars += string.punctuation    # !@#$%...


    if not chars:
        print("Error: You must select at least one character type!")
        return

    # 4. Generate the Password
    password = ''.join(secrets.choice(chars) for _ in range(length))

    print(f"\n✅ Generated Password: {password}\n")

if __name__ == "__main__":
    while True:
        generate_password()
        repeat = input("Generate another? (y/n): ").lower()
        if repeat != 'y':
            print("Goodbye!")
            break