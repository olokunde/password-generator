import random
import string

print("Welcome to Password Generator")

length = int(input("How long should the password be? "))

include_numbers = input("Include numbers? yes/no: ").lower()
include_symbols = input("Include symbols? yes/no: ").lower()

characters = string.ascii_letters

if include_numbers == "yes":
    characters += string.digits

if include_symbols == "yes":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is:", password)