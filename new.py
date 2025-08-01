import random

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True):
    """Generates a random password based on specified criteria."""

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"

    characters = ""
    if use_lowercase:
        characters += lowercase
    if use_uppercase:
        characters += uppercase
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += symbols

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password = generate_password()
    print(f"Generated password: {password}")
    print("hello, world")