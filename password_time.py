'''
Ellie Meredith
IS 303 - A01

Password Time Calculator
This program estimates how long it would take to crack a password
using a brute-force attack.

Inputs:
- Username (string)
- Password length (int)
- Character set size (int)

Processes:
- Convert password length and character set size to integers
- Calculate total combinations: character set size raised to the power of password length
- Calculate seconds to crack: combinations / 1000000000

Outputs:
- Print the username, password details, and estimated crack time in seconds
'''

username = input("What is your username? ")
password_length = int(input("How long is your password? "))
charset_size = int(input("How many possible characters are in your character set? (e.g. 26 for lowercase only) "))

combinations = charset_size ** password_length
seconds_to_crack = combinations / 1000000000

print("---")
print(f"{username} | password length: {password_length} | character set size: {charset_size}")
print(f"Total combinations: {combinations}")
print(f"Estimated seconds to crack: {seconds_to_crack}")