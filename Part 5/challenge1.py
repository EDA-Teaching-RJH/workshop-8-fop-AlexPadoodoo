#Challege 1

import re

phone_number = input("Enter a Phone Number: ")
#phone number should start with 07 and have 11 numbers
if re.search(r"^07\d{9}$", phone_number):
    print("Valid phone number!")
else:
    print("Invalid phone number")