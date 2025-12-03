#1 Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)

# identify the first 

numbers = (input("Enter any number of your choice: ")).strip()
i = 0
total = 0
while i < len(numbers):
    char = int(numbers[i])
    total += char
    i += 1

print(total)

i = 0
total = 0
n = input("Enter any number of your choice: ")
while True:
    
    if i < len(n):
        
        total = sum(range(1, i + 1))

#2 Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7


text = input("Enter any string: ").lower()

vowels = "aeiou"

no_of_vowels = 0

no_of_consonants = 0

i = 0

while i < len(text):
    char = text[i]
     
    if char in vowels:
        no_of_vowels += 1  
    else:
        no_of_consonants += 1

    i += 1

print(f"vowels: {no_of_vowels}, consonants: {no_of_consonants}")

# for loops -----------------------------------------------
text = input("Enter any string: ").lower()

vowels = "aeiou"
no_of_vowels = 0
no_of_consonants = 0

for char in text:
    if char.isalpha(): 
        if char in vowels:
            no_of_vowels += 1
        else:
            no_of_consonants += 1

print(f"vowels: {no_of_vowels}, consonants: {no_of_consonants}")

#3 Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

numbers = int((input("Enter a single number of your choice: ")).strip())
table_limit = 12 

i = 1
total = 0
while i <= table_limit:
    result = numbers * i
    print(f"{numbers} x {i} = {result}")
    i += 1

numbers = int(input("Enter a single number of your choice: ").strip())
table_limit = 12

# for loop --------------------------------------------------------------------

for i in range(1, table_limit + 1):
    result = numbers * i
    print(f"{numbers} x {i} = {result}")


#4 Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

text = input("Enter any string of your choice: ").lower().strip()

tool = len(text) - 1
reversed_tool = []
while tool >= 0:
    char = text[tool]
    reversed_tool.append(char)
    tool -= 1

# for i in range(len(text) - 1, -1, -1):
#     reversed_tool.append(text[i])

reversed_tool = "".join(reversed_tool)
print(reversed_tool)




#5 Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

numbers = input("Enter numbers separated by commas: ").strip()
number_strings = numbers.split(",")

no_duplicate = []
i = 0

while i < len(number_strings):
    num = int(number_strings[i].strip())
    if num not in no_duplicate:
        no_duplicate.append(num)
    i += 1

print("List without duplicates:", no_duplicate)

# for loop ------------------------------------------------------------

numbers = input("Enter numbers separated by commas: ").strip()
number_strings = numbers.split(",")

no_duplicate = []

for num_str in number_strings:
    num = int(num_str.strip())
    if num not in no_duplicate:
        no_duplicate.append(num)

print("List without duplicates:", no_duplicate)


