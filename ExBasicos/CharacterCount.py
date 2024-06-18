# Character Count
# Write a program that asks the user to input a sentence
# And counts the occurrence of each character in the sentence.

user_sentence = str(input("Write a short sentence: "))

char_count = {}

for char in user_sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"'{char}': {count}")