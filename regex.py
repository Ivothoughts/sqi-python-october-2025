

# 1. Create a folder - `mkdir folder_name`
# 2. Enter into the folder - `cd folder_name`
# 3. Create a virtual env - `python -m venv .venv` or `python3 -m venv .venv`
# 4. Activate the virtual env - `source .venv/bin/activate` or `.venv\Scripts\activate`
# 5. Install your dependencies e.g. bs4, requests using `pip install bs4 requests`
# 6. Scrape any site of your choice.


# """
# Solution to the Email Validator problem.
# Find the problem at:
# https://docs.google.com/presentation/d/1JqpvPnQp3FXbu6zVUkNuYjKlmfZi52HEbXAAUujiyfU/edit#slide=id.g2e38e92a40d_0_1276
# """

# import string

# def email_is_valid(email):
#     # The email address must contain exactly one "@" symbol.
#     if email.count("@") != 1:
#         return False
    
#     # The local part (before the "@") must:
#     # Include only letters (A-Z, a-z), digits (0-9), and the following special characters: ! # $ % & ' * + - / = ? ^ _ ` { | } ~
#     local_part, domain_part = email.split("@")

#     local_part_allowed_chars = list(string.ascii_letters) + [".", "!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~", '"']

#     # OR
#     # allowed = all(char in allowed_chars for char in local_part)
#     # if not allowed:
#     #     return False

    
#     for char in local_part:
#         if char not in local_part_allowed_chars:
#             return False
        
#     # Allow periods (.) but not at the start or end, and not consecutively.
#     # Be no more than 64 characters long.
#     fragments = local_part.split(".")
#     for fragment in fragments:
#         if not fragment:
#             return False
        
#     if len(local_part) > 64:
#         return False
    
#     # The domain part (after the "@") must:
#     # Include only letters (A-Z, a-z), digits (0-9), and hyphens (-).
#     domain_part_allowed_chars = list(string.ascii_letters) + list(string.digits) + ['-', '.']
     
#     for char in domain_part:
#         if char not in domain_part_allowed_chars:
#             return False



#     # Include the domain name and top-level domain.

#     labels = domain_part.split(".")

#     if len(labels) < 2:
#         return False

#     # Include periods (.) to separate the domain labels i.e. subdomains if any, domain name and TLD, 
#     # but not at the start or end of the domain part, and not consecutively.
#     fragments = domain_part.split(".")
#     for fragment in fragments:
#         if not fragment:
#             return False

#     # Hyphens can be placed anywhere except at the beginning or end of the domain part and cannot be used consecutively
#     # (i.e., you cannot have "--" within the domain part). 

#     fragments = domain_part.split("-")
#     for fragment in fragments:
#         if not fragment:
#             return False


#     # OR
#     # does_not_contain_consecutive_hyphens = all(bool(fragment) for fragment in domain_part.split("-"))
#     # if not does_not_contain_consecutive_hyphens:
#     #     return False

#     # Labels must not start or end with a hyphen.
#     # Each domain label is no more than 63 characters long
#     MAX_DOMAIN_LABEL_LEN = 63
#     for label in labels:
#         if len(label) > MAX_DOMAIN_LABEL_LEN:
#             return False
        
#     # Be no more than 253 characters long.
#     if len(domain_part) > 253:
#         return False


#     # The tld part must be at least two characters, for example: .com, .org, .cc. 
#     # It can contain numbers but must not be purely numerical.

#     tld = labels[-1]
#     if len(tld) < 2 or tld.isdigit():
#         return False


#     # The entire email address must be no more than 254 characters long.

#     MAX_EMAIL_LENGTH = 254
#     if len(email) > MAX_EMAIL_LENGTH:
#         return False
        
#     return True


import re

# search_text = input("Enter the text you are searching for: ")

# # Example 1: Simple match
# pattern = rf"\b{search_text}\b"
# text = "A word in a sentence in a paragraph."
# match = re.search(pattern, text)
# if match is not None:
#     print(match)
#     print("Match found:", match.group())
# else:
#     print("No match found")


# import re

# search_text = input("Enter the text you are searching for: ")

# # Example 1: Simple match
# pattern = rf"\b{search_text}\b"
# text = "A word in a sentence in a paragraph."
# matches = re.findall(pattern, text)
# print(matches)


# Example 2: Find all occurrences
# pattern = r"\d+"
# text = "There are 123 apples and 456 oranges."
# match = re.search(pattern, text)
# print("Numbers found:", match) 

# print(match)

# if match is not None:
#     print(match.group())
# else:
#     print('no match found')
# pattern = r"\d+"

# pattern = r"\b\d+\b"
# text = "There are 123 apples and 456 oranges."
# matches = re.findall(pattern, text)
# print("Numbers found:", matches) 




# Example 3: Replace text
# pattern = r"\s+"
# text = "This   is \ta       \ntest."
# print(text)
# new_text = re.sub(pattern, "", text)
# print("Replaced text:", new_text)  # Replaced text: This is a test.

# print("\thello")



# import re
# # Example 1: Match an email address
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}"
# text = "Contact us at hello@example.c80 for more info."
# match = re.search(pattern, text)
# if match:
#     print("Email found:", match.group())  # Email found: support@example.com


# Extracting Data

# import re
# # Example 2: Extract dates in YYYY-MM-DD format
# pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']


# import re
# # Example 2: Extract dates in YYYY-MM-DD format
# pattern = r"^\b\d{4}-\d{2}-\d{2}\b$"
# while True:
#     date = input("Enter a valid date: ").strip()
#     match = re.match(pattern, date)

#     if match is None:
#         print("Invalid or no date entered. Date must be provided and follow YYYY-MM-DD format.")
#         continue


#     import datetime
#     try:
#         date = datetime.datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         print("invalid date")
#         continue

#     print("Correct date entered")
#     break



# Validating Input

import re
# Example 3: Validate a phone number (US format)
pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
phone_number = "(123) 456-7890"
if re.match(pattern, phone_number):
    print("Valid phone number")  # Valid phone number
else:
    print("Invalid phone number")
