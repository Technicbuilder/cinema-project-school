import sqlite3
import os

#   This file will create the customer_record database
#   I will create a 'Manager class' to help store data, this file just creates the tables
#   Accounts comes pre installed with 2 accounts admin, staff (admin is used to block seats
#   that require blocking in case if performers wish to emerge from the crowd)


def customer_record_database():
    connection = sqlite3.connect('databases/cust_record')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cust_record (
                   phone_number TEXT PRIMARY KEY NOT NULL,
                   name TEXT,
                   booked_seats TEXT,
                   p_date TEXT,
                   amount_paid REAL
                   )

                    """)

    connection.commit()
    cursor.close()
    
def management_database():
    connection = sqlite3.connect('databases/management_record')
    cursor = connection.cursor()

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS management_record (
        p_date TEXT PRIMARY KEY,
        revenue REAL,
        seats_sold INTEGER
    )
                   """)

    connection.commit()
    cursor.close()

def user_accounts():
    connection = sqlite3.connect('databases/accounts_record')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts_record (
                   id INTEGER PRIMARY KEY,
                   username TEXT,
                   password TEXT 
                   )

                    """)

    account_data = [('admin', 'admin123'), ('staff', 'staff123')]
    cursor.executemany('INSERT OR IGNORE INTO accounts_record (username, password) VALUES (?, ?)', account_data)
    connection.commit()
    cursor.close()

if __name__ == '__main__':
    os.makedirs('databases', exist_ok=True)
    customer_record_database()
    management_database()
    user_accounts()