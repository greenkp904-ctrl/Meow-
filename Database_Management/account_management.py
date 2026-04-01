from Database_Management.dbManage import dbManage
import sqlite3

class AccountManager(dbManage):
    def __init__(self):
        super().__init__()

    def open_new_account(self, customer_id, acc_type, initial_balance, ifsc_code):
        """Sets up a new account and links it to a customer."""
        try:
            import uuid
            from datetime import datetime
            
            # Generate Unique Account Number
            account_no = f"ACC-{str(uuid.uuid4().hex[:6]).upper()}"
            opened_date = datetime.now().strftime("%Y-%m-%d")
            
            # 1. Insert into ACCOUNT table
            account_query = '''INSERT INTO ACCOUNT 
                               (Account_No, Account_Type, Balance, Opened_Date, Status, IFSC_Code) 
                               VALUES (?, ?, ?, ?, ?, ?)'''
            self.cursor.execute(account_query, (account_no, acc_type, initial_balance, opened_date, "Active", ifsc_code))

            # 2. Link Customer in CUSTOMER_ACCOUNT table
            link_query = '''INSERT INTO CUSTOMER_ACCOUNT (Customer_ID, Account_No) VALUES (?, ?)'''
            self.cursor.execute(link_query, (customer_id, account_no))

            self.conn.commit()
            return account_no
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            return None
        finally:
            self.close_connection()

    def display_accounts(self):
        """Fetches all accounts joined with Customer IDs for the UI table."""
        try:
            # Joins ACCOUNT and CUSTOMER_ACCOUNT tables
            query = '''
                SELECT A.Account_No, CA.Customer_ID, A.Account_Type, A.Balance, A.Status, A.IFSC_Code 
                FROM ACCOUNT A
                LEFT JOIN CUSTOMER_ACCOUNT CA ON A.Account_No = CA.Account_No
            '''
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching accounts: {e}")
            return []
        finally:
            self.close_connection()