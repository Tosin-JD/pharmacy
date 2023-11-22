import sqlite3

class SalesTable:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Sales (
            sales_ID INTEGER PRIMARY KEY,
            phar_ID INTEGER,
            cust_ID INTEGER,
            med_ID INTEGER,
            count INTEGER,
            purchase_ID INTEGER,
            date DATE,
            total_amount VARCHAR(255),
            FOREIGN KEY (phar_ID) REFERENCES Pharmacist(phar_ID),
            FOREIGN KEY (cust_ID) REFERENCES Customer(cust_ID),
            FOREIGN KEY (med_ID) REFERENCES Medicines(med_ID),
            FOREIGN KEY (purchase_ID) REFERENCES Purchasing(purchase_ID)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, data):
        query = '''
        INSERT INTO Sales (phar_ID, cust_ID, med_ID, count, purchase_ID, date, total_amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, data)
        self.conn.commit()

    def update(self, sales_ID, data):
        query = '''
        UPDATE Sales
        SET phar_ID=?, cust_ID=?, med_ID=?, count=?, purchase_ID=?, date=?, total_amount=?
        WHERE sales_ID=?
        '''
        self.conn.execute(query, (*data, sales_ID))
        self.conn.commit()

    def delete(self, sales_ID):
        query = 'DELETE FROM Sales WHERE sales_ID=?'
        self.conn.execute(query, (sales_ID,))
        self.conn.commit()

    def select_all(self):
        query = 'SELECT * FROM Sales'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def select_by_id(self, sales_ID):
        query = 'SELECT * FROM Sales WHERE sales_ID=?'
        cursor = self.conn.execute(query, (sales_ID,))
        return cursor.fetchone()

# Example usage:
# table = SalesTable()  # Create an instance of the SalesTable class
# table.insert((1, 1, 1, 2, 1, '2023-01-01', '100.00'))
# sales = table.select_all()
# print(sales)
# sale_1 = table.select_by_id(1)
# print(sale_1)
# table.update(1, (1, 1, 1, 3, 1, '2023-02-01', '150.00'))
# table.delete(1)
