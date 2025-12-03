# Project Overview:
# Create a simple phone book manager where users can add, view, update, and delete contacts
# in a file named `phone_book.py`.

# Requirements:
# Data Storage: Use a list of dictionaries to store contact information. Each contact should have the following attributes:
# Name (string)
# Phone Number (string)
# Favorite (boolean)
# Functions/Actions:
# add_contact(): Add a new contact to the phone book.
# view_contacts(): Display all the contacts in the phone book.
# update_contact(phone_number): Update the information of a contact given their phone number.
# delete_contact(phone_number): Remove a contact from the phone book using their phone
# number.
# search_contact(name): Search for a contact by their exact name.
# mark_favorite(phone_number): Mark a contact as a favorite.
# unmark_favorite(phone_number): Unmark a contact as a favorite.
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.

def add_contact(name, phone_number,favourite=True):
    for contact in contacts:
        if contact["phone_number"] == phone_number:
            return f"Contact with the phone number {phone_number} already exists. "
        
    contacts.append({
        "Name": name,
        "Phone_number": phone_number,
        "Favourite": favourite
    })
    return f"contacts {name} added successfully"

def view_contacts():
    if not contacts:
        return "No contacts in Phone Book"
    else:
        for contact in contacts:
            fav_status = "★" if contact["Favourite"] else ""
            print(f"Name: {contact['Name']}, phone: {contact['Phone_number']} {fav_status}")

def update_contact(phone_number):
    for contact in contacts:
        if contact["Phone_number"] == phone_number:
            print("Enter new details (leave blank to keep current value):")
            name = input(f"Name [{contact['Name']}]: ") or contact["Name"]
            fav_input = input(f"Favorite (yes/no) [{contact['Favorite']}]: ")
            favourite = contact["Favorite"] if not fav_input else (fav_input.lower() == "yes")
            contact.update({"Name": name, "Favorite": favourite})
            return "Contact updated successfully."
    return "Contact not found."

def delete_contact(phone_number):
    for contact in contacts:
        if contact["Phone_number"] == phone_number:
            contacts.remove(contact)
            return "Contact deleted successfully."
    return "Contact not found."

def search_contact(name):
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            return contact
    return "Contact not found."

def mark_favourite(phone_number):
    for contact in contacts:
        if contact["Phone_number"] == phone_number:
            contact["Favourite"] = True
            return f"{contact['Name']} marked as favourite."
    return "Contact not found."

def unmark_favourite(phone_number):
    for contact in contacts:
        if contact["Phone_number"] == phone_number:
            contact["Favourite"] = False
            return f"{contact['Name']} unmarked as favourite."
    return "Contact not found."




contacts = []

menu = """
Phone Book Menu:
1. Add Contact
2. View Contacts
3. Update Contact
4. Delete Contact
5. Search Contact
6. Mark Favorite
7. Unmark Favorite
8. Exit
"""

while True:
    print(menu)
    choice = input("Enter your choice (1-8): ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid choice.")
        continue

    if choice == "8":
        print("Exiting Phone Book. Goodbye!")
        break

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        print(add_contact(name, phone))
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        phone = input("Enter Phone Number to update: ")
        print(update_contact(phone))
    elif choice == "4":
        phone = input("Enter Phone Number to delete: ")
        print(delete_contact(phone))
    elif choice == "5":
        name = input("Enter Name to search: ")
        print(search_contact(name))
    elif choice == "6":
        phone = input("Enter Phone Number to mark favourite: ")
        print(mark_favourite(phone))
    elif choice == "7":
        phone = input("Enter Phone Number to unmark favourite: ")
        print(unmark_favourite(phone))