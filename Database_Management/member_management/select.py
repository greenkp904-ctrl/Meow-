import sqlite3

def display_customer():
    conn = sqlite3.connect("Database/bank_database.db")
    cursor = conn.cursor()

    try:
        query = '''SELECT * FROM CUSTOMER'''
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows 
    
    except sqlite3.Error as e:
        print(f"Database error : {e}")
        return []
        
    finally:
        # The 'finally' block ensures the database is ALWAYS closed and unlocked
        # Notice we added the parentheses () to execute the close command!
        conn.close()