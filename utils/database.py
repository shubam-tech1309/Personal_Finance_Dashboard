import sqlite3

from config.settings import (
    DATABASE_DIR,
    DATABASE_FILE,
)


class DatabaseManager:
    """
    Handles all SQLite database operations.

    UI files should never directly write SQL.
    They should communicate through this class.
    """

    def __init__(self):

        DATABASE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        self.initialize_database()


    def get_connection(self):

        return sqlite3.connect(
            DATABASE_FILE
        )


    def initialize_database(self):

        connection = self.get_connection()

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



    def add_transaction(
        self,
        transaction_date,
        transaction_type,
        category,
        description,
        amount,
    ):
        """
        Inserts a new transaction.
        """

        connection = self.get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO transactions
            (
                transaction_date,
                transaction_type,
                category,
                description,
                amount
            )

            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?
            )

            """,
            (
                transaction_date,
                transaction_type,
                category,
                description,
                amount,
            )
        )


        connection.commit()

        connection.close()



    def get_all_transactions(self):
        """
        Returns all transactions.
        """

        connection = self.get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT
                id,
                transaction_date,
                transaction_type,
                category,
                description,
                amount,
                created_at

            FROM transactions

            ORDER BY id DESC

            """
        )


        records = cursor.fetchall()


        connection.close()


        return records



    def delete_transaction(
        self,
        transaction_id
    ):
        """
        Deletes transaction by ID.
        """

        connection = self.get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            DELETE FROM transactions

            WHERE id = ?

            """,
            (
                transaction_id,
            )
        )


        connection.commit()

        connection.close()