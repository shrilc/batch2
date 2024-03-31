# Reference https://docs.python.org/3/library/sqlite3.html
import sqlite3


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        """
        Connects SQLite3 Database and creates connection and cursor to use for further execute of commands.
        :return: connection and cursor object
        """
        self.conn = sqlite3.connect(self.db_file)  # create a database file if not exists
        self.cursor = self.conn.cursor()

    def disconnet(self):
        """
        Disconnects all the process and connections from the sqllite3 database.
        :return:
        """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute(self, query, params=None):
        """
        Executes CREATE | UPDATE | DELETE operations and commits.
        :param query: valid sql query
        :param params: sql params
        :return: None
        """
        if not self.cursor:
            self.connect()
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=None):
        """
        Gets all the availabe records in the database(db) based on the query and params.
        :param query:
        :param params:
        :return: fetchall cursor.
        """
        if not self.cursor:
            self.connect()
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()



