# Problem 1

principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))
balance = principal
for i in range(years):
    balance = balance * (1 + rate/100)
    if str(f"{round(balance, 3):.3f}")[-1] == "5":
        print(f"Year {i+1}: {round(balance, 2) + 0.01:.2f}")
    else:
        print(f"Year {i+1}: {round(balance, 2):.2f}")
interest_earned = balance - principal

if str(f"{round (interest_earned, 3):.3f}")[-1] == "5":
    print(f"Total interest earned: {round(interest_earned, 2) + 0.01:.2f}")
else:
    print(f"Total interest earned: {round(interest_earned, 2):.2f}")



# Problem 2

def caesar_encode(text, shift):
    shifted_text = ""
    for i in text:
        if i.isalpha():
            if i.islower():
                i = chr((ord(i) + - 97 + shift) % 26 + 97)
            else:
                i = chr((ord(i) - 65 + shift) % 26 + 65)
            shifted_text += i
    return shifted_text

print(caesar_encode("Python", 3))

