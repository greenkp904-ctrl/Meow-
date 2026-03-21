#logic.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Models.models import *
from Database_Management import *

def menu():
    print("\n1. Customer Details Management\n" \
          "2. Transaction Management\n" \
          "3. Exit\n")
    return int(input("Enter your choice[1—3] : "))

def run_logic():
    setup_database()
    print("=================================================\n"
          "============| Chettikkulangara Bank |============\n"
          "=================================================\n\n")
    control_var = 0

    while(control_var != 3):
        control_var = menu()

        if(control_var == 1):
            customer_id = input("Enter the Customer ID : ")
            first_name = input("Enter the First Name : ")
            middle_name = input("Enter the Middle Name : ")
            last_name = input("Enter the Last Name : ")
            dob = input("Enter the Date of Birth : ")
            phone = input("Enter the Phone Number : ")
            email = input("Enter the Email : ")
            address = input("Enter the Address : ")

            customer_entry = Customer(customer_id, first_name, middle_name, last_name, dob, phone, email, address)
            status = insert_customer(customer_entry)
            if(status != 0):
               print("\nCustomer details entered successfully!!!\n")
            else:
               print("\nSome Error has occured!!!") 

        elif(control_var == 2):
            display_customer()

        elif(control_var == 3):
            continue

        else:
            print("Type in the correct option, dumbass")

if __name__ == "__main__":
    run_logic()