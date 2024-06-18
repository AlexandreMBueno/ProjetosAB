# Palindrome Checker
# Create a program that asks the user to input a word and checks if that word is a palindrome 
# (i.e., reads the same backward as forward).

# *** this code is supposed to work with only one word ***

# it is a much simpler version of the ValidPalindrome.py file that you can find in my NeetCode150 folder.

def palindrome(word):
    head = 0
    tail = len(word) - 1

    while head < tail:
        if word[head] != word[tail]:
            return False
        head += 1
        tail -= 1
    return True

#test with:
# test_1 = "alexandre"
# test_2 = "racecar"

word = str(input("Write a single word: "))
if palindrome(word):
    print("palindrome")
else:
    print("not palindrome")