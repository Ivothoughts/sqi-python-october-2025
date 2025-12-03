"""This module teaches you how to write functions"""

# def say_hi():
#     print('hi')

# print("Hello")

# say_hi()
# say_hi()
# say_hi()
# say_hi()
# say_hi()
# say_hi()

# [78, 793].append()


# def greet():
#     print("Good afternoon, SQI Oct Python Gurus")  # 1
#     print("inside function")  # 2


# print(greet())



# def greet():
#     print('Hello World!')  # 3

# greet()
# print('Outside function')  # 4





# print("Lorem ipsum dolor")  # 1
# def greet():
#     print("sit amet")  # 3, 6
#     print('Hello World!')  # 4, 7

# print('tempor incididunt ut labore')  # 2
# greet()
# print("consectetur adipiscing elit")  # 5
# greet()
# print("Nemo enim ipsam voluptatem")  # 8


# print("The sun rises in the east")  # 9


# def greet():
#     print("How's it going?")  # 1, 4, 6, 9
#     print("Stay curious, stay kind.")  # 2, 5, 7, 10


# greet()

# print("Midnight thoughts and coffee sips")  # 3
# greet()
# greet()
# print("Learning never exhausts the mind")  # 8
# greet()
# print("Wander often, wonder always")  # 11


# def square_num(num):
#     # return num ** 2
#     print(num ** 2)


# square_num(4)


# def greet1():
#     print("Hello")

# greet1("Winnie")


# def greet2(username):
#     print(username)
#     print(f"Hello, {username}!")

# greet2("Towi")

# Write a function introduction with a parameter name that prints "I am {name}".

# def add_two_nums(num1, num2):  # parameters
#     print(num1 + num2)

# add_two_nums(9, 10)  # arguments/args
# add_two_nums(2, 7)


# Write a function raise_to_power that takes in two parameters base and exponent and 
# prints base raised to the power of exponent.

# def raise_to_power(base: int, exponent: int) -> int:
#     return base ** exponent

# print(raise_to_power(2, 3))  # 8
# result = raise_to_power(2, 3)
# print(result)  # 8



# # my_list = [1, 2, 3]
# my_list = ['1', '2', '3']
# print(my_list.pop())
# # print(popped_item)
# print(my_list)



# Write a function change_to_lower with parameter word.
# Return the word lowercased.
# Print what is returned.

# Python and Javascript is dynamically typed
# Other languages like Java and C are statically typed


# type hints or type annotations

# def change_to_lower(word):
#     return word.lower()


# # print(change_to_lower("HELLO"))
# lowercase_word = change_to_lower("HELLO")
# # lowercase_word = change_to_lower(123)
# print(lowercase_word)



# Create a function upper_everyone that has parameter names which is a lit of strings where
# each istring is a name.
# Return a list of names where all the names are uppercased.

# def upper_everyone(names: list[str]) -> list[str]:
#     names.append("something")
#     return [name.upper() for name in names]

# print(upper_everyone(["Jade", "Joy", "James", "Janet", "Jack"]))

# ["JADE", "JOY", "JAMES", "JANET", "JACK"]



# nums: list[int] = [1, 2, 3]


# inventory: dict[str, int] = {"apples": 10, "bananas": 12, "oranges": 9}

# inventory: dict[str, int|str] = {"apples": 10, "bananas": 12, "oranges": "nine"}


# def greet():
#     pass


# print("Hey")



# # -----------------------------------------------ASSIGNMENT-------------------------------------------------
# 1. Create a function starts_with_m(word) that returns True if the word starts with the letter `m`.
# Otherwise, the function returns False
# Print the result of the function

# def starts_with_m(word: str):
#     return word.lower().startswith("m")

# def beginner_starts_with_m(word: str):
#     if word.lower().startswith("m"):
#         return True
#     else:
#         return False

# def intermediate_starts_with_m(word: str):
#     if word.lower().startswith("m"):
#         return True
#     return False


# print(starts_with_m("Maddie"))  # True
# print(starts_with_m("John"))  # False
# print(starts_with_m("marry"))  # True




# 2. Create a function is_even(num) that returns True if num is an even number.
# Otherwise, the function returns False
# Print the result of the function

# def is_even(num: int):
#     return num % 2 == 0

# print(is_even(3))  # False
# print(is_even(6))  # True


# 6. Write a function is_alliteration(two_word_string) that takes a two-word string and returns True if both words begin with the same letter.
# is_alliteration("Levelheaded llama") —> True
# is_alliteration("Crazy Kangaroo") –> False





# ----------------------------ASSIGNMENT CORRECTIONP--------------------------

# 1. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# after, print the result of the function.
# For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]

# def turn_to_upper(names: list[str]):
#     return [name.upper() for name in names]

# print(turn_to_upper(["Winifred", "Wilfred", "Justin", "Augusta"]))


# 2. Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys "first", "middle", and "last".
# The function should return only the middle name.
# For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"}, then the result would be "James". Another example is if name_dict is {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".


# def get_middle_name(name_dict: dict[str, str]) -> str: 
#     return name_dict["middle"]

# print(get_middle_name({"first": "Tola", "middle": "James", "last": "Akin"}))
# print(get_middle_name({"middle": "Chioma", "first": "Ada", "last": "Okeke"}))
# print(get_middle_name({"first": "Ada", "last": "Okeke"}))


# def get_middle_name(name_dict: dict[str, str]) -> str: 
#     if "middle" not in name_dict:
#         return
#     return name_dict["middle"]

# print(get_middle_name({"first": "Tola", "middle": "James", "last": "Akin"}))
# print(get_middle_name({"middle": "Chioma", "first": "Ada", "last": "Okeke"}))
# print(get_middle_name({"first": "Ada", "last": "Okeke"}))


# def get_middle_name(name_dict: dict[str, str]) -> str: 
#     return name_dict.get("middle", "No middle name")

# print(get_middle_name({"first": "Tola", "middle": "James", "last": "Akin"}))
# print(get_middle_name({"middle": "Chioma", "first": "Ada", "last": "Okeke"}))
# print(get_middle_name({"first": "Ada", "last": "Okeke"}))

# 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# For example, if the string is "Python", the result would be "nohtyP".


# def reverse_string(text):
#     return text[::-1]
#     # return "".join(list(reversed(text)))


# print(reverse_string("Python"))

# 4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# For example, if the string is "beautiful", the result would be 5.

# def count_vowels(text: str) -> int:
#     vowels = "aeiou"
#     no_of_vowels = 0
#     for char in text:
#         if char in vowels:
#             no_of_vowels += 1
#     return no_of_vowels

# print(count_vowels("beautiful"))


# def count_vowels(text: str) -> int:
#     vowels = "aeiou"
#     return sum(char in vowels for char in text)

# print(count_vowels("beautiful"))

# 5. Create a function called even_numbers that takes in a list of integers and returns a new list containing only the even numbers.
# For example, if the list is [1, 2, 3, 4, 5, 6], the result would be [2, 4, 6].


# def even_numbers(numbers: list[int]) -> list[int]:
#     return [num for num in numbers if num % 2 == 0]


# print(even_numbers([1, 2, 3, 4, 5, 6]))

# 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# For example, if the list is [12, 45, 3, 67, 23], the result would be 67.

# def find_max(numbers: list[int]) -> int:
#     if not numbers:
#         return
#     return max(numbers)

# print(find_max([]))
# print(find_max([12, 45, 3, 67, 23]))


# 7. Create a function called sum_dict_values that takes in a dictionary with numeric values and returns the sum of all the values.
# For example, if the dictionary is {"a": 10, "b": 20, "c": 5}, the result would be 35.

# def sum_dict_values(numbers: dict[str, int]) -> int:
#     return sum(numbers.values())

# print(sum_dict_values({}))
# print(sum_dict_values({"a": 10}))
# print(sum_dict_values({"a": 10, "b": 20, "c": 5}))

# 8. Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# For example, if the list is ["apple", "banana", "cherry"], the result would be {"apple": 5, "banana": 6, "cherry": 6}.


# def word_lengths(words: list[str]) -> dict[str, int]:
#     return {word: len(word) for word in words}


# print(word_lengths(["apple", "banana", "cherry"]))
# print(word_lengths([]))

# 9. Create a function called is_palindrome that takes in a string and returns True if the string is a palindrome (same forwards and backwards), otherwise False.
# For example, if the string is "level", the result would be True. If the string is "hello", the result would be False.

# def is_palindrome(text: str) -> bool:
#     text = text.lower().replace(" ", "")
#     return text == text[::-1]


# print(is_palindrome("hello"))  # False
# print(is_palindrome("madam"))  # True
# print(is_palindrome(text="madam"))  # True

# 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# For example, if list1 = [1, 2, 3] and list2 = [3, 4, 5], the result would be [1, 2, 3, 4, 5].


# def merge_lists(list1: list[int], list2: list[int]) -> list[int]:
#     return list(set(list1 + list2))

# print(merge_lists([1, 2, 3], [3, 4, 5]))


# def merge_lists(list1: list[int], list2: list[int]) -> list[int]:
#     merged_list = []

#     temp_merged_list = list1 + list2
#     for num in temp_merged_list:
#         if num not in merged_list:
#             merged_list.append(num)

#     return merged_list
    

# print(merge_lists([1, 2, 3], [3, 4, 5]))


# def greet(time_of_day="day", name="Anonymous"):
#     return f"Good {time_of_day}, {name}"

# # positional - args

# print(greet("Morning", "Ella"))
# print(greet("Morning"))
# print(greet())


# Keyword arguments - kwargs

# print(greet(name="Winnie"))



# def greet(time_of_day="day", name="Anonymous"):
#     return f"Good {time_of_day}, {name}"


# # 

# def greet():
#     time_of_day = input("Enter the time of day: ")
#     name = input("Enter your name: ")
#     return f"Good {time_of_day}, {name}"


# # result = greet()


# # print(f"The result is {result}")

# def count_chars(text: str) -> int:
#     return len(text)

# # print(count_chars(result))
# print(count_chars(greet()))


# def greet():
#     time_of_day = input("Enter the time of day: ")
#     name = input("Enter your name: ")
#     return f"Good {time_of_day}, {name}"

# def main_func(greet_func) -> int:
#     return len(greet_func())

# # print(main_func(result))
# print(main_func(greet))


# print(len(greet()))


# def square_num(num):
#     return num ** 2


# print(square_num(7))


# square_number = square_num


# print(square_number(6))


# 11. Create a function called multiply_numbers(a, b=2) that multiplies two numbers.
# If the second number is not provided, it should default to 2.
# Example 1: multiply_numbers(5) → 10
# Example 2: multiply_numbers(5, 3) → 15


# def multiply_numbers(a, b=2):
#     return a * b

# # print(multiply_numbers(5))  # 10
# # print(multiply_numbers(5, 3))  # 15
# print(multiply_numbers(b=5, a=3))  # 15
# print(multiply_numbers(b=5))  # 15


# 12. Create a function called greet_user(first_name, last_name="") that returns a greeting string.
# If last_name is not provided, it should only greet with the first name.
# Example 1: greet_user("Ada") → "Hello, Ada!"
# Example 2: greet_user("Tola", "Akin") → "Hello, Tola Akin!"

# def greet_user(first_name, last_name=""):
#     full_name = ""
#     if not last_name:
#         full_name = first_name
#     else:
#         full_name = f"{first_name} {last_name}"
#     return f"Hello, {full_name}!"


# print(greet_user("Ada"))
# print(greet_user("Tola", "Akin"))


# def greet_user(first_name, last_name=""):
#     if not last_name:
#         return f"Hello, {first_name}!"
#     return f"Hello {first_name} {last_name}!"


# print(greet_user("Ada"))
# print(greet_user("Tola", "Akin"))

# 13. Create a function called power(base, exponent=2) that raises the base to the power of the exponent.
# The exponent should default to 2 (square).
# Example 1: power(4) → 16
# Example 2: power(2, 3) → 8

# 14. Create a function called format_full_name(first, middle="", last="") that returns the full name as a single string.
# If middle or last is not provided, it should still work correctly.
# Example 1: format_full_name("John", "Paul", "Smith") → "John Paul Smith"
# Example 2: format_full_name("Ada", last="Okeke") → "Ada Okeke"

# 15. Create a function called calculate_discount(price, discount=10, tax=0) that calculates the final price after applying a discount (percentage) and then adding tax (percentage).
# Example 1: calculate_discount(100) → 90.0   (10% discount, no tax)
# Example 2: calculate_discount(200, discount=20, tax=5) → 168.0


# def calculate_discount(price, discount=10, tax=0):
#     discounted_amount = price - ((discount / 100) * price)
#     return discounted_amount + ((tax / 100) * discounted_amount)

# print(calculate_discount(100))
# print(calculate_discount(200, tax=5, discount=20))

# ----------------------------ASSIGNMENT CORRECTIONP--------------------------




# def say_hi_to_everyone(everyone: tuple[str]):
#     for somebody in everyone:
#         return f"Hello, {somebody} 👋"
    

# print(say_hi_to_everyone(("Jenny", "Blessing", "Francis", "Ife", "Tobi", "Sarah", "Towi")))


# def say_hi_to_everyone(everyone: tuple[str]):
#     for somebody in everyone:
#         print(f"Hello, {somebody} 👋")
    
    

# print(say_hi_to_everyone(("Jenny", "Blessing", "Francis", "Ife", "Tobi", "Sarah", "Towi")))

# def say_hi_to_everyone(*everyone):
#     print(everyone)
#     for somebody in everyone:
#         print(f"Hello, {somebody} 👋")
    
    

# # print(say_hi_to_everyone("Jenny", "Blessing", "Francis", "Ife", "Tobi", "Sarah", "Towi"))
# print(say_hi_to_everyone(("Jenny", "Blessing", "Francis", "Ife", "Tobi", "Sarah", "Towi")))



# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list3 = [*list1, *list2]

# print(list3)




# -------------------------------------ARGS AND KWARGS---------------------------------


# arbitrary number of args - *args
# def turn_to_upper(*wristwatch_brands):
#     return [brand.upper() for brand in wristwatch_brands]


# result = turn_to_upper("Patek Philippe", "Rolex", "Armani", "Richard Milli", "Hublot", "G-Shock", "Quartz")

# print(result)


# def add_2_nums(num1, num2):
#     return num1 + num2


# def add_all_nums(*numbers):
#     return sum(numbers)

# print(add_all_nums(9, 4, 9, 12, 6, 45, 10, 6))


# **kwargs - arbitrary no of keyword args

# def states_and_capitals(**states_and_their_capitals):
#     print(states_and_their_capitals)
#     for state, capital in states_and_their_capitals.items():
#         print(f"The capital of {state} is {capital}")


# states_and_capitals(ondo="Akure", oyo="Ibadan", enugu="enugu", ogun="Abeokuta", lagos="Ikeja")


# states_and_their_capitals = {'Ondo': 'Akure', 'Oyo': 'Ibadan', 'enu gu': 'enugu', 'ogun': 'Abeokuta', 'lagos': 'Ikeja'}

# states_and_capitals(**states_and_their_capitals)



# def figures_to_words(**figures_and_words):
#     for figure, word in figures_and_words.items():
#         print(f"{figure} -> {word}")


# # print(figures_to_words(12="twelve", 14="fourteen"))
# figures_and_words = {
#     "12": "twelve",
#     "14": "fourteen"
# }
# print(figures_to_words(**figures_and_words))



# def say_hi(name):
#     return f"Hi, {name}"


# # name = "John"

# # print(say_hi(name))

# my_name = "John"

# print(say_hi(my_name))


# mypy - type checker 
# linter - pylance

# -------------------------------------ARGS AND KWARGS---------------------------------

# -------------------------------------RECURSION---------------------------------


# def power(base, exponent):
#     # if exponent == 0:
#     #     return 1
#     # else:
#     return base * power(base, exponent - 1)

# print(power(2, 3))  # Output: 8


# 2 * power(2, 2)
# 2 * 2 * power(2, 1)
# 2 * 2 * 2 * power(2, 0)
# 2 * 2 * 2 * 1 -> 8


# -------------------------------------RECURSION---------------------------------




# -------------------------------------VARIABLE SCOPE---------------------------------

# name = "Before func call"  # global scope

# def my_func():
#     global name
#     name = "My func"  # local scope
#     print(name)



# print(name)  # Before func call

# my_func()  # My func

# print(name)  # My func



# name = "Before func call"  # global scope

# def my_func():
#     my_name = "My func"  # local scope
#     print(my_name)



# print(name)  # Before func call

# my_func()  # My func

# print(name)  # Before func call

# -------------------------------------VARIABLE SCOPE---------------------------------



# -------------------------------------DOCSTRINGS---------------------------------

# def add_two_nums(num1: int, num2: int) -> int:
#     """
#     This function adds 2 integers num1 and num2
#     Returns the result.
#     """
#     result = num1 + num2

#     return result


# print(add_two_nums(7, 3))

# print(help(add_two_nums))

# print(help(print))

# -------------------------------------DOCSTRINGS---------------------------------



# -------------------------------------ASSIGNMENT CORRECTION---------------------------------


# 1. Write a function sum_numbers(a, b) that returns the sum of two numbers.
# 2. Write a function is_even(n) that returns True if n is even and False if n is odd.
# 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

def is_prime(n):
    # if n <= 1:
    #     return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# print(is_prime(4))  # False
# print(is_prime(73)) # True


# assert is_prime(2) == True
# assert is_prime(72) == False
# assert is_prime(0) == False
# assert is_prime(123) == False
# assert is_prime(13) == True


# 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.


# def list_primes_up_to_n():
#     limit = int(input("Enter the limit: "))
#     return [i for i in range(2, limit+1) if is_prime(i)]


# print(list_primes_up_to_n())

# def list_first_n_primes():
#     n = int(input("Enter the value of n: "))

#     first_n_primes = []
#     i = 2

#     while len(first_n_primes) <= n - 1:
        
#         if is_prime(i):
#             first_n_primes.append(i)
#         i += 1
#     return first_n_primes


# print(list_first_n_primes())  # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, and 71.

# 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     return max(a, b)


# print(lesser_of_two_evens(4, 6))  # 4
# print(lesser_of_two_evens(3, 6))  # 6
# print(lesser_of_two_evens(3, 7))  # 7



# 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False


# 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# old_macdonald(‘macmahon’) —> MacMahon
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# def old_macdonald(name: str):
#     if len(name) < 4:
#         return name.capitalize()
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

# print(old_macdonald('macdonald'))  # —> MacDonald
# print(old_macdonald('macmahon'))  # —> MacMahon
# print(old_macdonald('mac'))  # —> MacDonald

# 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False


# def spy_game(list_of_ints: list[int]):
#     pattern = [0, 0, 7]

#     i = 0
#     for num in list_of_ints:
#         if num == pattern[i]:
#             i += 1

#         if i == 3:
#             return True
    
#     return False

# print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # —> True
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # —> True
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # —> False


# def spy_game(list_of_ints: list[int]):
#     pattern = [0, 0, 7]

#     for num in list_of_ints:
#         if pattern and num == pattern[0]:
#             pattern.pop(0)

#     return not pattern


# def spy_game(list_of_ints: list[int]):
#     pattern = [0, 0, 7]

#     for num in list_of_ints:
#         if num == pattern[0]:
#             pattern.pop(0)

#         if not pattern:
#             return True

#     return False



# print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # —> True
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # —> True
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # —> False

# 9. Write a function vol(radius) that computes the volume of a sphere given its radius.

# 10. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).

# def range_check(num, low, high):
#     return low <= num <= high


# def range_check(num, low, high):
#     return num in range(low, high+1)


# print(range_check(4, 2, 9))  # True
# print(range_check(4, 4, 9))  # True
# print(range_check(9, 4, 9))  # True
# print(range_check(100, 4, 9))  # False
# print(range_check(2, 4, 9))  # False


# 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.

# 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
# 13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# Sample List: [1, 2, 3, -4]
# Expected output: -24

# def multiply(list_items: list[int]):
#     product = 1

#     for num in list_items:
#         # product *= num
#         product = product * num

#     return product


# 14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# least once. For example: “The quick brown fox jumps over the lazy dog”.
# Hint: Import and use the string module.

# import string

# def is_pangram(text: str):
#     text = text.lower()
#     alphabets = string.ascii_lowercase
#     for char in alphabets:
#         if char not in text:
#             return False
        
#     return True

# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("The quick brown fox"))


# import string

# def is_pangram(text: str):
#     text = text.lower()
#     alphabets = set(string.ascii_lowercase)
#     return alphabets.issubset(text)
#     # return alphabets <= set(text)
    

# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("The quick brown fox"))

# 15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# other. a word, phrase, or name formed by rearranging the letters of another, such as
# spar, formed from rasp.

# def are_anagrams(s1: str, s2: str) -> bool:
#     s1, s2 = s1.lower().replace(" ", ""), s2.lower().replace(" ", "")
#     return sorted(s1) == sorted(s2)


# print(are_anagrams("spar", "rasp"))  #  True
# print(are_anagrams("angel", "angle"))  # True
# print(are_anagrams("Eleven plus two", "Twelve plus one"))  # True
# print(are_anagrams("hello", "young"))  # False



# 16. Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# (BMI) given weight in kilograms and height in meters.


# def calculate_bmi(weight: float, height: float) -> float:
#     return round(weight / (height ** 2), 2)

# print(calculate_bmi(70, 1.70))


# def calculate_bmi(weight: float, height: float) -> str:
#     bmi = round(weight / (height ** 2), 2)

#     # Underweight: Below 18.5
#     # Normal Weight: 18.5 to 24.9
#     # Overweight: 25.0 to 29.9
#     # Obese: 30.0 or greater 

#     if bmi < 18.5:
#         return "You are underweight"

#     if 18.5 <= bmi <= 24.9:
#         return "You weight is normal"
    
#     if 25.0 <= bmi <= 25.0:
#         return "You are overweight"
    
#     return "You are obese"

# # print(calculate_bmi(70, 1.70))
# # print(calculate_bmi(85, 1.68))
# print(calculate_bmi(63, 1.7))



# 17. Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# simple interest given principal amount, interest rate, and time (in years).



# -------------------------------------ASSIGNMENT CORRECTION---------------------------------