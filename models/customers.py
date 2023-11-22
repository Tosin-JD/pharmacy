"""
Contains the customer table
"""

import sqlite3

class CustomerTable:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Customer (
            cust_ID INTEGER PRIMARY KEY,
            fname VARCHAR(255),
            lname VARCHAR(255),
            gender INTEGER,
            age INTEGER,
            contact_add INTEGER,
            cust_email VARCHAR(255),
            cust_pass VARCHAR(255)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, data):
        query = '''
        INSERT INTO Customer (fname, lname, gender, age, contact_add, cust_email, cust_pass)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, data)
        self.conn.commit()

    def update(self, cust_ID, data):
        query = '''
        UPDATE Customer
        SET fname=?, lname=?, gender=?, age=?, contact_add=?, cust_email=?, cust_pass=?
        WHERE cust_ID=?
        '''
        self.conn.execute(query, (*data, cust_ID))
        self.conn.commit()

    def delete(self, cust_ID):
        query = 'DELETE FROM Customer WHERE cust_ID=?'
        self.conn.execute(query, (cust_ID,))
        self.conn.commit()

    def select_all(self):
        query = 'SELECT * FROM Customer'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def select_by_id(self, cust_ID):
        query = 'SELECT * FROM Customer WHERE cust_ID=?'
        cursor = self.conn.execute(query, (cust_ID,))
        return cursor.fetchone()

# Example usage:
# table = CustomerTable()  # Create an instance of the CustomerTable class
# table.insert(('John', 'Doe', 1, 25, 12345, 'john.doe@example.com', 'password123'))
# customers = table.select_all()
# print(customers)
# john = table.select_by_id(1)
# print(john)
# table.update(1, ('John', 'Doe', 1, 26, 12345, 'john.doe@example.com', 'newpassword'))
# table.delete(1)
