import sqlite3

def display_customer():
    
    conn = sqlite3.connect("Database/bank_database.db")
    cursor = conn.cursor()

    try:
        query = '''SELECT * FROM Customer'''
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("No records found.")
        else:
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} {row[3]} | Phone: {row[5]}")
    
    except sqlite3.Error as e:
        print(f"Database error : {e}")
        return 0

    conn.commit
    conn.close