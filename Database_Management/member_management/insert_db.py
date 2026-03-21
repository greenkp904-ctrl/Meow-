from Database_Management import dbManage

class insert_db(dbManage):
   
    def __init__():
        super.__init__()

    def insert_customer(obj):
        try:
            query = '''INSERT INTO Customer (Customer_ID, First_Name, Middle_Name, Last_Name, DOB, Phone, Email, Address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            data = (obj.Customer_ID, obj.First_Name, obj.Middle_Name, obj.Last_Name, obj.DOB, obj.Phone, obj.Email, obj.Address)

            super.cursor.execute(query, data)
        
        except super.Error as e:
            print(f"Database error : {e}")
            return 0

        super.close_connection()