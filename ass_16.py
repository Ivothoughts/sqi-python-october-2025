#1 Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)

# numbers = int(input("Enter a series of number: "))


#2 Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

#3 Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

#4 Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

#5 Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# 16.	Go through the string below and if the length of a word is even, print that word.
# 	st = ‘Print every word in this sentence that has an even number of letters’
# 	Output: 
# 	word
# 	in
# 	this
# 	sentence
# 	that
# 	an
# 	even
# 	number
# 	of

st = "Print every word in this sentence that has an even number of letters"

#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

# for i in range(1,101):
#     if i % 3 == 0:
#         print(f"{i} Fizz")
#     if i % 5 == 0:
#         print(f"{i} Buzz")
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} FizzBuzz")

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} Fizz")
    elif i % 5 == 0:
        print(f"{i} Buzz")
        

#  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# # print(list(enumerate(zip(names, grades))))

# for  (names, grades) in zip(names, grades):
#     print(f"{names} got grades {grades}")


#19 Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

# items = ['shoe', 'stick', 'toy', 'fruit']

# for i in range(len(items)):
#     # print(i)
#     if i % 2 == 0:
#         print(f"{i}: {items[i]}")
#     if i == items[2]:
        # break

# 20.	Given two lists of numbers of the same length, print the indices and values
#  	of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]

# print(list(enumerate(zip(list1, list2))))

# for ide, (list1, list2) in enumerate(zip(list1, list2)):
#     if list1 == list2:
#         continue
#     print(f"'Index{ide}: {list1} != {list2}'")




