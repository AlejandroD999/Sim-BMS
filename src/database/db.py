import sqlite3
import os

CURR_DIR = os.getcwd()
DB_PATH = os.path.join(CURR_DIR, "accounts.db")

def create_accounts_table():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        acc_table_query = """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            account_number TEXT NOT NULL UNIQUE,
            balance INTEGER NOT NULL
            )
            """

        cur.execute(acc_table_query)

def pull_accounts():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute("SELECT account_number FROM accounts")

        accounts = cur.fetchall()

    return accounts

if __name__ == "__main__":
    create_accounts_table()

    print(pull_accounts())