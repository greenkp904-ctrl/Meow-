import sqlite3

class dbManage:
    def __init__(self):
        self.conn = sqlite3.connect('Database/bank_database.db')
        self.cursor = self.conn.cursor()
    
    def close_connection(self):
        self.conn.commit()
        self.conn.close()
    
    def exec_query(self, query, data=()):
        try:
            self.cursor.execute(query, data)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            self.close_connection()