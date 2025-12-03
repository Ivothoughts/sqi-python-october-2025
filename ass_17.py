#1 Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)

# nums = input("Enter a series of numbers: ")
# numbers = []
# total = 0
# for num in nums:
#     total += int(num)

# nums = list(nums)

# nums = "+".join(nums)

# print(f"{total} ({nums})")

    
# print(sum(numbers))

#2 Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# collect input variable from the users
# have a list of vowels
# have a variable that counts the amount of vowels
# have a variable that counts the amount of consonants
# loop through each character in the string
#7 check if character exist in vowel list
#8 if the character exist in vowel list increase the vowel counts by 1
# repeat step 8 only

# phrase = input("Enter a sentence ").strip().replace(" ", "")
# vowels = "aeiou"
# count_of_vowels = 0
# count_of_consonants = 0

# for char in phrase:
#     if not char.isalpha():
#         continue
#     if char in vowels :
#         count_of_vowels += 1
#     else:
#         count_of_consonants += 1
    
# print(f"vowels: {count_of_vowels}, consonants: {count_of_consonants}") 

# for char in phrase:
#     if char in vowels:
#         count_of_vowels += 1
#     if char not in vowels:
#         count_of_consonants += 1
    


#3 Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# collect integers from users

# table_nums = int(input("Enter a number: "))

# for i in range(1, 13):
#     result = table_nums * i
#     print(f"{table_nums} x {i} = {result}")

# i = 1

# while i <= 12:
    # product = table_nums * i
    # # product = product * table_nums
    # print(f"{table_nums} x {i} = {product}")
    # i += 1

#4 Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# collect the word 
# count from the back 

# word = input("Enter a word: ")

# reversed_word = []

# for char in word:
#     reversed_word.insert(0, char)
# reversed_word = "".join(reversed_word)
# print(reversed_word)

#5 Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# list_of_nums = input("Enter a comma seperated list of numbers: ").split("," )
# new_list = []

# for char in list_of_nums:
#     num = int(char)

#     if num not in new_list:
#         new_list.append(num)

# print(new_list)


#  6.	Write a program that takes an integer input n from the user and prints the first 
# 	n numbers in the Fibonacci sequence. Example:
# 	Input: 10
# 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# collect the input "n"
    # print("char:", type(char))
# have a variable that stores the first start of the fibonacci sequence "0"
# have a variable that stores the second start of the fibonacci sequence "1"
# have a variable that stores the sum of the last two numbers

# n = int(input("Enter a number: "))

# result = [0, 1, ]

# for i in range(1, n-1):
    
#     result.append(result[i] + result[i - 1 ])
#     print(result)
# print(result)


# a, b = 0, 1

# for i in range(n):
#     print(a, end=", ")
#     a,b = b, a + b


#  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20

# list_of_nums = input("Enter a comma seperated list of numbers: ").split("," )

# ediited = int(list_of_nums[0])

# for char in list_of_nums:
#     num = int(char)
#     if num > ediited:
#         ediited = num
# print(ediited)


#  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

# nums = int(input("Enter a series of numbers: "))
# even_numbers = []
# total = 0
# for i in range(1, nums + 1):
#     if i % 2 == 0:
#         total += i
#         even_numbers.append(str(i))

# even_numbers = ' + '.join(even_numbers)
# print(f"{total} ({even_numbers})")

#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1

# words = input("Enter a word of your choice: ")
# char_frequncy = {}

# for char in words:
#     if char in char_frequncy:
#         char_frequncy[char] += 1
#     else:
#         char_frequncy[char] = 1

# for char, count in char_frequncy.items():
#     print(f"{char}: {count}")
    
# print(char_frequncy, end= "")
    
#  10.	Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)

# n = int(input("Enter a number of your choice: "))
# total = 0
# squares = []

# for i in range(1, n + 1):
#     total += i ** 2
#     squares.append(f"{i}^2")
    
# squares = " + ".join(squares)

# print(f"{total} ({squares})")

#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"

# phrases = input("Enter a sentence: ").title()
# new_phrases = phrases.split()
# acronym = ""

# for word in new_phrases:
#     # print(new_phrases)
#     acronym += word[0]

# print(acronym)

#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4

# words = input("Enter a sentence: ").split()
# count = 0
# for word in words:
#     count += 1

# print(count)

#  13. 	Collect a string from the user and only print put the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence

# phrase = input("Enter a sentence: ").lower()
# phrase = phrase.split()
# for word in phrase:
#     if word.startswith("s"):
#         print(word)

#  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.

#  16.	Go through the string below and if the length of a word is even, print that word.
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

# words = input("Enter a sentence: ")
# words = words.split()

# for word in words:
#     if len(word) % 2 == 0:
#         print(word)

#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} FizzBuzz")
#     elif i % 3 == 0:
#         print(f"{i} Fizz")
#     elif i % 5 == 0:
#         print(f"{i} Buzz")
    # else:
        # print(i)

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


