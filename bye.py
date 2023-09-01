import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_with_website(website, length=12, include_digits=True, include_special_chars=True):
    password = generate_password(length, include_digits, include_special_chars)
    return f"Password for {website}: {password}"

website_name = input("Enter the name of the website: ")
password = generate_password_with_website(website_name)
print(password)
