#1  Write a function sum_numbers(a, b) that returns the sum of two numbers.
# def sum_numbers(a, b):
#     return a + b

#2  Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#     return n % 2 == 0

# print(is_even(9))
# print(is_even(4))
#3  Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n ** 0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(30))


#4  Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.

# def prime_no_upto_n():
#     n = int(input("Enter a number: "))
#     primes = []
#     for i in range(2, n +  1):
#         if is_prime(i):
#             primes.append(i)
#     print(f"prime numbers up to {n}: {primes}")
  
    
# prime_no_upto_n()
#5  Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)
#6  Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.

# def is_alliteration(two_word_string: str) -> bool:
#     splitted_word = two_word_string.lower().split()
#     return splitted_word[0][0] ==  splitted_word[1][0]

# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

#7  Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# def old_macdonald(name: str):
#     if len(name) < 4:
#         return name.capitalize()
#     else:
#         return name[0].upper() + name[1:3] + name[3].upper() + name[4: ]
    
# print(old_macdonald("macdonald"))
# print(old_macdonald("cat"))

#8  Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# def spy_game(list_of_ints: list) -> bool:
#     james_bond = [0, 0, 7]
#     bond = 0

#     for num in list_of_ints:
#         if num == james_bond[bond]:
#             bond += 1
#             if bond == len(james_bond):
#                 return True
#     return False
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))
   
#9  Write a function vol(radius) that computes the volume of a sphere given its radius.

def vol(radius):
    return (4/3) * (22 / 7) * (radius ** 3)

print(vol(3))
#10  Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
#11  Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
#12  Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
#  13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# 	Sample List: [1, 2, 3, -4]
# 	Expected output: -24
#  14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# 	Hint: Import and use the string module.
#  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# 	spar, formed from rasp.
#  16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# 	(BMI) given weight in kilograms and height in meters.
#  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# 	simple interest given principal amount, interest rate, and time (in years).

