# IndexError - try to access an iterable out of range
# e.g: 
# "John"[100]
# ["apple", "banana", "cherry"][3]


# TypeError - try to do an operation that is unsupported by the data type(s)
# e.g:

# 12[9]

# 7 + "8"

# {"blue", "orange", "silver"}["blue"]


# def greet():
#     return "Hi"

# greet("John")


# AttributeError - trying to access a non-existent or unsuppoorted attribute 
# e.g:
# age = 12
# age.append()


# KeyError - try to access non-existent key of a dict

# {"blue": 4, "silver": 6, "orange": 6}["black"]
# {"blue", "silver", "orange"}.remove("black")


# ValueError - unsupported value provided for an operation or method or function

# age = int(input("How old are you now? "))

# int("7.9")

# float("eyfghue3jnkmf")



# ZeroDivisionError - try to divide by zero

# 6 / 0




# print(0 / 8)

# 0 / 0
# print("End of file")






# try:
#     num1 = int(input("Enter num1: "))
#     num2 = int(input("Enter num2: "))
#     result = num1 / num2
#     8[9]
# except ValueError as e:
#     print(f"num1 and num2 must be numbers: {e}")
# except ZeroDivisionError as e:
#     print(f"Cannot divide by zero: {e}")
# except Exception:
#     print("Oops! Something went wrong")
# else:
#     print(f"{num1} / {num2} = {result}")


# Ask the user for their age.
# If they enter a value that is not convertible to an integer,
# keep asking them until they do.
# If they enter a negative age, keep asking them until they enter a valid one
# If the age is valid, print their birth year.


# while True:
#     try:
#         age = int(input("How old are you now? "))
#     except ValueError as e:
#         print(f"age must be an integer")
#     else:
#         if age < 0:
#             print("Age must be positive")
#             continue
        
#         print(f"You were born in {2025 - age}")
#         break



# class InsufficientFundsError(Exception):
#     pass


# balance = 800


# def withdraw(amount):
#     global balance
#     if amount > balance:
#         raise InsufficientFundsError("Funds insufficient")
    
#     balance -= amount
#     print("Withdrawal sduccessful")



# try:
#     withdraw(300)
#     withdraw(600)
# except InsufficientFundsError as e:
#     print(e)

# while True:
#     try:
#         age = int(input("How old are you now? "))
#     except ValueError as e:
#         print(f"age must be an integer")
#     else:
#         if age < 0:
#             raise ValueError("Age must be positive")
        
#         print(f"You were born in {2025 - age}")
#         break



# 1. Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.


# class NegativeNumberError(Exception):
#     pass

# def check_positive(number):
#     if number < 0:
#         raise NegativeNumberError("number is negative")
#     return "Number is positive"


# try:
#     result = check_positive(-5)
# except NegativeNumberError as e:
#     print(e)
# else:
#     print(result)

# print(result)

# try:
#     print(check_positive(5))
# except NegativeNumberError as e:
#     print(e)




# 2. Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.


# def safe_divide(a, b):
#     try:
#         return int(a) / int(b)
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#     except ValueError:
#         return "a or b is not convertible to an integer"
#     except TypeError:
#         return "Unsupported types for division"
    

# # print(safe_divide(12, 3))
# # print(safe_divide(12, [3]))
# print(safe_divide("12", "eufneifkmce"))
# # print(safe_divide("12", [5]))


# def safe_divide(a, b):
#     try:
#         return int(a) / int(b)
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#     except ValueError:
#         return "a or b is not convertible to an integer"
#     except TypeError:
#         return "Unsupported types for division"
#     finally:
#         print("Something")


# print(safe_divide(12, 3))
# print(safe_divide("12", "eufneifkmce"))




