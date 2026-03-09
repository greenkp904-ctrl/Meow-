import sqlite3

def setup_database():

    conn = sqlite3.connect('bank_database.db')
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

    print("Inserting initial records...")

    cursor.executemany('''INSERT OR IGNORE INTO BRANCH VALUES (?, ?, ?)''', [
        ('SBIN0001234', 'Kozhikode Main', 'Mavoor Road, Kozhikode'),
        ('SBIN0005678', 'Kochi InfoPark', 'Kakkanad, Kochi'),
        ('SBIN0009101', 'Trivandrum City', 'MG Road, Trivandrum'),
        ('SBIN0001112', 'Kannur Central', 'Thavakkara, Kannur'),
        ('SBIN0001314', 'Thrissur Round', 'Swaraj Round, Thrissur')
    ])

    cursor.executemany('''INSERT OR IGNORE INTO EMPLOYEE VALUES (?, ?, ?, ?, ?)''', [
        ('E001', 'Rahul Nair', 'Manager', 75000.00, 'SBIN0001234'),
        ('E002', 'Sneha Menon', 'Cashier', 35000.00, 'SBIN0005678'),
        ('E003', 'Arun Kumar', 'Loan Officer', 45000.00, 'SBIN0009101'),
        ('E004', 'Priya Varghese', 'Clerk', 30000.00, 'SBIN0001112'),
        ('E005', 'Vishnu Das', 'Assistant Manager', 60000.00, 'SBIN0001314')
    ])

    cursor.executemany('''INSERT OR IGNORE INTO CUSTOMER VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', [
        ('C101', 'Ajay', '', 'Krishnan', '1995-04-12', '9876543210', 'ajay@email.com', '123 Palm Villa, Kozhikode'),
        ('C102', 'Meera', 'T', 'Joseph', '1988-11-25', '8765432109', 'meera.j@email.com', '45B Marine Drive, Kochi'),
        ('C103', 'Karthik', 'Raja', 'Pillai', '2001-02-14', '7654321098', 'karthik@email.com', '78 Lane, Trivandrum'),
        ('C104', 'Anjali', '', 'Menon', '1992-08-05', '6543210987', 'anjali.m@email.com', 'Fort Road, Kannur'),
        ('C105', 'Fahad', 'Ali', 'Khan', '1985-12-30', '5432109876', 'fahad@email.com', 'Green Park, Thrissur')
    ])

    cursor.executemany('''INSERT OR IGNORE INTO ACCOUNT VALUES (?, ?, ?, ?, ?, ?)''', [
        ('A5001', 'Savings', 25000.50, '2023-01-15', 'Active', 'SBIN0001234'),
        ('A5002', 'Current', 150000.00, '2022-06-10', 'Active', 'SBIN0005678'),
        ('A5003', 'Savings', 5400.75, '2024-02-20', 'Active', 'SBIN0009101'),
        ('A5004', 'Fixed Deposit', 500000.00, '2021-11-05', 'Active', 'SBIN0001112'),
        ('A5005', 'Savings', 1200.00, '2023-09-18', 'Inactive', 'SBIN0001314')
    ])

    cursor.executemany('''INSERT OR IGNORE INTO CUSTOMER_ACCOUNT VALUES (?, ?)''', [
        ('C101', 'A5001'),
        ('C102', 'A5002'),
        ('C103', 'A5003'),
        ('C104', 'A5004'),
        ('C105', 'A5005')
    ])

    cursor.executemany('''INSERT OR IGNORE INTO LOAN VALUES (?, ?, ?, ?, ?, ?)''', [
        ('L901', 'Home Loan', 8.5, 'Approved', 2500000.00, 'C101'),
        ('L902', 'Car Loan', 9.2, 'Active', 800000.00, 'C102'),
        ('L903', 'Education', 7.5, 'Pending', 500000.00, 'C103'),
        ('L904', 'Personal', 12.0, 'Approved', 150000.00, 'C104'),
        ('L905', 'Business', 10.5, 'Active', 1200000.00, 'C105')
    ])

    cursor.executemany('''INSERT OR IGNORE INTO "TRANSACTION" VALUES (?, ?, ?, ?, ?)''', [
        ('T0001', 'Deposit', 5000.00, '2024-02-25', 'A5001'),
        ('T0002', 'Withdrawal', 2000.00, '2024-02-26', 'A5001'),
        ('T0003', 'Transfer', 15000.00, '2024-02-26', 'A5002'),
        ('T0004', 'Deposit', 1000.00, '2024-02-27', 'A5003'),
        ('T0005', 'Interest Credit', 250.00, '2024-02-27', 'A5004'),
        ('T0006', 'Withdrawal', 500.00, '2024-02-28', 'A5003'),
        ('T0007', 'Deposit', 20000.00, '2024-02-28', 'A5002'),
        ('T0008', 'Transfer', 3000.00, '2024-02-29', 'A5005'),
        ('T0009', 'ATM Withdrawal', 1000.00, '2024-03-01', 'A5001'),
        ('T0010', 'Fee Deduction', 50.00, '2024-03-01', 'A5002')
    ])

    conn.commit()
    conn.close()
    print("Database built and records inserted successfully!")

if __name__ == "__main__":
    setup_database()