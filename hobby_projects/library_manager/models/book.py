from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    @abstractmethod
    def to_dict(self):
        pass


class BookDB(Book):
    def __init__(self, title, author, isbn, id_=None):
        super().__init__(title, author, isbn)
        self.id = id_

    def to_dict(self):
        """
        :return: a dictionary of book data
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }
