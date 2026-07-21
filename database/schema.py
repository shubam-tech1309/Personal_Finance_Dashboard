TRANSACTION_TABLE = """

CREATE TABLE IF NOT EXISTS transactions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    transaction_date TEXT NOT NULL,

    category TEXT NOT NULL,

    transaction_type TEXT NOT NULL,

    amount REAL NOT NULL,

    description TEXT,

    created_at TEXT,

    updated_at TEXT

);

"""