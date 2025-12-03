# print("My name is Winnie")
# print("My name is Winnie")
# print("My name is Winnie")
# print("My name is Winnie")
# print("My name is Winnie")
# print("My name is Winnie")
# print("My name is Winnie")
# print("My name is Winnie")
# print("My name is Winnie")
# print("My name is Winnie")


# i = 1

# while i <= 10:
#     print(f"{i} My name is Winnie")
#     i += 1




# i = 5

# while i <= 25:
#     print(i)
#     i += 1


# i = 30

# while i >= 5:
#     print(i)
#     i -= 1


# 1. Count from 40 to 76, 76 is inclusive
# 2. Count from 56 to 12, showing only the even numbers.


# i = 1

# while i <= 10:
#     print(f"{i}: My name is Feyi")
#     i += 1

# i = 90

# while i >= 72:
#     print(i)
#     i -= 1


# i = 90

# numbers = []

# while i >= 72:
#     numbers.append(i)
#     i -= 1

# print(numbers)



# 1, 2, 3, 4, ..., 49, 50


# i = 1

# numbers = []

# while i <= 50:
#     numbers.append(str(i))
#     i += 1


# print(numbers)

# print(", ".join(numbers))

# import string

# i = 1

# numbers = ""

# while i <= 50:
#     numbers += str(i)
#     if i != 50:
#         numbers += ", "
#     i += 1


# print(numbers)


# print("".join(("James", "Jake", "Jack", "Jill")))  # correct
# print("".join((["James"], ["Jake"], ["Jack"], ["Jill"])))  # TypeError


# "Ife"

# Hello, Ife
# Hello, Ife
# Hello, Ife



# i = 5

# while i <= 15:
#     print(i)
#     if i == 10:
#         break
#     i += 1


# i = 4

# while i <= 14:
#     i += 1
#     if i == 10:
#         continue
#     print(i)


# Create a list containing 60 to 100, but stop when you get to 70 i.e. 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
# Create a list containing 10 to 20, but skip 15 i.e. 10, 11, 12, 13, 14, 16, 17, 18, 19, 20


# i = 5

# while i <= 15:
#     print(i)
#     i += 1
# else:
#     print("Loop has ended")



# 2. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e.g. if n is 5, do 1+2+3+4+5 (15).


# 6
# 1 + 2 + 3 + 4 + 5 + 6

# pseudocode 

# 1. Collect the number n from the user
# 2. Create a space to store the total
# 2. Count from 1 up to n
# 3. Each time, add the current number to the total


# n = int(input("Enter the number: "))

# total = 0

# i = 1

# result = []

# while i <= n:
#     result.append(str(i))
#     total += i
#     i += 1

# print(total)
# print(result)

# print(" + ".join(result) + " = " + str(total))

# 1 + 2 + 3 + 4 + 5 = 15



# n = int(input("Enter the number: "))

# i = 1

# result_str = []
# result_int = []

# while i <= n:
#     result_str.append(str(i))
#     result_int.append(i)
#     i += 1

# print(result_str)
# print(result_int)

# print(" + ".join(result_str) + " = " + str(sum(result_int)))


# n = int(input("Enter the number: "))

# i = 1

# result_int = []

# while i <= n:
#     result_int.append(i)
#     i += 1

# print(result_int)
# result_str = [str(num) for num in result_int]
# print(result_str)

# print(" + ".join(result_str) + " = " + str(sum(result_int)))


# ---------------------------------------------PRINTING SHAPES---------------------------------------
# length - 4

# ****
# ****
# ****
# ****


# length - 5

# ***** 
# *****
# *****
# *****
# *****


# length = int(input("Enter the length of the square: "))

# i = 1
# while i <= length: 
#     print("*" * length)
#     i += 1

# ---------------------------------------------PRINTING SHAPES---------------------------------------


# ---------------------------------------------ASSIGNMENT CORRECTION---------------------------------------

# 1. Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5

# i = 1

# while i <= 5:
#     print(i)
#     i += 1


# 2. Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello


# i = 0

# while i < 3:
#     print("Hello")
#     i += 1


# 3. Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10

# i = 2

# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# 4. Print numbers in reverse from 5 to 1 using a while loop.
# Expected Output:
# 5
# 4
# 3
# 2
# 1

# i = 5

# while i >= 1:
#     print(i)
#     i -= 1


# 5. Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# i = 0

# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# i = 1

# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1


# 6. Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# length = int(input("Enter the length of the square: "))

# i = 1

# while i <= length:
#     print("*" * length)
#     i += 1


# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


# 7. Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****

# height = int(input("Enter the height of the triangle: "))

# i = 1

# while i <= height:
#     print("*" * i)
#     i += 1

# 8. Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!

# EAFP

# try:
#     number = int(input("Enter the countdown start: "))
# except ValueError:
#     print("number must be an integer")
# else:
#     while number >= 1:
#         print(number)
#         number -= 1
#     else:
#         print("Go!")



# 9. Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111


# i = 1
# result = []

# while i <= 10:
#     result.append("1")
#     i += 1

# print("".join(result))


# i = 1
# result = ""

# while i <= 10:
#     result += "1"
#     i += 1

# print(result)


# 10. Print a list of the first 12 multiples of 3 starting from 3


# i = 1

# multiples_of_3 = []

# while i < 13:
#     multiples_of_3.append(i * 3)
#     i += 1

# print(multiples_of_3)

# ---------------------------------------------ASSIGNMENT CORRECTION---------------------------------------

# ---------------------------------------------ASSIGNMENT CORRECTION---------------------------------------

# 2. Write a program that uses a while loop to print numbers from 1 to 10.


# 3. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).



# 5. Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.


# 6. Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.


# 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625

# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))

# i = 1

# result = 1

# while i <= exponent:
#     # result *= base
#     result = result * base
#     i += 1


# print(result)
# ---------------------------------------------ASSIGNMENT CORRECTION---------------------------------------



# ---------------------------------------------LOOPING THROUGH ITERABLES---------------------------------------

# name = "Racheal"

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])


# name = input("Enter your name: ")

# i = 0

# # while i <= len(name) - 1:
# while i < len(name):
#     print(name[i])
#     i += 1



# musical_instruments = ["gong", "drum", "saxophone", "guitar", "keyboard"]


# 1. gong
# 2. drum
# 3. saxophone
# 4. guitar
# 5. keyboard

# ---------------------------------------------LOOPING THROUGH ITERABLES---------------------------------------

# ---------------------------------------------INFINITE LOOPS---------------------------------------


# while True:
#     num = int(input("Enter an even number: "))

#     if num % 2 == 0:
#         print("Done")
#         break

#     print(f"{num} is not even")

# number = 7
# while number >= 1:
#     print(number)
#     number -= 1
#     if number == 3:
#         break
# else:
#     print("Go!")


# is_odd = True

# while is_odd:
#     num = int(input("Enter an even number: "))

#     if num % 2 == 0:
#         print("Done")
#         is_odd = False
#         continue

#     print(f"{num} is not even")
# else:
#     print(f"Else block")





# ---------------------------------------------INFINITE LOOPS---------------------------------------



# musical_instruments = ["gong", "drum", "saxophone", "guitar", "keyboard"]

# gong
# g
# o
# n
# g

# drum
# d
# r
# u
# m



# i = 0

# while i < len(musical_instruments):
#     instrument = musical_instruments[i]
#     print(instrument)
#     j = 0
#     while j < len(instrument):
#         print(instrument[j])
#         j += 1
#     i += 1


# i = 0

# while i < len(musical_instruments):
#     instrument = musical_instruments[i]
#     print("i:", i)
#     j = 0
#     while j < len(instrument):
#         print("j:", j)
#         j += 1
#     i += 1



# musical_instruments = ["gong", "drum", "saxophone", "guitar", "keyboard"]
# class_of_instrument = ["percussion", "percussion", "woodwind", "string", "chordophone"]


# i = 0

# while i < len(musical_instruments):
#     print(f"{musical_instruments[i]} is a/an {class_of_instrument[i]} instrument")
#     i += 1


# musical_instruments = ["gong", "drum", "saxophone", "guitar", "keyboard"]
# class_of_instrument = ["percussion", "percussion", "woodwind", "string", "chordophone", "idiophone"]


# shorter_list = min([musical_instruments, class_of_instrument])


# i = 0

# while i < len(shorter_list):
#     print(f"{musical_instruments[i]} is a/an {class_of_instrument[i]} instrument")
#     i += 1


# 1. Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350


# balance = int(input("Enter your balance: "))

# while True:
#     withdrawal_amount = int(input("ENter withdrawal amount: "))

#     if withdrawal_amount < balance:
#         balance -= withdrawal_amount
#         print(f"Remaining balance: {balance}")
#     else:
#         print("Insufficient funds")

#     another_withdrawal = input("Do you want to make anoher withdrawal? (yes/no): ").lower()

#     if another_withdrawal != "yes":
#         print(f"Final Balance: {balance}")
#         break


# balance = int(input("Enter your balance: "))

# keep_asking = True

# while keep_asking:
#     withdrawal_amount = int(input("Enter withdrawal amount: "))

#     if withdrawal_amount < balance:
#         balance -= withdrawal_amount
#         print(f"Remaining balance: {balance}")
#     else:
#         print("Insufficient funds")

#     while True:
#         another_withdrawal = input("Do you want to make anoher withdrawal? (yes/no): ").lower()

#         if another_withdrawal not in ["yes", "no"]:
#             print("Invalid input, enter yes or no only")
#             continue

#         if another_withdrawal == "no":
#             print(f"Final Balance: {balance}")
#             keep_asking = False
#             break



# ---------------------------------------ASSIGNMENT CORRECTION---------------------------------------------------
# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.


# import random

# secret_num = random.randint(1, 50)

# from random import randint

# secret_num = randint(1, 50)

# attempts_left = 5

# while attempts_left >= 1:
#     guess = int(input("Guess the secret number: "))

#     # if not(1 <= guess <= 50):
#     if guess < 1 or guess > 50:
#         print("You must guess between 1 and 50.")
#         continue

#     if guess == secret_num:
#         print("Congratulations!!! 🎊🎉. You guessed the number correctly.")
#         break

#     if guess < secret_num:
#         print("You guessed too low.")
#     else:
#         print("You guessed too high.")

#     attempts_left -= 1

#     print(f"You have {attempts_left} attempts left.")
# else:
#     print(f"Sorry, better luck next time. 🥲  You have used up all your attempts. The secret number was {secret_num}")



# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# from getpass import getpass

# CORRECT_PASSWORD = "secret"

# while True:
#     password = getpass("Enter the password: ").strip()
#     if password == CORRECT_PASSWORD:
#         print("Password is correct")
#         break

#     print("Invalid password")

# bello
# CORRECT_PASSWORD = "secret"
# password = ""

# while password != CORRECT_PASSWORD:
#     password = getpass("Enter the password: ").strip()

#     if password != CORRECT_PASSWORD:
#         print('Invalid password')
# else:
#     print("Password is correct")

# Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625


# 8. Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.

# I am John!

# 1. Go through every char in the string
# 2. Check if it is a vowel
# 3. If it is, we will increase the count of vowels by 1
# 4. Otherwise, we will skip it

# crypt

# text = input("Enter some text: ").strip().lower()

# vowels = "aeiou"

# no_of_vowels = 0

# i = 0

# while i < len(text):
#     char = text[i]

#     if char in vowels:
#         no_of_vowels += 1

#     i += 1

# print(f"No of vowels: {no_of_vowels}")

# 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().

# Python

# 012345

# text = input("Enter some text to reverse: ").strip()

# idx = len(text) - 1

# reversed_text = []

# while idx >= 0:
#     char = text[idx]
#     reversed_text.append(char)
#     idx -= 1

# reversed_text = "".join(reversed_text)

# print(reversed_text)
# sugar

# ""
# "u" + "s" -> "us"
# "g" + "us" -> "gus"
# "a" + "gus" -> "agus"
# "r" + "agus" -> "ragus"

# text = input("Enter some text to reverse: ").strip()

# idx = 0

# reversed_text = []

# while idx < len(text):
#     char = text[idx]
#     reversed_text.insert(0, char)
#     print(reversed_text)
#     idx += 1

# reversed_text = "".join(reversed_text)

# print(reversed_text)


# text = input("Enter some text to reverse: ").strip()

# idx = 0

# reversed_text = ""

# while idx < len(text):
#     char = text[idx]
#     # reversed_text += char
#     reversed_text = char + reversed_text
#     print(reversed_text)
#     idx += 1

# print(reversed_text)

# 10. Write a program that takes comma-separated integers from the user, converts that
# to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
# Use the min() function.

# "6, 8, 1, 7"

# numbers = input("Enter comma-separated numbers: ").split(",")

# print(numbers)

# smallest = int(numbers[0])

# i = 1

# while i < len(numbers):
#     number = int(numbers[i])
#     if number < smallest:
#         smallest = number
#     i += 1

# print(numbers)

# print(f"{smallest} is the smallest")


# 11. Write a program that takes a string input from the user and uses a while loop to count
# the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# halloween

# {'h': 1, 'a': 1, 'l': 2, 'o': 1, 'w': 1, 'e': 2, 'n': 1}

# 1. Go through every char in the string
# 2. Keep track of how many times you have seen each char
# 3. If you have seen the char before, increase its count by 1
# 4. If not, register it as the first time


# text = input("Enter some text: ").lower().strip()

# i = 0

# occurences = {}

# while i < len(text):
#     char = text[i]
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1
#     i += 1

# print(occurences)


# ---------------------------------------ASSIGNMENT CORRECTION---------------------------------------------------




# ---------------------------------------ASSIGNMENT CORRECTION---------------------------------------------------

# 2. Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48


# total_cost = 0

# while True:
#     item_price = float(input("Enter item price: "))

#     total_cost += item_price

#     another_item = input("Enter another item? (yes/no): ").strip().lower()

#     if another_item != "yes":
#         print(f"Total cost: {total_cost}")
#         break


# 3. Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

# while True:
#     password = input("Enter password: ").strip()

#     if 8 <= len(password) <= 25:
#         print("Password accepted.")
#         break

#     print("Password must be at least 8 characters long and have a maximum of 25 characters.")


# 4. Write a program that asks for the user's age and keeps prompting them until they 
# enter a valid age (greater than or equal to 0).
# Sample Input and Output:
# Enter your age: -5
# Invalid age. Please enter a valid age.
# Enter your age: 25
# Age accepted.



# 5. Write a program that tracks the inventory of items in a store. The user should be able 
# to add or remove items and the program should display the current inventory after each
# operation. The program stops when the user decides to exit.
# The current store inventory is {'eggs': 40, 'fish': 200, 'bread': 343, 'yam':2}
# Sample Input and Output:
# Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit


# inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}


# while True:
#     operation = input("Enter operation (add/remove/exit): ").strip().lower()
    
#     if operation not in ["add", "remove", "exit"]:
#         print("Invalid operation")
#         continue

#     if operation == "exit":
#         break
    

#     item = input("Enter item: ").strip()
#     quantity = int(input("Enter quantity: "))

#     if operation == "add":

#         if item in inventory:
#             inventory[item] += quantity
#         else:
#             inventory[item] = quantity
#     elif operation == "remove":
#         if item in inventory:
#             inventory[item] -= quantity
#         else:
#             print(f"You cannot remove {item}. {item} is not in the inventory.")

#     print(f"Current inventory: {inventory}")

# ---------------------------------------ASSIGNMENT CORRECTION---------------------------------------------------



