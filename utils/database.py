from pathlib import Path
import sqlite3

from config.settings import DATABASE_DIR, DATABASE_FILE


class DatabaseManager:
    def __init__(self):
        self.database_path = DATABASE_FILE

    def initialize(self):
        """
        Creates the database folder, database file,
        and required tables if they do not exist.
        """
        DATABASE_DIR.mkdir(parents=True, exist_ok=True)

        connection = sqlite3.connect(self.database_path)

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                transaction_date TEXT NOT NULL,

                transaction_type TEXT NOT NULL,

                category TEXT NOT NULL,

                description TEXT,

                amount REAL NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()
        connection.close()

    def get_connection(self):
        return sqlite3.connect(self.database_path)