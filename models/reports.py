import sqlite3

class ReportsTable:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Reports (
            report_ID INTEGER PRIMARY KEY,
            purchase_ID INTEGER,
            sales_ID INTEGER,
            cust_ID INTEGER,
            date DATE,
            FOREIGN KEY (purchase_ID) REFERENCES Purchasing(purchase_ID),
            FOREIGN KEY (sales_ID) REFERENCES Sales(sales_ID),
            FOREIGN KEY (cust_ID) REFERENCES Customer(cust_ID)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, data):
        query = '''
        INSERT INTO Reports (purchase_ID, sales_ID, cust_ID, date)
        VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, data)
        self.conn.commit()

    def update(self, report_ID, data):
        query = '''
        UPDATE Reports
        SET purchase_ID=?, sales_ID=?, cust_ID=?, date=?
        WHERE report_ID=?
        '''
        self.conn.execute(query, (*data, report_ID))
        self.conn.commit()

    def delete(self, report_ID):
        query = 'DELETE FROM Reports WHERE report_ID=?'
        self.conn.execute(query, (report_ID,))
        self.conn.commit()

    def select_all(self):
        query = 'SELECT * FROM Reports'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def select_by_id(self, report_ID):
        query = 'SELECT * FROM Reports WHERE report_ID=?'
        cursor = self.conn.execute(query, (report_ID,))
        return cursor.fetchone()

# Example usage:
# table = ReportsTable()  # Create an instance of the ReportsTable class
# table.insert((1, 1, 1, '2023-01-01'))
# reports = table.select_all()
# print(reports)
# report_1 = table.select_by_id(1)
# print(report_1)
# table.update(1, (1, 1, 1, '2023-02-01'))
# table.delete(1)
