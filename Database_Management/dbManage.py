import sqlite3

class dbManage:
    def __init__(self):
        self.conn = sqlite3.connect('Database/bank_database.db')
        self.cursor = self.conn.cursor()
    
    def close_connection(self):
        self.conn.commit()
        self.conn.close()