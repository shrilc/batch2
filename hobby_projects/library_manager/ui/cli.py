from batch2.hobby_projects.library_manager.models.book import BookDB
from batch2.hobby_projects.library_manager.models.library import Library
from batch2.hobby_projects.library_manager.utils.exceptions import QuitException


class CLI:
    def __init__(self, db_file):
        self.library = Library(db_file)

    def run(self):
        try:
            while True:
                print("\nPersonal Library Manager")
                print("1. Add a book")
                print("2. Remove a book")
                print("3. View all books")
                print("4. Search for a book")
                print("5. Quit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    self.add_book()
                elif choice == "2":
                    self.remove_book()
                elif choice == "3":
                    self.view_all_books()
                elif choice == "4":
                    self.search_books()
                elif choice == "5":
                    raise QuitException
                else:
                    print("Invalid choice. Please try again")
        except QuitException:
            print("\n Thank you for using Personal Library Manager!")

    def add_book(self):
        print("\n Add a Book")
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        book = BookDB(title, author, isbn)
        self.library.add_book(book)
        print("\nBook added successfully!")

    def remove_book(self):
        print("\nRemove a Book")
        book_id = input("Enter the Id of the book you want to remove: ")
        self.library.remove_book(book_id)
        print("\nBook removed successfully")

    def view_all_books(self):
        print("\n All Books")
        books = self.library.get_all_books()
        if books:
            for book in books:
                print(f"ID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"ISBN: {book['isbn']}")
                print("")
        else:
            print("No books found.")

    def search_books(self):
        pass




