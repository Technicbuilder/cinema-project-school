import sqlite3

class Manager:
    def store_customer_record(self, phone, name, date, price, seats):
        string_seats = ', '.join(seats)
        conn = sqlite3.connect('databases/cust_record')
        cursor = conn.cursor()

        cursor.execute(""" INSERT INTO cust_record (phone_number, name, booked_seats, p_date, amount_paid)
                       VALUES (?, ?, ?, ?, ?)""", (phone, name, string_seats, date, price))

        conn.commit()
        conn.close()


    def store_management_record(self, date, revenue, seats_sold):
        conn = sqlite3.connect('databases/management_record')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO management_record (p_date, revenue, seats_sold)
            VALUES (?, 0, 0)""", (date,)
            )

        cursor.execute("""
            UPDATE management_record
            SET revenue = revenue + ?,
            seats_sold = seats_sold + ?
            WHERE p_date = ?""", (revenue, seats_sold, date)
            )

        conn.commit()
        conn.close()

if __name__ == '__main__':
    data_manager = Manager()
