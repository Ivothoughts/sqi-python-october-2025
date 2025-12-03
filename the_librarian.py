def add_book(title, author, year, isbn, available=True):
    for book in library:
        if book["ISBN"] == isbn:
            return f"A book with ISBN {isbn} already exists."
        

    library.append({
        "Title": title,
        "Author": author,
        "Year": year,
        "ISBN": isbn,
        "Available": available
    })
    return f"Book '{title}' added successfully."


def view_books():
    if not library:
        return "No books in the library"
    else:
        for book in library:
            return book
    
def update_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            print("Enter new details (leave blank to keep current value): ")
            title = input(f"Title [{book['Title']}]: ") or book["Title"]
            author = input(f"Author [{book['Author']}]: ") or book["Author"]
            year = input(f"Year [{book['Year']}]: ")
            year = int(year) if year else book["Year"]
            available = input(f"Available [{book['Available']}]: ")
            available = (available.lower() == "true") if available else book["Available"]
            book.update({"Title": title, "Author": author, "Year": year, "Available": available})
            return"Book updated successfully" 
            
    return "Book not found."

def delete_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            library.remove(book)
            return "Book deleted successfully"
    return "Book not found"

def search_book(title):
    for book in library:
        if book["Title"].lower() == title.lower():
            print("Book found:", book)
            return
    print("Book not found.")

def borrow_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            if book["Available"]:
                book["Available"] = False
                print(f"You borrowed '{book['Title']}'.")
            else:
                print("Book is already borrowed")
            return
    print("Book not found.")

def return_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            if not book["Available"]:
                book["Available"] = True
                print(f"You returned '{book['Title']}'.")
            else:
                print("Book was not borrowed.")
        print("Book not found")

menu = """
1. add_book
2. view_books
3. update_book
4. delete_book
5. search_book
6. borrow_book
7. return_book
8. exit 

"""
library = []

while True:
    print("Welcome \n Library Menu")
    print(menu)

    choice = input("Enter your choice from 1 to 8: ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid choice.")
        continue
    
    if choice == "8":
        print("quitter la bibliothèque, Aurevoir!")
        break

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter Author: ")
        year = input("Enter Year: ")
        isbn = input("Enter ISBN: ")
        add_book(title, author, year, isbn)
    
    elif choice == "2":
        print(view_books())

    elif choice == "3":
        isbn = input("Enter ISBN of book to update: ")
        update_book(isbn)
    
    elif choice == "4":
        isbn = input("Enter ISBN of book to delete: ")
        delete_book(isbn)
        
    elif choice == "5":
        title = input("Enter title to search: ")
        search_book(title)

    elif choice == "6":
        isbn = input("Enter ISBN of book to borrow")
        borrow_book(isbn)

    elif choice == "7":
        isbn = input("Enter ISBN of book to return")
        return_book(isbn)
        
