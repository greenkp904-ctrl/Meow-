from Database_Management.dbManage import dbManage
import sqlite3
import uuid

class LoanManager(dbManage):
    def __init__(self):
        super().__init__()

    def apply_for_loan(self, cust_id, loan_type, amount):
        """Inserts a new loan application into the database."""
        try:
            loan_id = f"L-{str(uuid.uuid4().hex[:6]).upper()}"
            # Standard rates: Home (8.5%), Car (10.5%), Education (7.0%), Business (12.0%)
            rates = {"Home": 8.5, "Car": 10.5, "Education": 7.0, "Business": 12.0}
            rate = rates.get(loan_type, 10.0)
            
            query = '''INSERT INTO LOAN (Loan_ID, Loan_Type, Interest_Rate, Status, Amount, Customer_ID) 
                       VALUES (?, ?, ?, ?, ?, ?)'''
            self.cursor.execute(query, (loan_id, loan_type, rate, "Pending", amount, cust_id))
            self.conn.commit()
            return loan_id
        except sqlite3.Error as e:
            print(f"Loan Error: {e}")
            return None
        finally:
            self.close_connection()

    def get_all_loans(self):
        """Fetches all loan records for the UI table."""
        try:
            self.cursor.execute("SELECT * FROM LOAN")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching loans: {e}")
            return []
        finally:
            self.close_connection()