

# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------
# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]
# square = [digit * digit for digit in digits]
# print(square)
print([digit * digit for digit in digits])

# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]

print([name for name in names if "a" in name.lower()])

# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]
print([value > 10 for value in values])

# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]
print([animal[-1] for animal in animals])

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
values = [5, 12, 3, 18, 7]
print(all(value > 10 for value in values))

# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
names = ["John", "Sara", "Mike", "Amanda"]
print(any(name for name in names if "a" in name.lower()))

# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
print(all(greeting.isupper() for greeting in greetings))

# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]
print(any(word.lower().startswith("z") for word in words ))

# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
print(any(email for email in emails if ".org" in email))

# 10. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
values = [1, 3, 5, 7, 9]
print(all(value for value in values if value % 2 != 0))

# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
words = ["hi", "dog", "go", "sun"]
print(all(len(word) > 2 for word in words))

# 12. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
nums = [2, 4, 6, 8]
print([num * 3 for num in nums])

# 13. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False
temperatures = [12, 7, 3, -1, 5]
print(all(temp > 0 for temp in temperatures))

# 14. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
fruits = ["banana", "mango", "kiwi", "grape"]
print(all(fruit.endswith(("a", "i", "o", "u", "e")) for fruit in fruits))

# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
greetings = ["HELLO", "WORLD", "PYTHON"]
print([greeting.lower() for greeting in greetings])

# 16. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
numbers = [5, -2, 3, 0, 8]
print(any(num < 0 for num in numbers))

# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
items = ["sky", "tree", "rock", "stone"]
print([item for item in items if "e" in item])

# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
names = ["Alice", "Bob", "charlie", "David"]
print(all(name[0].isupper() for name in names))

# 19. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
sentences = ["Short one", "This is a much longer sentence", "Okay"]
print(any(len(sentence) > 20 for sentence in sentences))

# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------







