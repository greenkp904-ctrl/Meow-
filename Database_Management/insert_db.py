import sqlite3

def insert_customer(obj):
    
    conn = sqlite3.connect("Database/bank_database.db")
    cursor = conn.cursor()

    try:
        query = '''INSERT INTO Customer (Customer_ID, First_Name, Middle_Name, Last_Name, DOB, Phone, Email, Address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        data = (obj.Customer_ID, obj.First_Name, obj.Middle_Name, obj.Last_Name, obj.DOB, obj.Phone, obj.Email, obj.Address)

        cursor.execute(query, data)
    
    except sqlite3.Error as e:
        print(f"Database error : {e}")
        return 0

    conn.commit()
    conn.close()