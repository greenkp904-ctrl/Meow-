from Database_Management import dbManage
import sqlite3

class update_db(dbManage):
    def __init__(self):
        # Calls parent to setup self.conn and self.cursor
        super().__init__()
    
    def update_customer(self, obj):
        """Updates an existing customer record using the Customer object."""
        try:
            # Match the order of ? to the data tuple exactly
            query = '''UPDATE Customer SET 
                       First_Name = ?, 
                       Middle_Name = ?, 
                       Last_Name = ?, 
                       DOB = ?, 
                       Phone = ?, 
                       Email = ?, 
                       Address = ? 
                       WHERE Customer_ID = ?'''
            
            data = (
                obj.First_Name, 
                obj.Middle_Name, 
                obj.Last_Name, 
                obj.DOB, 
                obj.Phone, 
                obj.Email, 
                obj.Address, 
                obj.Customer_ID  # This matches the WHERE clause
            )

            # Using your parent's exec_query because it handles the COMMIT
            self.exec_query(query, data)
            
            # Debugging check: ensures the ID actually matched a row
            if self.cursor.rowcount == 0:
                print(f"Warning: No customer found with ID {obj.Customer_ID}")
                return False
                
            return True

        except sqlite3.Error as e:
            print(f"Database error during update: {e}")
            return False
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
            
        finally:
            # Ensures connection closes even if the query fails
            self.close_connection()

    def delete_customer(self, id):
        """Deletes a customer record based on Customer_ID."""
        try:
            query = '''DELETE FROM Customer WHERE Customer_ID = ?'''
            
            # CRITICAL: Added the comma to make this a proper tuple
            data = (id,)

            # Using exec_query to ensure the deletion is committed (saved)
            self.exec_query(query, data)
            
            return True

        except sqlite3.Error as e:
            print(f"Database error during deletion: {e}")
            return False
            
        finally:
            self.close_connection()