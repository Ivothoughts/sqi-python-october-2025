# item = "Television"

# i = 0

# while i < len(item):
#     print(item[i])
#     i += 1


# for char in item:
#     print(char)


# gadgets = ["Phone", "TV", "Radio", "Fan", "Freezer", "Boiling Ring", "Electric Kettle"]

# for gadget in gadgets:
#     print(gadget)

# for gadget in gadgets:
    # print(gadgets)
    # print("shoe")


# gadgets = ["Phone", "TV", "Radio", "Fan", "Freezer", "Boiling Ring", "Electric Kettle"]

# for gadget in gadgets:
#     # print(gadgets)
#     print("Hey")
#     print(gadget)

# native_soups = ("Okra", "Afang", "Edikaikong", "Egusi", "Abula", "Owu", "Banga", "Oha")

# for soup in native_soups:
#     for char in soup:
#         print(char)
#     print("\n")


# native_soups = {"Okra", "Afang", "Edikaikong", "Egusi", "Abula", "Owu", "Banga", "Oha"}

# for soup in native_soups:
#     print(soup)


# i = 0

# while i < len(native_soups):
#     print(native_soups[i])
#     i += 1


# for num in [1, 2, 3]:
#     print(num)


# for num in range(7):
# for num in list(range(7)):
    # print(num)


# print(list(range(7)))

# for i in range(3, 10):
#     print(i)


# for i in range(3, 10, 2):
#     print(i)


# for i in range(3):
#     print(i)



# states_and_capitals = {"Ondo": "Akure", "Ogun": "Abeokuta", "Lagos": "Ikeja", "Enugu": "Enugu", "Oyo": "Ibadan", "Anambra": "Awka"}

# for state in states_and_capitals.keys():
# for state in states_and_capitals:
#     print(state)
# for capital in states_and_capitals.values():
#     print(capital)


# print(states_and_capitals.items())

# for state, capital in states_and_capitals.items():
#     # print(item)
#     print(f"The capital of {state} is {capital}")

# native_soups = {"Okra", "Afang", "Edikaikong", "Egusi", "Abula", "Owu", "Banga", "Oha"}


# dog_breeds = ["Rotweiller", "Chihuahua", "Poodle", "Doberman", "Pitbull", "Lhasa Apso", "Boer boel", "Ekuke"]

# for dog_breed in dog_breeds:
#     if dog_breed == "Doberman":
#         continue
#     print(dog_breed)

# for dog_breed in dog_breeds:
#     print(dog_breed)
#     if dog_breed == "Pitbull":
#         break

# print()
# print()
# print()

# for dog_breed in dog_breeds:
#     if dog_breed == "Lhasa Apso":
#         break
#     print(dog_breed)


# dog_breeds = ["Rotweiller", "Chihuahua", "Poodle", "Doberman", "Pitbull", "Lhasa Apso", "Boer boel", "Ekuke"]


# for i in range(len(dog_breeds)):
#     print(f"The breed at index {i} is {dog_breeds[i]}")

# 1. Rotweiller
# 2. Chihuahua
# 3. Poodle
# 4. Doberman
# 5. Pitbull
# 6. Lhasa Apso
# 7. Boer boel
# 8. Ekuke

# dog_breeds = ["Rotweiller", "Chihuahua", "Poodle", "Doberman", "Pitbull", "Lhasa Apso", "Boer boel", "Ekuke"]


# print(list(enumerate(dog_breeds, start=100)))

# for i, breed in enumerate(dog_breeds, start=1):
#     # print(f"The breed at index {i} is {breed}")
#     print(f"{i}. {breed}")




# dog_breeds = ["Rotweiller", "Chihuahua", "Poodle", "Doberman", "Pitbull", "Lhasa Apso", "Boer boel", "Ekuke"]


# for dog_breed in dog_breeds:
#     print(dog_breed)
# else:
#     print("Loop has ended")


# dog_breeds = ["Rotweiller", "Chihuahua", "Poodle", "Doberman", "Pitbull", "Lhasa Apso", "Boer boel", "Ekuke"]


# for dog_breed in dog_breeds:
#     # print(dog_breed)
#     pass


# print(dog_breed)


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]


# for adjective in adjectives:
#     for animal in animals:
#         print(f"{adjective} {animal}")




# native_soups = ("Okra", "Afang", "Edikaikong", "Egusi", "Abula", "Owu", "Banga", "Oha")

# for soup in native_soups:
#     for char in soup:
#         print(char)
#     print("\n")


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# print(list(range(len(adjectives))))

# for i in range(len(adjectives)):
#     print(i)  # 2
#     print(f"{adjectives[i]} {animals[i]}")  # playful dolphin



# adjectives = ["fierce", "majestic", "playful", "happy"]
# animals = ("lion", "eagle", "dolphin")

# print(list(enumerate(zip(adjectives, animals))))

# for idx, (adjective, animal) in enumerate(zip(adjectives, animals), start=1):
#     print(f"{idx}. {adjective} {animal}")


# adjectives = ["fierce", "majestic", 10, "playful", "happy"]
# animals = ("lion", 13, "eagle", "dolphin", False)

# print(list(enumerate(zip(adjectives, animals))))

# for idx, (adjective, animal) in enumerate(zip(adjectives, animals), start=1):
#     print(f"{idx}. {adjective} {animal}")


# 11. Collect a phrase from the user and use a loop to generate an acronym by taking the first
# letter of each word. Print the acronym. Example:
# Input: "Portable Network Graphics"
# Output: "PNG"

# 1. Collect the string from the user and turn to title case
# 2. Separate the words by splitting on the space
# 3. Create a space to store the first letters
# 4. Go through every word in the list
# 5. Add the first char of each word to the storage
# 6. Join back to a string


# words = input("Enter a phrase: ").title().split()

# acronym = []

# for word in words:
#     acronym.append(word[0])

# acronym = "".join(acronym)
# print(acronym)


# -------------------------ASSIGNMENT CORRECTION------------------------------------

# 1. Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)


# 2. Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# 3. Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60


# 4. Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]


# numbers = input("Enter numbers separated by commas: ").split(",")

# unique_nums = []

# for num in numbers:
#     number = int(num)
#     if number not in unique_nums:
#         unique_nums.append(number)

# print(unique_nums)

# 6. Write a program that takes an integer input n from the user and prints the first 
# n numbers in the Fibonacci sequence. Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# 0 + 1 -> 1
# 1 + 1 -> 2
# 1 + 2 -> 3
# 2 + 3 -> 5
# 3 + 5 -> 8

# n = int(input("Enter the value of n: "))  # 5

# fibonacci = [0, 1]


# # for i in range(1, 4): -> 1, 2, 3
# for i in range(1, n - 1):
#     current_num = fibonacci[i]  # 2
#     previous_num = fibonacci[i - 1]  # 1
#     next_num = previous_num + current_num  # 3
#     fibonacci.append(next_num)  # [0, 1, 1, 2, 3]

# print(fibonacci)


# 7. Collect a list of numbers from the user (entered as comma-separated values) and use a 
# loop to find and print the largest number in the list. Don't use the built-in max 
# function or anything similar.
# Input: "10, 20, 5, 15"
# Output: 20

# numbers = input("Enter comma separated numbers: ").split(',')

# highest = int(numbers[0])

# for num in numbers:
#     num = int(num)
#     if num > highest:
#         highest = num

# print(f"{highest} is the highest")

# 8. Write a program that takes an integer n from the user and calculates the sum of all 
# even numbers from 1 to n. Print the sum.
# Input: 10
# Output: 30 (2 + 4 + 6 + 8 + 10)

# 9. Collect a string from the user and use a loop to count the frequency of each character 
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1


# 10. Write a program that takes an integer n from the user and calculates the sum of 
# squares of all numbers from 1 to n. Print the sum. Example:
# Input: 3
# Output: 14 (1^2 + 2^2 + 3^2)


# n = int(input("Enter the value of n: "))
# sum_of_squares = 0

# for i in range(1, n+1):
#     # sum_of_squares += i * i
#     sum_of_squares += i ** 2
    

# print(sum_of_squares)

# 11. Collect a phrase from the user and use a loop to generate an acronym by taking the first
# letter of each word. Print the acronym. Example:
# Input: "Portable Network Graphics"
# Output: "PNG"


# 12. Collect a string from the user and use a loop to count the number of words in the string. 
# Print the count. Example:
# Input: "Hello world from Python"
# Output: 4


# words = input("Enter some text: ").strip().split()

# no_of_words = 0

# for word in words:
#     no_of_words += 1

# print(f"There are {no_of_words} words in the text")


# 13. Collect a string from the user and only print out the words that start with the letter 
# ‘S'. Example:
# Input: “Print only the words that start with s in this Sentence”
# Output: 
# start
# s
# Sentence


# words = input("Enter some text: ").split()

# for word in words:
#     if word.lower().startswith("s"):
#         print(word)


# 14. Print all the even numbers from 1 to 20 using the range function and a loop.


# for i in range(2, 21, 2):
#     print(i)


# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# 15. Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# by 3.

# 16. Go through the string below and if the length of a word is even, print that word.
# st = ‘Print every word in this sentence that has an even number of letters'
# Output: 
# word
# in
# this
# sentence
# that
# an
# even
# number
# of


# st = 'Print every word in this sentence that has an even number of letters'

# words = st.split()

# for word in words:
#     if len(word) % 2 == 0:
#         print(word)


# 17. Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# “Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# are multiples of both three and five, print “FizzBuzz”.

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



# 18. You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# *args

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# shorter_list = min([names, grades])

# no_of_items = len(shorter_list)

# for i in range(no_of_items):
#     name = names[i]
#     grade = grades[i]

#     print(f"{name} got grade {grade}")

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# print(list(zip(names, grades)))

# for name, grade in zip(names, grades):
#     print(f"{name} got grade {grade}")


# 19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

# items = ['shoe', 'stick', 'toy', 'fruit']

# for i, item in enumerate(items):
#     if i % 2 == 0:
#         print(f"{i}: {item}")



# 20. Given two lists of numbers of the same length, print the indices and values
# of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
# 'Index 1: 8 != 3',
# 'Index 3: 7 != 9',
# 'Index 5: 4 != 0',
# ]


# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# result = []

# for i, (list1_item, list2_item) in enumerate(zip(list1, list2)):
#     if list1_item != list2_item:
#         result.append(f"Index {i}: {list1_item} != {list2_item}")

# print(result)

# -------------------------ASSIGNMENT CORRECTION------------------------------------



# animals = ["dog", "cat", "ram", "goat", "chicken"]

# animals_copy = []

# for animal in animals:
#     animals_copy.append(animal.upper())


# print("animals:", animals)
# print("animals_copy:", animals_copy)

# animals = ["dog", "cat", "ram", "goat", "chicken"]

# animals_copy = [animal.upper() for animal in animals]

# print("animals:", animals)
# print("animals_copy:", animals_copy)




# animals = ["dog", "cat", "ram", "goat", "chicken"]
# # [3, 3, 3, 4, 7]


# animals_lens = []

# for animal in animals:
#     animals_lens.append(len(animal))


# print(animals_lens)


# animals = ["dog", "cat", "ram", "goat", "chicken"]

# animals_lens = [len(animal) for animal in animals]

# print(animals_lens)



# 0, 1, 1, 1, 0


# animals = ["dog", "cat", "ram", "goat", "chicken"]

# no_of_a = [animal.count("a") for animal in animals]

# print(no_of_a)


# name = "James"

# print(name.count("a"))




# animals = ["dog", "cat", "ram", "goat", "eagle", "chicken"]

# # [False, False, False, False, True, False]

# start_with_vowel = [animal.lower().startswith(("a", "e", "i", "o", "u")) for animal in animals]

# print(start_with_vowel)



# foods = ["garri", "bread", "beans", "rice", "akara", "ewedu", "achicha", "fish", "oha", "abacha", "pancake", "spaghetti", "yam"]

# foods_that_start_with_vowel = [food for food in foods if food.lower().startswith(("a", "e", "i", "o", "u"))]

# print(foods_that_start_with_vowel)


# movie_genre = ("comedy", "romance", "thriller", "action", "adventure", "horror", "sci-fi", "anime", "musical")


# 1. Print a list that contains each of the movies in movie_genre in uppercase form
# 2. Print a list of only the movies that have lengths less than 6




# all_countries = ["Nigeria", "USA", "Ghana", "UAE", "Canada", "Switzerland", "Japan", "Germany", "Australia", "Togo", "China"]

# developing_countries = ["Nigeria", "Togo", "Ghana"]


# developed_countries = [country for country in all_countries if country not in developing_countries]

# print(developed_countries)


# all_countries = ["Nigeria", "USA", "Ghana", "UAE", "Canada", "Switzerland", "Japan", "Germany", "Australia", "Togo", "China"]

# len_all_countries = {country: len(country) for country in all_countries}

# print(len_all_countries)


# all_countries = ["Nigeria", "USA", "Ghana", "UAE", "Canada", "Switzerland", "Japan", "Germany", "Australia", "Togo", "China"]

# start_with_vowels = {country: country.lower().startswith(("a", "e", "i", "o", "u")) for country in all_countries}
# start_with_vowels = {country: country.lower()[0] in "aeiou" for country in all_countries}


# print(start_with_vowels)



# all_countries = ["Nigeria", "USA", "Ghana", "UAE", "Canada", "Switzerland", "Japan", "UAE", "Germany", "Australia", "Togo", "China"]

# developing_countries = ["Nigeria", "Togo", "Ghana"]


# developed_countries = {country for country in all_countries if country not in developing_countries}

# print(developed_countries)



# even nos between 7 and 65
# 8, 10, 12, ..., 62, 64
# even_nos = [number for number in range(7, 65) if number % 2 == 0]
# print(even_nos)


# multiples of both 3 and 5
# 1 and 100

# 15, 45, ...

# multiples_of_3_and_5 = [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]
# print(multiples_of_3_and_5)


# multiples_of_3_and_5 = [num for num in range(1, 101) if num % 15 == 0]
# print(multiples_of_3_and_5)



# -----------------------------------------------GENERATORS------------------------------------------------------


# multiples_of_3_and_5 = (num for num in range(1, 101) if num % 15 == 0)
# print(multiples_of_3_and_5)

# print(all([True, True, False, False, True]))
# print(any([True, True, False, False, True]))  # True
# print(all([True, True, True, True, True]))
# print(all([False, False, False, False, False]))  # False
# print(any([False, False, False, False, False]))  # False



# animals = ["dog", "cat", "ram", "goat", "eagle", "chicken"]

# # [False, False, False, False, True, False]

# start_with_vowel = [animal.lower().startswith(("a", "e", "i", "o", "u")) for animal in animals]

# print(all(start_with_vowel))

# animals = ["dog", "cat", "ram", "goat", "eagle", "chicken"]

# # [False, False, False, False, True, False]

# all_start_with_vowel = all((animal.lower().startswith(("a", "e", "i", "o", "u")) for animal in animals))

# print((animal.lower().startswith(("a", "e", "i", "o", "u")) for animal in animals))
# print(all_start_with_vowel)




# 1. Create a list of Booleans indicating if each number is greater than 10  (transform)
# Input: [5, 12, 3, 18, 7]

# numbers = [5, 12, 3, 18, 7]

# print([num > 10 for num in numbers])


# 2. Create a list of all numbers greater than 10 (filter)
# Input: [5, 12, 3, 18, 7]

# numbers = [5, 12, 3, 18, 7]
# print([num for num in numbers if num > 10])


# 3. Are all the items in the list greater than 10?
# Input: [5, 12, 3, 18, 7]

# numbers = [5, 12, 3, 18, 7]

# print(all(num > 10 for num in numbers))


# # 4. Is there any item that is greater than 10?
# numbers = [5, 12, 3, 18, 7]

# print(any(num > 10 for num in numbers))


# # 1. Create a list of names that contain the letter 'a'
# # Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: ["Sara", "Amanda"]
# names = ["John", "Sara", "Mike", "Amanda"]


# # 2. Create a list of the last characters of each word
# # Input: ["dog", "cat", "lion", "tiger"]
# # Expected Output: ["g", "t", "n", "r"]
# animals = ["dog", "cat", "lion", "tiger"]



# # 3. Is there any name that contains the letter 'a'?
# # Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: True
# names = ["John", "Sara", "Mike", "Amanda"]

# # 4. Are all the words made up of only uppercase letters?
# # Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# # Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]




# text = "Portable Network Graphics"
# words = text.split()


# acronym = [word[0] for word in words]

# print("".join(acronym))



# If the user enters 3, the program should create:

# [
#   [1, 2, 3],
#   [2, 4, 6],
#   [3, 6, 9]
# ]


# [
#     [1*1, 1*2, 1*3],
#     [2*1, 2*2, 2*3],
#     [3*1, 3*2, 3*3],
# ]


# result = []  # [[1,2, 3], [2, 4, 6]]

# num = int(input("Enter a number: "))  # 3

# for i in range(1, num+1):  # 1, 2, 3
#     row = []  # 2, 4, 6
#     for j in range(1, num+1):  # 1, 2, 3
#         row.append(i * j)   
#     result.append(row)

 
# print(result)

# result = [[i * j for j in range(1, num+1)] for i in range(1, num+1)]

# print(result)


# -----------------------------------------------GENERATORS------------------------------------------------------



# is_happy = False

# is_female = True

# if is_happy and is_female:
#     print(True)
# else:
#     print(False)

# is_happy = False

# is_female = True

# print(is_happy and is_female)




# password = "Str0ngP@ssword"

# has_at_least_8_chars = len(password) >= 8

# has_upper = 

