import sqlite3
from pathlib import Path
import os

FILE_DIR = Path(__file__).resolve()

DB_PATH = os.path.join(FILE_DIR.parent, "accounts.db")

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

def create_account(acc_number, initial_balance):

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute("INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (acc_number, initial_balance))


def pull_account_nums():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute("SELECT account_number FROM accounts")

        accounts = cur.fetchall()

    return [x[0] for x in accounts]

# TODO Make function to pull full account number
# THEN update pull_acount_details to use the account_number

def pull_account_details(last_digits):
    # Uses acc_number to fetch data and returns class 'Account'
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute("SELECT account_number, balance FROM accounts WHERE account_number LIKE ?", (f"%{last_digits}",))

        acc = cur.fetchone()

    return acc

def update_balance(acc_number, new_balance):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, acc_number))

