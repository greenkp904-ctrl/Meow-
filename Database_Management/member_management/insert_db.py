from Database_Management import dbManage

class insert_db(dbManage):
    def __init__(self):
        # Correct way to call parent constructor
        super().__init__()

    def insert_customer(self, obj):
        try:
            # Table name must match your setup_db.py (CUSTOMER)
            query = '''INSERT INTO CUSTOMER (Customer_ID, First_Name, Middle_Name, Last_Name, DOB, Phone, Email, Address) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            data = (obj.Customer_ID, obj.First_Name, obj.Middle_Name, obj.Last_Name, 
                    obj.DOB, obj.Phone, obj.Email, obj.Address)

            # Use self.cursor inherited from dbManage
            self.cursor.execute(query, data)
            self.conn.commit()
            return 1
        
        except Exception as e:
            print(f"Database error : {e}")
            return 0
        finally:
            self.close_connection()