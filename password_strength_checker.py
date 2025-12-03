# --------------------------PASSWORD CHECKER-------------------------------------------------------------
# Scenario: You need to check if a user's password is strong enough.

# Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# DO NOT USE REGEX.

password = "De11Heweltp@kard"
special = "!@#$%^&*()"
char_len = len(password) >= 8
has_upper = any(pw.isupper() for pw in password)
has_lower = any(pw.islower() for pw in password)
has_digit = any(pw.isdigit() for pw in password )
special_char = any(pw in special for pw in password)
print(char_len and has_upper and has_lower and has_digit and special_char)