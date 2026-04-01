from Database_Management.dbManage import dbManage
import sqlite3

class BranchManager(dbManage):
    def __init__(self):
        super().__init__()

    def add_branch(self, ifsc, name, location):
        """Inserts a new branch into the BRANCH table."""
        try:
            query = "INSERT INTO BRANCH (IFSC_Code, Branch_Name, Location) VALUES (?, ?, ?)"
            return self.exec_query(query, (ifsc, name, location))
        except sqlite3.Error as e:
            print(f"Branch Database Error: {e}")
            return False

    def display_branches(self):
        """Fetches all records from the BRANCH table for the UI table."""
        try:
            self.cursor.execute("SELECT * FROM BRANCH")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching branches: {e}")
            return []
        finally:
            self.close_connection()