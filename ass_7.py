# Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".

name = input("What is your name?: ")
print(f"Hello, {name}!")

# Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.

from datetime import datetime
current_year = datetime.now().year

birth_year = input("What year were you born?: ")
age = current_year - int(birth_year)
print("You are {} years old.".format(age))


# Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.

fav_col = input("What is your favourite color?: ")
print("Your favourite color is " + fav_col + ".")


# Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.

text = input("Input any text!: ")
text = text.replace(" ","").lower()
is_palindrome = text == text[::-1]
print(f"It is {is_palindrome} that {text} is a palindrome.")



# Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.

from getpass import getpass
password = getpass("Input password: ")
is_valid = 8 <= len(password) <= 30
print(f"It is {is_valid} that the password fulfils the criteria.")

# Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.

weight = float(input("What is your weight in kg?: "))
height = float(input("What is your height in meters: "))
BMI = round(((weight) / (height ** 2)), 2)
print(f"Your BMI is {BMI}")

# Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.

x, y, z = "Orange", "Banana", "Cherry"

# Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# single line.

age, name, is_student = 10, "John", True

# Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.

x, y = 5 , 10
print("{1} {0}".format(5,10))

# Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# variables a, b, and c.

a, b, c = 1,2,3
print(a) 
print(b)
print(c)

# Convert a string variable called height from “1.35” to a float.

height = "1.35"
height = float(height)
# print(type(height))

# Predict the output of the following statements:
# a) bool("") #False
# b) bool(123) #True
# c) bool(["apple", "cherry", "banana"]) #True
# d) bool(False) #True
# e) bool(None) #False
# f) bool(0) #False
# g) bool("abc") #True
# h) bool(()) #False
# i) bool([]) #False
# j) bool({}) #False
