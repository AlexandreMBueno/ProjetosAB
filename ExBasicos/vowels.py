# Vowel Counter
# Write a program that asks the user to input a word and counts how many vowels (a, e, i, o, u) are in that word.

word = str(input("Write a word: "))
print(word)
vowels_list = {"a", "e", "i", "o", "u"}
vowels_count = 0
for i in word:
    if i in vowels_list:
        vowels_count += 1
print(vowels_count)