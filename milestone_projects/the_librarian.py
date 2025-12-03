library: list[dict[str, str | int | bool]] = [
    {"title": "1984", "author": "George Orwell", "year": 1949, "isbn": "0451524934", "available": True},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "isbn": "0061120081", "available": True},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "isbn": "0743273567", "available": True},
]


def add_book():
    title = input("Enter the title of the book you wish to add: ").strip()
    author = input("Enter the author of the book: ").strip()
    year = input("Enter the publication year of the book: ").strip()
    isbn = input("Enter the ISBN number of the book: ").strip()

    library.append({"title": title, "author": author, "year": year, "isbn": isbn, "available": True})

    print("Book added to the library successfully")


def view_books():

    if not library:
        print("No books in the library right now, check back later")
        return
    
    for idx, book in enumerate(library, start=1):
        print(f"""
Book {idx}
Title: {book["title"]}
Author: {book["author"]}
Year of Publication: {book["year"]}
ISBN: {book["isbn"]}
Available: {'Yes' if book["available"] else 'No'}
""")

def update_book(isbn):
    for book in library:
        if isbn == book["isbn"]:
            book["title"] = input(f"Enter the title of the book you wish to add or leave blank to use '{book["title"]}': ").strip() or book["title"]
            book["author"] = input(f"Enter the author of the book or leave blank to use '{book["author"]}': ").strip() or book["author"]
            book["year"] = input(f"Enter the publication year of the book or leave blank to use '{book["year"]}': ").strip() or book["year"]
            book["isbn"] = input(f"Enter the ISBN number of the book or leave blank to use '{book["isbn"]}': ").strip() or book["isbn"]
            print("Book updated successfully")
            return
        
    print(f"Book with that ISBN {isbn} does not exist")
        

def delete_book(isbn):
    for book in library:
        if isbn == book["isbn"]:
            library.remove(book)
            print("Book deleted successfully")
            return
        
    print(f"Book with that ISBN {isbn} does not exist")


def search_book(isbn):
    for book in library:
        if isbn == book["isbn"]:
            print(f"""
Title: {book["title"]}
Author: {book["author"]}
Year of Publication: {book["year"]}
ISBN: {book["isbn"]}
Available: {'Yes' if book["available"] else 'No'}
""")
            return
        
    print(f"Book with that ISBN {isbn} does not exist")



# def process_borrow_or_return(isbn, borrow: bool):
#     for book in library:
#         if isbn == book["isbn"]:

#             availability = not borrow

#             if not availability:
#                 if not book["available"]:
#                     print("Book has already been borrowed. Check back later")
#                     return
                
#                 book["available"] = False
#                 print("Book successfully borrowed")
#                 return
#             else:
            

#             book["available"] = False
#             return

def borrow_book(isbn):
    for book in library:
        if isbn == book["isbn"]:
            if not book["available"]:
                print("Book has already been borrowed. Check back later")
                return

            book["available"] = False
            print("Book successfully borrowed")
            return

    print(f"Book with that ISBN {isbn} does not exist")


def return_book(isbn):
    for book in library:
        if isbn == book["isbn"]:
            if book["available"]:
                print("Book is already available.")
                return

            book["available"] = True
            print("Book successfully returned")
            return

    print(f"Book with that ISBN {isbn} does not exist")


menu = """
AB. Add Book
VB. View Book
UB. Update Book
DB. Delete Book
SB. Search Book
BB. Borrow Book
RB. Return Book
EX. Exit
"""
while True:
    print(menu)

    choice = input("Choose an option from the menu above: ").strip().lower()

    if choice == "ab":
        add_book()
    elif choice == "vb":
        view_books()
    elif choice == "ub":
        isbn = input("Enter the ISBN of the book you wish to update: ").strip()
        update_book(isbn)
    elif choice == "db":
        isbn = input("Enter the ISBN of the book you wish to delete: ").strip()
        delete_book(isbn)
    elif choice == "sb":
        isbn = input("Enter the ISBN of the book you are searching for: ").strip()
        search_book(isbn)
    elif choice == "bb":
        isbn = input("Enter the ISBN of the book you wish to borrow: ").strip()
        borrow_book(isbn)
    elif choice == "rb":
        isbn = input("Enter the ISBN of the book you wish to return: ").strip()
        return_book(isbn)
    elif choice == "ee":
        print("Bye bye 👋")
        break
    else:
        print("Invalid choice")

    
    

    