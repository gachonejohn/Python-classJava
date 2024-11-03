#library management system

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def display_info(self):
        print(f"Book title: {self.title}, Author: {self.author}, year {self.year}")

#child/derived/subclass
class LibraryBook(Book):
    def __init__(self, title, author, year,isbn,copies_available):
        super().__init__(title,author,year)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -=1
            return f"{self.title} borrowed. copies left: {self.copies_available}"
        else:
            return f"No of copies {self.title} Available"

    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned. copies left: {self.copies_available}"
book1 = LibraryBook("Atomic habits", "James clear", 1999,9,5)

# print(book1.display_info())
print(book1.borrow_book())
print(book1.borrow_book())
print(book1.borrow_book())
print(book1.borrow_book())
print(book1.borrow_book())
print(book1.borrow_book())
print(book1.return_book())
print(book1.return_book())
print(book1.return_book())

