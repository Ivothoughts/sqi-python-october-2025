# Scenario:
# You are working as a data analyst for a marketing company. You have been given a large text document containing customer reviews and feedback. Your task is to extract all email addresses and phone numbers from this document for further analysis.

# Task:
# Write a Python script named `data_analyst.py` that:
# Reads the contents of a text file named reviews.txt.
# Extracts all email addresses and phone numbers from the text.
# Email addresses follow the standard format: username@domain.tld
# Phone numbers are in the format: +234 803 456 7890
# Writes the extracted email addresses to a file named emails.txt and the phone numbers to a file named phone_numbers.txt.

# Requirements:
# Use regular expressions to find the email addresses and phone numbers.
# Ensure that the extracted data is saved in separate files, one for emails and one for phone numbers.

# Example:
# Given the following content in reviews.txt:

# Customer feedback:
# - Email: john.doe@example.com
# - Phone: +234 803 456 7890
# - Another contact: jane_smith@workplace.org
# - Alternate phone: +234 701 234 5678

# The script should produce:
# emails.txt containing:
# john.doe@example.com
# jane_smith@workplace.org
# phone_numbers.txt containing:
# +234 803 456 7890
# +234 701 234 5678

# 	Go here and download the `reviews.txt` file to use.

import re

def extract_data():
    
    with open("reviews.txt", "r", encoding="utf-8") as file:
        text = file.read()

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\+234\s\d{3}\s\d{3}\s\d{4}"

    emails = re.findall(email_pattern, text)
    phone_numbers = re.findall(phone_pattern, text)

    with open("emails.txt", "w", encoding="utf-8") as email_file:
        for email in emails:
            email_file.write(email + "\n")

    
    with open("phone_numbers.txt", "w", encoding="utf-8") as phone_file:
        for phone in phone_numbers:
            phone_file.write(phone + "\n")

    print("✅ Extraction complete! Check emails.txt and phone_numbers.txt.")


extract_data()