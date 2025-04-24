class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0 
        print("----WelCome to the library-----")
        print("\n This book added recently 👇")
                
                
    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f"✅ {book_name} added to the library")
        
        
    def available_books(self, old_collection_book):
        self.collections = old_collection_book
        self.no_of_books += 1
        return self.collections
        
        
    def display_all_book(self):
        print("\n📚 Books Available in the library")
        print(f"{self.collections}")
        if self.no_of_books == 0:
            print("No Books Available in the library")
        else:
            for book in self.books:
                print(f"{book}")
                                
    
    def issue_book(self, issue_book):
        self.issue_book_name = issue_book
        print(f"\n{issue_book} was issued")
        self.no_of_books -= 1
        
        
    def number_of_books(self):
        return self.no_of_books
    
library = Library()

library.add_book("Ramayana Part-2")
library.add_book("Bhagvad Gita")


library.available_books("Ramayan Part-1")
library.available_books("Mahabharat Part-1")
library.available_books("Mahabharat Part-2")

library.display_all_book()

library.issue_book("Ramayana Part-2")

print(f"\n📈 Total Available books = {library.number_of_books()}")


# # 📚 Simple Library Management System in Python

# A beginner-friendly Python program that demonstrates how to manage books in a library using **Object-Oriented Programming (OOP)**. The program uses a custom `Library` class with features like adding books, displaying all books, and showing the total number of books.

# ---

# ## 🧱 Class Structure

# ### `Library` class has:
# - `books`: a list to store book names
# - `no_of_books`: a counter to keep track of the number of books

# ### Methods:
# - `add_book(book_name)`: Adds a new book to the library
# - `display_books()`: Prints all books in the library
# - `get_number_of_books()`: Returns the total number of books

# ---

# ## 🛠️ How to Run

# 1. Make sure you have Python installed on your computer.
# 2. Save the file as `library_management.py`.
# 3. Open terminal or command prompt and run:


# 🚀 Example Output
# ✅ 'Python Programming' added to the library.
# ✅ 'Data Structures and Algorithms' added to the library.
# ✅ 'Introduction to AI' added to the library.

# 📚 Books available in the library:
# 1. Python Programming
# 2. Data Structures and Algorithms
# 3. Introduction to AI

# 📈 Total number of books: 3

# 🧠 Concepts Used
# Object-Oriented Programming (OOP)
# Class and Object
# Instance Variables and Methods
# List operations
# Basic input/output in Python

# ✅ Features To Add (Ideas)
# Menu-driven interface
# Remove a book
# Search a book
# File-based saving and loading of books

# 👨‍💻 Author
# Made for learning and practice with ❤️ in Python