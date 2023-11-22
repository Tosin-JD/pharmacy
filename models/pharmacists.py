import sqlite3

class PharmacistTable:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Pharmacist (
            phar_ID INTEGER PRIMARY KEY,
            fname VARCHAR(255),
            lname VARCHAR(255),
            gender INTEGER,
            age INTEGER,
            contact_add INTEGER,
            phar_email VARCHAR(255),
            phar_pass VARCHAR(255)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, data):
        query = '''
        INSERT INTO Pharmacist (fname, lname, gender, age, contact_add, phar_email, phar_pass)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, data)
        self.conn.commit()

    def update(self, phar_ID, data):
        query = '''
        UPDATE Pharmacist
        SET fname=?, lname=?, gender=?, age=?, contact_add=?, phar_email=?, phar_pass=?
        WHERE phar_ID=?
        '''
        self.conn.execute(query, (*data, phar_ID))
        self.conn.commit()

    def delete(self, phar_ID):
        query = 'DELETE FROM Pharmacist WHERE phar_ID=?'
        self.conn.execute(query, (phar_ID,))
        self.conn.commit()

    def select_all(self):
        query = 'SELECT * FROM Pharmacist'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def select_by_id(self, phar_ID):
        query = 'SELECT * FROM Pharmacist WHERE phar_ID=?'
        cursor = self.conn.execute(query, (phar_ID,))
        return cursor.fetchone()

# Example usage:
# table = PharmacistTable()  # Create an instance of the PharmacistTable class
# table.insert(('John', 'Doe', 1, 25, 12345, 'john.doe@example.com', 'password123'))
# pharmacists = table.select_all()
# print(pharmacists)
# john = table.select_by_id(1)
# print(john)
# table.update(1, ('John', 'Doe', 1, 26, 12345, 'john.doe@example.com', 'newpassword'))
# table.delete(1)
