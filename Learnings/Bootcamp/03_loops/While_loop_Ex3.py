# Keep asking user for password until correct.
correct_password = "Enter@1212"
password = ""

while password != correct_password:
    password = input("Please enter the password: ")
print("Password is accepted!")