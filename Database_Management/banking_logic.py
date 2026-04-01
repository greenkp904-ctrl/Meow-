import sqlite3
import uuid
from datetime import datetime
from Database_Management.dbManage import dbManage

class BankingLogic(dbManage):
    def __init__(self):
        super().__init__()

    def process_transaction(self, acc_no, amount, t_type):
        """Updates account balance and logs the transaction."""
        try:
            # 1. Fetch current balance
            self.cursor.execute("SELECT Balance FROM ACCOUNT WHERE Account_No = ?", (acc_no,))
            res = self.cursor.fetchone()
            if not res: return False, "Account not found"
            
            balance = res[0]
            if t_type == "Withdrawal" and balance < amount:
                return False, "Insufficient Balance"

            # 2. Update Balance
            new_balance = balance + amount if t_type == "Deposit" else balance - amount
            self.cursor.execute("UPDATE ACCOUNT SET Balance = ? WHERE Account_No = ?", (new_balance, acc_no))

            # 3. Log into TRANSACTION table
            t_id = f"TXN{str(uuid.uuid4().int)[:8]}"
            date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.cursor.execute('''INSERT INTO "TRANSACTION" 
                (Transaction_ID, Transaction_type, Amount, Date, Account_No) 
                VALUES (?, ?, ?, ?, ?)''', 
                (t_id, t_type, amount, date_str, acc_no))
            
            self.conn.commit()
            return True, "Transaction Successful"
        except Exception as e:
            self.conn.rollback()
            return False, str(e)

    def get_transaction_history(self, account_no):
        """Fetches all transactions for a specific account for the UI table."""
        try:
            # Matches the TRANSACTION table schema
            query = '''SELECT Transaction_ID, Transaction_type, Amount, Date 
                       FROM "TRANSACTION" WHERE Account_No = ? ORDER BY Date DESC'''
            self.cursor.execute(query, (account_no,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching history: {e}")
            return []
        finally:
            self.close_connection()