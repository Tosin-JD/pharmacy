import sqlite3

class PurchasingTable:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Purchasing (
            purchase_ID INTEGER PRIMARY KEY,
            cust_ID INTEGER,
            med_ID INTEGER,
            amount VARCHAR(255),
            date DATE,
            FOREIGN KEY (cust_ID) REFERENCES Customer(cust_ID),
            FOREIGN KEY (med_ID) REFERENCES Medicines(med_ID)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, data):
        query = '''
        INSERT INTO Purchasing (cust_ID, med_ID, amount, date)
        VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, data)
        self.conn.commit()

    def update(self, purchase_ID, data):
        query = '''
        UPDATE Purchasing
        SET cust_ID=?, med_ID=?, amount=?, date=?
        WHERE purchase_ID=?
        '''
        self.conn.execute(query, (*data, purchase_ID))
        self.conn.commit()

    def delete(self, purchase_ID):
        query = 'DELETE FROM Purchasing WHERE purchase_ID=?'
        self.conn.execute(query, (purchase_ID,))
        self.conn.commit()

    def select_all(self):
        query = 'SELECT * FROM Purchasing'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def select_by_id(self, purchase_ID):
        query = 'SELECT * FROM Purchasing WHERE purchase_ID=?'
        cursor = self.conn.execute(query, (purchase_ID,))
        return cursor.fetchone()

# Example usage:
# table = PurchasingTable()  # Create an instance of the PurchasingTable class
# table.insert((1, 1, '5', '2023-01-01'))
# purchases = table.select_all()
# print(purchases)
# purchase_1 = table.select_by_id(1)
# print(purchase_1)
# table.update(1, (1, 1, '10', '2023-02-01'))
# table.delete(1)
