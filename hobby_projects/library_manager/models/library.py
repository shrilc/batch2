from .book import BookDB
from ..database.database import Database


class Library:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT NOT NULL
            )
        """)

    def add_book(self, book):
        query = "INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)"
        params = (book.title, book.author, book.isbn)
        self.db.execute(query, params)

    def remove_book(self, book_id):
        query = "DELETE FROM books WHERE id = ?"
        params = (book_id,)
        self.db.execute(query, params)

    def get_all_books(self):
        query = "SELECT id, title, author, isbn from books"
        rows = self.db.fetchall(query) # (id=2, title=str, author=str, isbn=str)
        output_d = []
        for row in rows:
            to_dict = {
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'isbn': row[3]
            }
            output_d.append(to_dict)

        return output_d

    def search_books(self, query):
        query = f"SELECT id, title, author, isbn FROM books WHERE title LIKE '%{query}%' OR author LIKE '%{query}%' OR isbn LIKE '%{query}%'"
        rows = self.db.fetchall(query)
        return [BookDB(*row) for row in rows]