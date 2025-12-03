#1 Write a program that uses a while loop to print numbers from 1 to 10.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1


#2 Write a program that takes an integer n from the user and calculates the sum of all 
n = int(input("Enter a number: "))
total_sum = sum(range(1, n +1))
# if n < 0:
#     print("Enter a positive integer")
# else:
#     print(f"The sum of all integers from 1 to {n} is {total_sum}")

# --------------------------------------------------OR----------------------------------------------------------------------

# n = int(input("Enter a number: "))
# total_sum = n * (n + 1) // 2
# if n < 0:
#     print("Enter a positive integer")
# else:
#     print(f"The sum of all integers from 1 to {n} is {total_sum}")


#3 natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).
# n = int(input("Enter a number: "))
# i = 1
# total = 0
# while i <= n:
#     total += i
#     i += 1

# print(total)


#4 Write a program that generates a random secret number between 1 and 50. Use a while loop to allow the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.
import random

secret_number = random.randint(1, 50)
# secret_number = set(range(1,51))
# i = 0
# max_attempts = 5

# while i < max_attempts:
#     guess = int(input("guess your first number: "))
#     i += 1
#     if guess < 0:
#         print("invalid input !")
#     elif guess == secret_number:
#         print("Correct ! you guessed the secret number")
#         break
#     elif guess > secret_number:
#         print("Too high !, try a lower number")
#     elif guess < secret_number:
#         print("Too low !, try a higher number")
# if i == max_attempts and guess != secret_number:
#     print(f"Out of attempts the secret number is {secret_number} ")
    


#5 Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.
import getpass
# password = "secret"
# while True:
#     security = getpass.getpass("Enter your password: ")
#     if security == password:
#         print("Access granted")
#         break
#     else:
#         print("Incorrect password. Try again. ")

#6 Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
# user_input = int(input("Enter a number: "))
# while user_input >= 0 :
#     print(user_input)
#     user_input -= 1

#7 Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# n = int(input("Enter any number: "))
# i = 2
# while i <= n:
#         print(i)
#         i += 2

#8 Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
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
# power = int(input("Enter the exponent: "))

# result = 1
# i = 0

# while i < power:
#         result *= base
#         i += 1

# print(f"{base} raised to the power of {power} is {result}")

#8 Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.

string_input = input("Enter a string: ").lower()
vowels = ["a", "e", "i", "o", "u"]
count = 0
i =0
while i < len(string_input):
        if string_input[i] in vowels:
                count += 1
        i += 1
                
print("Number of vowels: ", count)


#9 Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().

string = input("Enter a string: ")
reversed_str = ""
i = len(string) - 1

while i >= 0:
    reversed_str += string[i]
    i -= 1

print("Reversed string: ", reversed_str)

# 10.	Write a program that takes comma-separated integers from the user, converts that to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
# Use the min() function.


# user_input = input("Enter comma-separated integers: ")
# numbers = tuple(map(int, user_input.split(',')))


# i = 0
# minimum = numbers[0]


# while i < len(numbers):
#     if numbers[i] < minimum:
#         minimum = numbers[i]
#     i += 1


# print("Minimum value in the tuple is:", minimum)


# ----------------------------------part 2------------------------------------------------------
#1 Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5

# n = 5
# i = 1
# while i <= n:
#     print(i)
#     i += 1

#2 Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello

# i = 0
# text = "Hello"
# while i < 3:
#     print(text)
#     i += 1

# 5.	Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
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
 
# i = 1

# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1

# 6. 	Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

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

# n = int(input("Enter a number: "))


# i = 0

# while i < n:
#     print("*" * n)
#     i += 1



# 7.	Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****


# n = int(input("Enter a number: "))


# i = 1

# while i <= n:
#     print("*" * i)
#     i += 1

# height = int(input("Enter a number:"))

# i = 1

# while height >= i:
#     print("*" * height)
#     height -= 1


# sentence = input("Enter a sentence: ").strip()
# i = 0

# while i < len(sentence):
#     print(sentence[i])
#     i += 1


# musical_instrument = ["gong", "drum", "saxophone", "guitar", "keyboard"]

# i = 0

# while i < len(musical_instrument):
#     print(f"{i + 1}. {musical_instrument[i]} ")
#     i += 1


while True:
    food = input("Enter your favourite food: ").lower()
    if food.startswith("r"):
        print("That's the real deal")
        break
    if len(food) > 10:
        print("wake up!")
        continue

    print("That is a very bad choice")
