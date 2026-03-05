#Problem 1
temperature = int(input("Enter temperature:"))
scale = input("Enter scale (C/F)")
if scale.upper() == "C":
    print(f"{temperature:.1f} C = {temperature *(9/5) + 32:.1f} F")
elif scale.upper() == "F":
    print(f"{temperature:.1f} F = {(temperature - 32) * 5/9:.1f} C")
else:
    print("Invalid scale")

#Problem 4

gpa = float(input("Enter GPA:"))
credit_hours = int(input("Enter credit hours:"))
prerequisite = input("Prerequisite completed?")

print(f"GPA: {gpa}")
print(f"Credits: {credit_hours}")
print(f"Prerequisite: {prerequisite}")


if gpa >= 3.5 and credit_hours >= 60 and prerequisite.lower() == "yes":
    print("Status: Approved: You meet all requirements.")
elif gpa >= 3.5 and credit_hours >= 60:
    print("Status: Conditionally Approved: Complete the prerequisite first.")
elif gpa >= 3.0 and credit_hours >= 45:
    print("Status: Waitlisted: You may be admitted if space is available.")
elif gpa >= 2.0:
    print("Status: Not eligible yet: Raise your GPA or earn more credits.")
else:
    print("Status: Denied: GPA is below minimum threshold.")