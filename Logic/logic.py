#logic.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Models.models import *

def menu():
    print("\n1. Add User\n" \
          "2. Show Users\n" \
          "3. Exit\n")
    return int(input("Enter your choice[1—3] : "))

def run_logic():
    print("=================================================\n"
          "============| Chettikkulangara Bank |============\n"
          "=================================================\n\n")
    control_var = 0

    while(control_var != 3):
        control_var = menu()

        if(control_var == 1):
             customer_id = input("Enter the Customer ID : ")
             name = input("Enter the Name : ")
             dob = input("Enter the Date of Birth : ")
             phone = input("Enter the Phone Number : ")
             email = input("Enter the Email : ")
             address = input("Enter the Address : ")

             customer_entry = Customer(customer_id, name, dob, phone, email, address)

             print("\nCustomer details entered successfully!!!\n")

        elif(control_var == 2):
            Customer.display_customers()

        elif(control_var == 3):
            continue

        else:
            print("Type in the correct option, dumbass")

if __name__ == "__main__":
    run_logic()