# Define the Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


# Define the Patron Class
class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


# Define the Library Class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add Book
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    # Register Patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron '{patron.name}' registered successfully.")

    # Borrow Book
    def borrow_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            if book.borrow():
                patron.borrow_book(book)
                print(f"{patron.name} borrowed '{book.title}'.")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid Patron ID or ISBN.")

    # Return Book
    def return_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            if book in patron.borrowed_books:
                patron.return_book(book)
                book.return_book()
                print(f"{patron.name} returned '{book.title}'.")
            else:
                print("This patron did not borrow this book.")
        else:
            print("Invalid Patron ID or ISBN.")

    # Display Information
    def display_info(self):
        print("\n------ Library Books ------")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title} | {book.author} | ISBN: {book.isbn} | {status}")

        print("\n------ Patrons ------")
        for patron in self.patrons:
            print(f"Name: {patron.name}")
            print(f"ID: {patron.patron_id}")
            if patron.borrowed_books:
                print("Borrowed Books:")
                for book in patron.borrowed_books:
                    print(f" - {book.title}")
            else:
                print("Borrowed Books: None")
            print()


# ---------------- Main Program ----------------

library = Library()

# Add Books
book1 = Book("Python Programming", "Guido van Rossum", "101")
book2 = Book("Data Structures", "Mark Allen", "102")
book3 = Book("Machine Learning", "Andrew Ng", "103")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register Patrons
patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

library.register_patron(patron1)
library.register_patron(patron2)

# Borrow Books
library.borrow_book("P001", "101")
library.borrow_book("P002", "102")

# Return Book
library.return_book("P001", "101")

# Display Information
library.display_info()