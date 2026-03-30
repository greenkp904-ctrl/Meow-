from Database_Management import dbManage
import sqlite3

class insert_db(dbManage):
   
    def __init__(self):
        super().__init__()

    def insert_customer(self, obj):
        try:
            query = '''INSERT INTO Customer (Customer_ID, First_Name, Middle_Name, Last_Name, DOB, Phone, Email, Address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            data = (obj.Customer_ID, obj.First_Name, obj.Middle_Name, obj.Last_Name, obj.DOB, obj.Phone, obj.Email, obj.Address)

            self.exec_query(query, data)
            return True
        
        except super.Error as e:
            print(f"Database error : {e}")
            return False

        self.close_connection()