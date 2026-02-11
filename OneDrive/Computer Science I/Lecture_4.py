text = "Programming"
print(text[0])
print(text[-1])
print(text[4])
print(len(text))



text = "hello world, welcome to PYTHON"
# Convert to all uppercase
upper_text = text.upper()
# Convert to all lowercase
lower_text = text.lower()
# Convert to title case
title_text = text.title()

print(upper_text) # HELLO WORLD, WELCOME TO PYTHON
print(lower_text) # hello world, welcome to python
print(title_text) # Hello World, Welcome To Python

text = "Hello, this is a sample sentence!"

print(len(text))
print(text.count("a"))
print(text.startswith("Hello"))
print(text.isalnum())

name = " JOHN DOE "
email = " John.Doe@Email.COM "
phone = " (555) 123-4567 "

clean_name = name.strip()
clean_name = clean_name.title()
clean_email = email.strip()
clean_email = clean_email.lower()
clean_phone = phone.strip()
clean_phone = clean_phone.replace("(", "")
clean_phone = clean_phone.replace(")", "")
clean_phone = clean_phone.replace("-", "")




print(clean_name)
print(clean_email)
print(clean_phone)