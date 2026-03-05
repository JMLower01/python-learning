#Problem 1
distance = float(input("Enter distance:"))
unit = input("Enter unit(km/mi):")
if unit.lower() == "km":
    print(f"{distance:.2f} km = {distance * 0.621371:.2f} mi")
elif unit.lower() == "mi":
    print(f"{distance:.2f} mi = {distance * 1.60934:.2f} km")
else:
    print("Invalid unit.")
    
#Problem 2
sentence = input("Enter a sentence:")
sentence = sentence.strip(" ")
space_count = sentence.count(" ")
lower_sentence = sentence.lower()
vowel_count = lower_sentence.count("a") + lower_sentence.count("e") + lower_sentence.count("i") + lower_sentence.count("o") + lower_sentence.count("u")
total_length = 0
print(f"Total characters: {len(sentence)}")
print(f"Total words: {space_count + 1}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {len(sentence) - vowel_count - space_count}")
word_list = sentence.split()
for i in range(len(word_list)):
    word = word_list[i]
    total_length = total_length + len(word)
    if i == 0:
        longest_word = word_list[i]
    else:
        if len(word_list[i]) > len(longest_word):
            longest_word = word_list[i]
average_length = total_length / len(word_list)
print(f"Average word length:{average_length:.2f}")
print(f"Longest word: {longest_word}")


    
