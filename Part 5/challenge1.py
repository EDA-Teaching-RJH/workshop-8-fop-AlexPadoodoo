#Challege 1

import re

phone_number = input("Enter a Phone Number: ")

if re.search(r"^07, \d, {m,11}$", phone_number)