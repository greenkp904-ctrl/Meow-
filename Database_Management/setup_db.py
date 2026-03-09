import sqlite3

def setup_database():

    conn = sqlite3.connect('Database/bank_database.db')
    cursor = conn.cursor()

    print("Creating database tables...")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BRANCH (
        IFSC_Code TEXT PRIMARY KEY,
        Branch_Name TEXT,
        Location TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS EMPLOYEE (
        Employee_ID TEXT PRIMARY KEY,
        Name TEXT,
        Designation TEXT,
        Salary REAL,
        IFSC_Code TEXT,
        FOREIGN KEY (IFSC_Code) REFERENCES BRANCH(IFSC_Code)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CUSTOMER (
        Customer_ID TEXT PRIMARY KEY,
        First_Name TEXT,
        Middle_Name TEXT,
        Last_Name TEXT,
        DOB TEXT,
        Phone TEXT,
        Email TEXT,
        Address TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ACCOUNT (
        Account_No TEXT PRIMARY KEY,
        Account_Type TEXT,
        Balance REAL,
        Opened_Date TEXT,
        Status TEXT,
        IFSC_Code TEXT,
        FOREIGN KEY (IFSC_Code) REFERENCES BRANCH(IFSC_Code)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CUSTOMER_ACCOUNT (
        Customer_ID TEXT,
        Account_No TEXT,
        PRIMARY KEY (Customer_ID, Account_No),
        FOREIGN KEY (Customer_ID) REFERENCES CUSTOMER(Customer_ID),
        FOREIGN KEY (Account_No) REFERENCES ACCOUNT(Account_No)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS LOAN (
        Loan_ID TEXT PRIMARY KEY,
        Loan_Type TEXT,
        Interest_Rate REAL,
        Status TEXT,
        Amount REAL,
        Customer_ID TEXT,
        FOREIGN KEY (Customer_ID) REFERENCES CUSTOMER(Customer_ID)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "TRANSACTION" (
        Transaction_ID TEXT PRIMARY KEY,
        Transaction_type TEXT,
        Amount REAL,
        Date TEXT,
        Account_No TEXT,
        FOREIGN KEY (Account_No) REFERENCES ACCOUNT(Account_No)
    )''')

    conn.commit()
    conn.close()

