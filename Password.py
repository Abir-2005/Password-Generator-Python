'''A password generator is a useful tool that generates strong and random passwords for users.
This project aims to create a password generator application using Python, allowing users to
specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the password.

Generate Password: Use a combination of random characters to generate a password of the 
                specified length.

Display the Password: Print the generated password on the screen.'''


import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()"
len = int(input("Enter the length of Password : "))
password = ""

for a in range(len):
    password += random.choice(chars)

print("Your Generate Password is ",password)
