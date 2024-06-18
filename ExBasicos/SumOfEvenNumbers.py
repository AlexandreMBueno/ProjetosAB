# Sum of Even Numbers
# Write a program that receives a list of numbers and calculates the sum of all even numbers in the list.

list = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
temp = 0

for i in list:
    if i % 2 == 0:
        temp = i + temp
print(temp)

