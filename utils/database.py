import sqlite3

from config.settings import (
    DATABASE_DIR,
    DATABASE_FILE,
)


class DatabaseManager:
    """
    Handles all SQLite operations.
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
        date,
        transaction_type,
        category,
        description,
        amount,
    ):

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
                date,
                transaction_type,
                category,
                description,
                amount,
            )
        )


        connection.commit()

        connection.close()



    def get_all_transactions(self):

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


        data = cursor.fetchall()


        connection.close()


        return data



    def delete_transaction(
        self,
        transaction_id
    ):
        """
        Deletes transaction permanently.
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



    def get_statistics(self):

        connection = self.get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT

            transaction_type,
            SUM(amount)

            FROM transactions

            GROUP BY transaction_type

            """
        )


        rows = cursor.fetchall()


        income = 0

        expense = 0


        for row in rows:


            if row[0] == "Income":

                income = row[1] or 0


            elif row[0] == "Expense":

                expense = row[1] or 0



        balance = income - expense


        connection.close()


        return {

            "income": income,

            "expense": expense,

            "balance": balance,

            "savings": balance

        }