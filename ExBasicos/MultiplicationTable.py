# Multiplication Table
# Write a program that asks the user to input a number 
# Displays the multiplication table of that number from 1 to 10.

number = int(input("Type a number: "))
i = 1

while i <= 10:
    calc = number * i
    print(f"{number} * {i} = {calc}")
    i += 1
