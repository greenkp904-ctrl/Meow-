import sqlite3

def get_customer_details(cust_id):
    """Fetches current data to pre-fill the update form"""
    try:
        conn = sqlite3.connect("Database/bank_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CUSTOMER WHERE Customer_ID = ?", (cust_id,))
        row = cursor.fetchone()
        conn.close()
        return row
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def delete_customer_record(cust_id):
    """Deletes a customer by ID. Use an empty string '' to remove the corrupted user."""
    try:
        conn = sqlite3.connect("Database/bank_database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM CUSTOMER WHERE Customer_ID = ? OR Customer_ID = ''", (cust_id,))
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    except Exception as e:
        print(f"Delete Error: {e}")
        return False

def update_customer_record(old_id, new_id, f_name, m_name, l_name, dob, phone, email, address):
    """Now includes Middle Name (m_name) in the update process"""
    try:
        conn = sqlite3.connect("Database/bank_database.db")
        cursor = conn.cursor()
        query = '''UPDATE CUSTOMER SET Customer_ID=?, First_Name=?, Middle_Name=?, Last_Name=?, 
                   DOB=?, Phone=?, Email=?, Address=? WHERE Customer_ID=?'''
        # Make sure the variables match the exact order of the ? in the query above
        cursor.execute(query, (new_id, f_name, m_name, l_name, dob, phone, email, address, old_id))
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    except Exception as e:
        print(f"Update Error: {e}")
        return False