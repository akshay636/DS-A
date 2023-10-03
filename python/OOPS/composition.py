# Define a simple class representing a Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

# Define another class representing a Library, which contains Book objects
class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list to store books

    def add_book(self, book):
        self.books.append(book)  # Add a Book object to the library

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

# Create some Book objects
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Create a Library object and add the books to it using composition
library = Library()
library.add_book(book1)
library.add_book(book2)

# List the books in the library
library.list_books()
