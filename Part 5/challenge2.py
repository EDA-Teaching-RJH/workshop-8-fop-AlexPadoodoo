import re

student_id = input("Enter your student ID: ")

# string must begin with exactly 4 letters followed by 4 numbers
if re.search(r"^\w{4}\d{4}$", student_id):
    print("Valid student ID!")
else:    
    print("Invalid student ID")