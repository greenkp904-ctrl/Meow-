import sqlite3

def display_customer():
    
    conn = sqlite3.connect("Database/bank_database.db")
    cursor = conn.cursor()

    try:
        query = '''SELECT * FROM Customer'''
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows 
    
    except sqlite3.Error as e:
        print(f"Database error : {e}")
        return 0

    conn.commit
    conn.close