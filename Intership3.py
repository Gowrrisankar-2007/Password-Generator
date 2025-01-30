import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    try:
        length = int(input("Enter password length (or 0 to exit): "))
        if length == 0:
            print("Goodbye!")
            break
        elif length < 4:
            print("Password should be at least 4 characters long.")
        else:
            print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")
