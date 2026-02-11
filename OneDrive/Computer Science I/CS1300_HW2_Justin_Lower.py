# Problem 1
first_name = input("Input first name:")
last_name = input("Input last name:")
age = 2026 - int(input("Input birth year:"))
favorite_hobby = input("Input favorite hobby:")
print("=" * 30)
print("Name:", end= "\t")
print(f"{first_name.capitalize()} {last_name.capitalize()}")
print(f"Age:\t{age}")
print(f"Hobby:\t{favorite_hobby}")
print("=" * 30)

#Problem 2

sentence = input("Enter a sentence:")
starts_with_capital = sentence[0].isupper()
if (sentence.endswith(".")):
    ends_with_punctuation = True
elif (sentence.endswith("?")):
    ends_with_punctuation = True
elif (sentence.endswith("!")):
    ends_with_punctuation = True
else:
    ends_with_punctuation = False
    
sentence_without_spaces = sentence.replace(" ", "")
lower_sentence = sentence.lower()
a_count = lower_sentence.count("a")
e_count = lower_sentence.count("e")
i_count = lower_sentence.count("i")
o_count = lower_sentence.count("o")
u_count = lower_sentence.count("u")
vowel_count = a_count + e_count + i_count + o_count + u_count
print(f"Number of characters (with spaces):\t {len(sentence)} ")
print(f"Number of characters (no spaces):\t {len(sentence_without_spaces)}")
print(f"Number of words:\t {sentence.count(" ") + 1}")
print(f"Number of vowels:\t{vowel_count}")
print(f"Uppercase:\t {sentence.upper()}")
print(f"Lowercase:\t {lower_sentence}")
print(f"Reverse:\t {sentence[::-1]}")
if starts_with_capital == True:
    print("Starts with capital:\t Yes")
else:
    print("Starts with capital:\t No")

if ends_with_punctuation == True:
    print("Ends with punctuation:\t Yes")
else:
    print("Ends with punctuation:\t No")
    
    

