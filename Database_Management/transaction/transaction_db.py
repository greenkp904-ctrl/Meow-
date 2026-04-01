# Add this to your existing BankingLogic class in Database_Management/banking_logic.py
def get_transaction_history(self, account_no):
    """Fetches all transactions for a specific account."""
    try:
        # Matches the "TRANSACTION" table in your setup_db.py
        query = '''SELECT Transaction_ID, Transaction_type, Amount, Date 
                   FROM "TRANSACTION" WHERE Account_No = ? ORDER BY Date DESC'''
        self.cursor.execute(query, (account_no,))
        return self.cursor.fetchall()
    except Exception as e:
        print(f"Error fetching history: {e}")
        return []
    finally:
        self.close_connection()