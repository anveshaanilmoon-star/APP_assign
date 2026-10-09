class book:
    def __init__(self,title,author,isbn,is_borrowed=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.borrowed= is_borrowed

    def borrow_book(self):
        if  not self.borrowed:
            print(f"The book {self.title} with book number {self.isbn} by author {self.author} cannot be borrowed.")
        else:
            self.borrowed==False
            print(f"The book {self.title} with book number {self.isbn} by author {self.author} is borrowed.")

    def return_book(self):
        if not self.borrowed:
            print(f"The book {self.title} with book number {self.isbn} by author {self.author} has not been returned. ")

        else:
            self.borrowed==True
            print(f"The book {self.title} with book number {self.isbn} has been returned.")
        
class patron:
    def __init__(self,name,patron,borrowed_books=True):        
        self.name=name
        self.patron=patron
        self.borrowed=borrowed_books

    def borrow_book(self):
        if not self.borrowed:
            print(f"The patron {self.name} with patron ID {self.patron} has not borrowed a book.")            
        else:
            self.borrowed==True
            print(f"The patron {self.name} with patron ID {self.patron} has borrowed a book.")

    def return_book(self):
        if not self.borrowed:
            print(f"The patron {self.name} with patron ID {self.patron} has not returned the book.")  
        else:
            self.borrowed=True
            print(f"The patron {self.name} with patron ID {self.patron} has returned the book.")
            
class Library:
    def __init__(self,patrons,books):
        self.books=books
        self.patrons=patrons

    def add_book(self):
        print(f"The book {self.books} has been added.")
    
    def register_patron(self):
        print(f"The person named {self.patrons} has been registered.")
    
    def borrow_books(self):
        print(f"The book {self.books} has been borrowed.")
    
    def return_book(self):
        print(f"The book {self.books} has been returned.")
           
obj1=book("Harry Potter","J.K Rowlling",978-0-7432-4626-8)
obj1.borrow_book()
obj1.return_book()
obj2=patron("Rahul","U00012345")
obj2.borrow_book()
obj2.return_book()         
obj3=Library("U00012345","Harry Potter")
obj3.add_book()
obj3.register_patron()
obj3.borrow_books()
obj3.return_book()