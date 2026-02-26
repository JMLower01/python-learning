#Problem 1
a = input("Input first integer:")
b = input("Input second integer:")
c = input("Input third integer:")

if a < b < c:
    print("a < b < c\tTrue")
else:
    print("a < b < c\tFalse")
if not (a > b or b > c):
    print("not a > b or b > c\tTrue")
else:
    print("not a > b or b > c\tFalse")
if a <= b and b <= c:
    print("a <= b and b <= c\tTrue")
else:
    print("a <= b and b <= c\tFalse")
if not(a > b or b > c) == (a <= b and b <= c):
    print("De Morgan's Law confirmed. Expressions 2 and 3 match.")
else:
    print("De Morgan's Law disproven. Expressions 2 and 3 don't match.")
    

#Problem 2
temperature = int(input("What is the temperature?"))
is_raining = input("Is it raining?")

if temperature > 100:
    print("EXTEREME HEAT WARNING: Stay indoors!")
elif temperature > 85:
    if is_raining.lower() == "yes":
        print("Warm rain - watch for flash floods.")
    else:
        print("Hot and dry - stay hydrated.")
elif temperature > 60:
    if is_raining.lower() == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather - Enjoy your day!")
elif temperature >= 32:
    print("It's cold - bundle up!")
else: 
    print("FREEZE WARNING: Roads may be icy!")

#Problem 3
first_score = int(input("Input first score:"))
second_score = int(input("Input second score:"))
third_score = int(input("Input third score:"))
average = (first_score + second_score + third_score) / 3
name = input("Input student's name:")
print("=" * 40)
print("\t STUDENT GRADE REPORT")
print("=" * 40)
print(f"Student: {name}")
print(f"Exam 1: {first_score}")
print(f"Exam 2: {second_score}")
print(f"Exam 3: {third_score}")
print("-" * 40)
print(f"Average: {average:.2f}")
if average >= 90:
    print("Grade:\tA")
    print("Status:\tDean's List")
elif average >= 70:
    if average >= 87:
        print("Grade\tA-")
    elif average >= 83:
        print("Grade:\tB+")
    elif average >= 80:
        print("Grade:\tB")
    elif average >= 77:
        print("Grade:\tB-")
    elif average >= 73:
        print("Grade:\tC+")
    else:
        print("Grade\tC")
    print("Status:\tGood Standing")
elif average >= 60:
    if average >= 67:
        print("Grade\tC-")
    elif average >=63:
        print("Grade:\tD+")
    else:
        print("Grade:\tD")
    print("Status:\tAcademic Probation")
else:
    print("Grade:\tF")
    print("Status:\tAcademic Suspension Warning")
print("=" * 40)