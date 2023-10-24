import random
import string

def create_password(length):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Input the desired password length
password_length = int(input("Enter the password length you want: "))

# Generate and print the password
password = create_password(password_length)
print("Your password is:", password)
print("Thank you!")
