import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        database_folder = Path(__file__).parent

        self.database_path = database_folder / "finance.db"

        self.connection = sqlite3.connect(self.database_path)

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS transactions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT NOT NULL,

            category TEXT NOT NULL,

            type TEXT NOT NULL,

            amount REAL NOT NULL,

            notes TEXT

        )

        """)

        self.connection.commit()

    def close(self):

        self.connection.close()