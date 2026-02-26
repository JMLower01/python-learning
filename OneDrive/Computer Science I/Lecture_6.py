
age = int(input("Input age:"))
if 0 <= age <= 120:
    print("Valid Age")
else:
    print("Invalid Age")
    
phone_number = input("Enter phone number:")

if not phone_number.isdigit():
    print("Phone number should be only numbers.")
elif not len(phone_number) == 10:
    print("Phone number should be 10 digits")
else:
    print("Phone number accepted")
    
password = input("Create a password:")

if password.lower == ("password"):
    print("Password cannot be the word password")
elif len(password) < 8:
    print("Password should be at least 8 characters long.")
elif not any(c.isdigit() for c in password):
    print("Password should contain a digit.")
elif password.lower == password:
    print("Password should contain an uppercase letter.")
else:
    print("Password accepted")
    
email = input("Enter email:")


if not email:
    print("You did not enter an email.")
elif email.count("@") != 1:
    print("Email should contain exactly one @.")
elif email[0] == "@":
    print("Email should contain characters before the @.")
elif not email.find("@") < email.rfind("."):
    print("Email should contain a . after the @.")
else:
    print("Valid email.")
    




    
    
    