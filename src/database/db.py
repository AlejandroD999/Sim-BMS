import sqlite3
import os

curr_dir = os.getcwd()
with sqlite3.connect(os.path.join(curr_dir, "accounts.db")) as conn:
    cur = conn.cursor()

    acc_table_query = """
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        account_number TEXT NOT NULL UNIQUE,
        balance INTEGER NOT NULL
        )
        """
    
    cur.execute(acc_table_query)
