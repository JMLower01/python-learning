#Problem 1
age = int(input("Enter age: "))
matinee = input("Is the showing a matinee? (yes/no) ")
is_matinee = True if matinee.lower()== "yes" else False
if age < 0:
    print("Error: age must be positive")
elif age >= 65:
    print("Age group: Senior")
    if is_matinee:
        print("Ticket price: $6.00")
    else:
        print("Ticket price: $7.00")
elif age >= 18:
    print("Age group: Adult")
    if is_matinee:
        print("Ticket price: $8.00")
    else:
        print("Ticket price: $13.00")
elif age >= 13:
    print("Age group: Teen")
    if is_matinee:
        print("Ticket price: $7.00")
    else:
        print("Ticket price: $10.00")
else:
    print("Age group: Child")
    if is_matinee:
        print("Ticket price: $6.00")
    else: 
        print("Ticket price: $8.00")

#Problem 2
errors = []
student_id = input("Enter student id:")
name = input("Enter name:")
age = input("Enter age:")
major = input("Enter major:")
if len(student_id) != 8:
    errors.append("Student ID must be exactly 8 characters")
if not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")
if not student_id[1:].isdigit():
    errors.append("Last 7 characters of student ID must be numbers")
if not name.strip():
    errors.append("Name is empty")
if len(name) < 2:
    errors.append("Name must be at least 2 characters")
try:
    age_int = int(age)
    if age_int < 16 or age_int > 99:
        errors.append("Age must be between 16 and 99")
except ValueError:
  
 errors.append("Age must be an integer")

if not major.lower() in ["cs", "it", "ce", "ds"]:
    errors.append("Major must be one of: CS, IT, CE, DS")
if errors:
    print("Profile has errors:")
    for error in errors:
        print(error)
else:
    print("Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name:\t {name}")
    print(f"Age:\t {age}")
    print(f"Major:\t {major}")

    

#Problem 3
print("-" * 30)
print("   CAMPUS CAFE ORDER SYSTEM")
print("-" * 30)
print("1. Coffee\t - $3.50")
print("2. Sandwich\t - $6.00")
print("3. Salad\t - $5.50")
print("4. Combo\t - $8.00")
print("5. Exit")
menu_choice = input("Enter your choice(1-5)")
if menu_choice == "1":
    size = input("Choose a size (S/M/L)")
    if size.lower() == "s":
        price = 3.50
        item = "Small Coffee"
    elif size.lower() == "m":
        price = 4.50
        item = "Medium Coffee"
    elif size.lower() == "l":
        price = 5.50
        item = "Large Coffee"
    else:
        price = 3.50
        print("Invalid size - defaulted to Small")
        item = "Small Coffee"
elif menu_choice == "2":
    cheese = input("Add cheese?(yes/no)")
    if cheese.lower() == "yes":
        price = 6.75
        item = "Sandwich with Cheese"
    else:
        price = 6.00
        item = "Sandwich"
elif menu_choice == "3":
    dressing = input("Choose a dressing (Ranch, Italian, Vinaigrette, None):")
    price = 5.50
    if dressing.lower() in ["ranch", "italian", "vinaigrette",]:
        item = f"Salad + {dressing.upper()}"
    elif dressing.lower() == "none":
        item = "Salad"
    else:
        item = "Salad"
        print("Invalid dressing - defaulted to none")
elif menu_choice == "4":
    size = input("Choose a size: (S/M/L)")
    cheese = input("Add cheese? (yes/no)")
    if size.lower == "s":
        if cheese.lower() == "yes":
            price = 8.75
            item = "Combo (Small, Cheese)"
        else:
            price = 8.00
            item = "Combo (Small, No Cheese)"
    elif size.lower() == "m":
        if cheese.lower() == "yes":
            price = 9.75
            item = "Combo (Medium, Cheese)"
        else:
            price = 9.00
            item = "Combo (Medium, No Cheese)"
    elif size.lower() == "l":
        if cheese.lower() == "yes":
            price = 10.75
            item = "Combo (Large, Cheese)"
        else:
            price = 10.00
            item = "Combo (Large, No Cheese)"
    else:
        print("Invalid size - defaulted to Small")
        if cheese.lower() == "yes":
            price = 8.75
            item = "Combo (Small, Cheese)"
        else:
            price = 8.00
            item = "Combo (Small, No Cheese)"
if menu_choice in ["1", "2", "3", "4"]:
    name = input("Enter name:")
    subtotal = 0
    try:
        quantity = int(input("How many?"))
        if quantity > 0:
            subtotal = price * quantity
    except ValueError:
        print("Invalid quantity")
    if subtotal and name.strip():
        tax = subtotal * 0.07
        total = subtotal + tax
        print("-" * 30)
        print("\tORDER RECEIPT")
        print("-" * 30)
        print(f"Customer: {name}")
        print(f"Item: {item}")
        print(f"Quantity: {quantity}")
        print(f"Unit Price: ${price:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax: (7%) ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("-" * 30)
        
        
        
        
    
    
        


        
        
        
        


    
