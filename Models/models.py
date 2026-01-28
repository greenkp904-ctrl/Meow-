#models.py

class Customer:

    customers = []

    def __init__(self, Customer_ID, Name, DOB, Phone, Email, Address):
        self.Customer_ID = Customer_ID
        self.Name = Name
        self.DOB = DOB
        self.Phone = Phone
        self.Email = Email
        self.Address = Address
        print(f"\nUser created : {self.Name}")
        self.add_to_records()

    def add_to_records(self):
        self.customers.append(self)

    @classmethod
    def display_customers(cls):
        count = 0
        for i in cls.customers:
            count += 1
            print(f"\n{count}th Customer : \n" + 
                        "===================\n\n")
            print("Customer ID : " + i.Customer_ID)
            print("Name        : " + i.Name)
            print("DOB         : " + i.DOB)
            print("Phone       : " + i.Phone)
            print("Email       : " + i.Email)
            print("Address     : " + i.Address)
            print("\n===================\n\n")
    