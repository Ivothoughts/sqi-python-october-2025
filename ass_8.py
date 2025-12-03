# -------------------------------- DIVISION AND REMAINDERS --------------------------------
# Write a program that divides 15 by 4 and prints both the normal division and floor division results.
# Also print the remainder when 20 is divided by 6.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(num1 / num2)
print(num1 // num2)
print(20 % 6)


# -------------------------------- BALLS AND BOXES --------------------------------
# You have 95 apples and 8 baskets.
# Print how many apples each basket will get and how many apples will be left over.
# Example Output:
# 11
# 7

apples = 95
baskets = 8
print(apples // baskets)
print(apples % baskets)



# -------------------------------- MINUTES TO HOURS --------------------------------
# You are given 505 minutes.
# Convert it to hours and minutes.
# Example Output:
# 8 hours, 25 minutes

period = 505
hours = period // 60
minutes = period % 60
print(f"{hours} hours, {minutes} minutes")


# -------------------------------- CHECKING EVEN NUMBERS --------------------------------
# Given a number, print True if it is even, otherwise print False.
# Example Input:
# 9
# Example Output:
# False

number = 9
print( (number % 2) == 0)

# -------------------------------- MULTIPLE OF 3 --------------------------------
# Ask the user for a number.
# Print True if the number is a multiple of 3, otherwise print False.
# Example Input:
# 12
# Example Output:
# True

request = int(input("Enter a number of your choice: "))
print((request  % 3) == 0)



# -------------------------------- REMAINDER EXERCISE --------------------------------
# Ask the user for two numbers.
# Print the remainder when the first number is divided by the second.
# Example Input:
# 17
# 5
# Example Output:
# 2

remain1 = int(input("Enter a number of your choice: "))
remain2 = int(input("Enter a number of your choice: "))
print(remain1 % remain2)



# -------------------------------- HOURS AND MINUTES INPUT --------------------------------
# Ask the user to enter total minutes.
# Convert it to hours and minutes, then print the result.
# Example Input:
# 145
# Example Output:
# 2 hours, 25 minutes

total_minutes = int(input("Enter the total minute: "))
total_hours = total_minutes // 60
minutes = total_minutes % 60
print(f" {total_hours} hours, {minutes} minutes ")


# -------------------------------- OBJECT DISTRIBUTION --------------------------------
# Ask the user for total candies and number of kids.
# Print how many candies each kid gets and how many are left.
# Example Input:
# 53
# 8
# Example Output:
# Each kid gets 6 candies, 5 left over

total_candies = int(input("Enter the amount of candies you ate: "))
total_kids = int(input("Enter the amount of kids you have: "))
each_candies = total_candies // total_kids
left_over = total_candies % total_kids
print(f" Each kid gets {each_candies} candies, {left_over} left over")


# -------------------------------- MULTIPLE OF 10 --------------------------------
# Ask the user for a number.
# Print True if the number is a multiple of 10, otherwise False.
# Example Input:
# 47
# Example Output:
# False

give_me = int(input("Enter any number of your choice: "))
print((give_me % 10) == 0)
