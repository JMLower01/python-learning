# What will each line print?
message = "Hello, Python!"
print(message)
print(type(message))

number = 42
print(type(number))


# These lines have errors. Fix them to be valid AND follow PEP 8:
# 1st_name = "Taylor"
# user-age = 21
# class = "Computer Science"
# My Score = 100

first_name = "Taylor"
user_age = 21
class_name = "Computer Science"
my_score = 100

print (first_name, user_age, class_name, my_score)



# Run this code and explain what you observe:
a = 256
b = 256
print("a =", a, "id(a) =", id(a))
print("b =", b, "id(b) =", id(b))
print("Same object?", id(a) == id(b))

print()

c = 257
d = 257
print("c =", c, "id(c) =", id(c))
print("d =", d, "id(d) =", id(d))
print("Same object?", id(c) == id(d))

# BEFORE: Messy code
x="johnsmith@email.com"
Y=2026-2004
z=Y>=18
a="Welcome" if z else "Sorry, too young"
#print(a)

email = "johnsmith@email.com"
age = 2026-2004
is_old_enough = age >= 18
result_message = "Welcome" if is_old_enough else "Sorry, too young"

print (result_message)

print("second try to make sure git repo work")
