# 17.	Convert a string “James John Kennedy” called “names” to a list using the string 
# .split() method. Store the result in a list called “names_list”

names = "James John Kennedy"
print(names.split(" "))
print(names.split())

# 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.

cities = ['New York', 'Los Angeles', 'Chicago']
cities_string = "; ".join(cities)
# print(": ".join(cities))

print(cities_string)

# 19.	Create a string variable sentence with the value "the quick brown fox jumps over the 
# lazy dog". Capitalize the first letter of the string and 
# print the result.

sentence = "the quick brown fox jumps over the lazy dog"
print(sentence.capitalize())

# 20. 	Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# the first letter of each word and print the result.

book_title = "to kill a mockingbird"
print(book_title.title())

# 21. 	Create a string variable text with the value "hello world". Count the number of 
# occurrences of the letter 'o' and print the result.

text = "hello world"
print(text.count("o"))

# 22. 	Create a string variable filename with the value "document.txt". Check if the string 
# starts with "doc" and print the result.

filename = "document.txt"
print(filename.startswith("doc"))

# 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# string ends with ".com" and print the result.

url = "https://www.example.com"
print(url.endswith(".com"))

# 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# the position of the word "needle" and print the result.

phrase = "find the needle in the haystack"
print(phrase.find("needle"))

# 25.	Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.

template = "Hello, {}. Welcome to {}"
print(template.format("Alice","wonderland"))

# 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# of the word "not" and print the result.

quote = "To be or not to be"
print(quote.find("not"))

# 27.	Create a string variable word with the value "hello". Check if all characters in the 
# string are lowercase and print the result.

word = "hello"
print(word.islower())

# 28.	Create a string variable shout with the value "HELLO". Check if all characters in the 
# string are uppercase and print the result.

word = "HELLO"
print(word.isupper())

# 29.	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# lowercase and print the result.

mixed_case = "PyThOn"
print(mixed_case.lower())

# 30. 	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# uppercase and print the result.

mixed_case = "PyThOn"
print(mixed_case.upper())

# 31. 	Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# print the result.

padded_text = " hello "
print(padded_text.lstrip())

# 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# print the result.

padded_text = " hello "
print(padded_text.rstrip())

# 33.	Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# whitespace and print the result.

padded_text = " hello "
print(padded_text.strip())

# 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.

greeting = "Hello, World!"
print(greeting.replace("World", "Alice"))

# REPL - Read EValuate Print Loop 