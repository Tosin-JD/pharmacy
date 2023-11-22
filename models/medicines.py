import sqlite3

class MedicinesTable:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Medicines (
            med_ID INTEGER PRIMARY KEY,
            med_category VARCHAR(30),
            name VARCHAR(30),
            description VARCHAR(30),
            price VARCHAR(30)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, data):
        query = '''
        INSERT INTO Medicines (med_category, name, description, price)
        VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, data)
        self.conn.commit()

    def update(self, med_ID, data):
        query = '''
        UPDATE Medicines
        SET med_category=?, name=?, description=?, price=?
        WHERE med_ID=?
        '''
        self.conn.execute(query, (*data, med_ID))
        self.conn.commit()

    def delete(self, med_ID):
        query = 'DELETE FROM Medicines WHERE med_ID=?'
        self.conn.execute(query, (med_ID,))
        self.conn.commit()

    def select_all(self):
        query = 'SELECT * FROM Medicines'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def select_by_id(self, med_ID):
        query = 'SELECT * FROM Medicines WHERE med_ID=?'
        cursor = self.conn.execute(query, (med_ID,))
        return cursor.fetchone()

# Example usage:
# table = MedicinesTable()  # Create an instance of the MedicinesTable class
# table.insert(('Category A', 'Medicine A', 'Description A', '50.00'))
# medicines = table.select_all()
# print(medicines)
# medicine_a = table.select_by_id(1)
# print(medicine_a)
# table.update(1, ('Category A', 'Medicine A', 'Updated Description', '60.00'))
# table.delete(1)
