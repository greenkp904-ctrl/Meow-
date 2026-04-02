from Database_Management.dbManage import dbManage
import sqlite3

class EmployeeManager(dbManage):
    def __init__(self):
        super().__init__()

    def add_employee(self, emp_id, name, designation, salary, ifsc):
        """Inserts a new employee record linked to a branch."""
        try:
            query = '''INSERT INTO EMPLOYEE (Employee_ID, Name, Designation, Salary, IFSC_Code) 
                       VALUES (?, ?, ?, ?, ?)'''
            # Inherits exec_query from dbManage to handle commits
            return self.exec_query(query, (emp_id, name, designation, salary, ifsc))
        except sqlite3.Error as e:
            print(f"Employee DB Error: {e}")
            return False

    def get_all_employees(self):
        """Fetches all employee records for the UI table."""
        try:
            self.cursor.execute("SELECT * FROM EMPLOYEE")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching employees: {e}")
            return []
        finally:
            self.close_connection()