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