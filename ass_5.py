# -------------------------------- .LOWER() --------------------------------
# 1. Create a word in uppercase and print it in lowercase.
# Example:
# word = "ELEPHANT"
# Expected output:
# elephant
word = "ELEPHANT"
print(word.lower())



# -------------------------------- .CAPITALIZE() --------------------------------
# 2. Create a sentence in any case and print it with only the first letter capitalized.
# Example:
# sentence = "hELLO from school"
# Expected output:
# Hello from school
sentence = "hELLO from school"
print(sentence.capitalize())


# -------------------------------- .TITLE() --------------------------------
# 3. Create a phrase with spaces, hyphens, or underscores and print it in title case.
# Example:
# phrase = "fresh-juice_day"
# phrase = phrase.replace("-", " ").replace("_", " ")
# Expected output:
# Fresh Juice Day
phrase = "fresh-juice_day"
phrase = phrase.replace("-", " ").replace("_", " ")
print(phrase.title())


# -------------------------------- .COUNT() --------------------------------
# 4. Create a text and print how many times "banana" appears.
# Example:
# text = "banana banana banana"
# Expected output:
# 3
text = "banana banana banana"
print(text.count("banana"))


# -------------------------------- .STARTSWITH() AND .ENDSWITH() --------------------------------
# 5. Create a string and print True if it starts with a specific prefix "super", else False.
# Example:
# text = "superhero"
# Expected output:
# True
text = "superhero"
print(text.startswith("super"))

# 6. Create another string and print True if it ends with a specific suffix ".txt", else False.
# Example:
# text = "notes.txt"
# Expected output:
# True
text = "notes.txt"
print(text.endswith(".txt"))


# -------------------------------- COMBINED TASK --------------------------------
# 7. Create a filename and print True if it ends with ".jpg", ".png", or ".gif" (case-insensitive).
# Example:
# filename = "holiday.PnG"
# Expected output:
# True
filename = "holiday.PnG"
filename_lower = filename.lower()
print(filename_lower.endswith((".jpg", ".png", ".gif")))


# -------------------------------- EXTRA TASK --------------------------------
# 8. Create a short message in uppercase and print it in lowercase, capitalized, and title case — one per line.
# Example:
# message = "WELCOME TO THE EVENT"
# Expected output:
# welcome to the event
# Welcome to the event
# Welcome To The Event
message = "WELCOME TO THE EVENT"
print(message.lower())
print(message.capitalize())
print(message.title())

