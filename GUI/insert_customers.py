import customtkinter as ctk
from Database_Management.member_management.insert_db import insert_db
from Models import *

class InsertCustomersTab(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

        #=================Personal Information=================

        self.personal = ctk.CTkFrame(self, bg_color= "transparent")
        self.personal.grid(row = 0, column = 0, sticky = "nsew", padx = 20, pady = 20)
        self.personal.grid_columnconfigure(1, weight=1)

        personal_info_heading = ctk.CTkLabel(self.personal, text = 'Personal Information')
        personal_info_heading.grid(row = 0, column = 0, columnspan = 2, pady = (20, 10))

        customer_id_lbl = ctk.CTkLabel(self.personal, text = "Customer ID : ")
        customer_id_lbl.grid(row = 1, column = 0, padx = 20, pady = (20, 10), sticky = 'w')

        self.customer_id_txt = ctk.CTkEntry(self.personal, placeholder_text = "E.g., C101")
        self.customer_id_txt.grid(row = 1, column = 1, pady = (20, 10))

        fname_lbl = ctk.CTkLabel(self.personal, text = "First Name : ")
        fname_lbl.grid(row = 2, column = 0, padx = 20, sticky = "w", pady = (20, 10))

        self.fname_txt = ctk.CTkEntry(self.personal, placeholder_text = "E.g., John")
        self.fname_txt.grid(row = 2, column = 1, pady = (20, 10))

        midname_lbl = ctk.CTkLabel(self.personal, text = "Middle Name : ")
        midname_lbl.grid(row = 3, column = 0, padx = 20, sticky = "w", pady = (20, 10))

        self.midname_txt = ctk.CTkEntry(self.personal, placeholder_text = "Optional")
        self.midname_txt.grid(row = 3, column = 1, pady = (20, 10))

        lastname_lbl = ctk.CTkLabel(self.personal, text = "Last Name : ")
        lastname_lbl.grid(row = 4, column = 0, padx = 20, sticky = "w", pady = (20, 10))

        self.lastname_txt = ctk.CTkEntry(self.personal, placeholder_text = "E.g., Doe")
        self.lastname_txt.grid(row = 4, column = 1, pady = (20, 10))

        dob_lbl = ctk.CTkLabel(self.personal, text = "Date Of Birth : ")
        dob_lbl.grid(row = 5, column = 0, padx = 20, sticky = "w", pady = (20, 30))

        self.dob_txt = ctk.CTkEntry(self.personal, placeholder_text = "YYYY-MM-DD")
        self.dob_txt.grid(row = 5, column = 1, pady = (20, 30))

        #=================Contact Information=================

        self.contact = ctk.CTkFrame(self, bg_color="transparent")
        self.contact.grid(row = 0, column = 1, sticky = "nsew", padx = 20, pady = 20)
        self.contact.grid_columnconfigure(1, weight=1)


        contact_info_heading = ctk.CTkLabel(self.contact, text = 'Contact Information')
        contact_info_heading.grid(row = 0, column = 0, columnspan = 2, pady = (20, 10))

        phone_lbl = ctk.CTkLabel(self.contact, text = "Phone Number : ")
        phone_lbl.grid(row = 1, column = 0, padx = 20, sticky = "w", pady = (20, 10))

        self.phone_txt = ctk.CTkEntry(self.contact, placeholder_text = "Enter 10 digits")
        self.phone_txt.grid(row = 1, column = 1, pady = (20, 10))

        email_lbl = ctk.CTkLabel(self.contact, text = "Email : ")
        email_lbl.grid(row = 2, column = 0, padx = 20, sticky = "w", pady = (20, 10))

        self.email_txt = ctk.CTkEntry(self.contact, placeholder_text = "Enter the email here")
        self.email_txt.grid(row = 2, column = 1, pady = (20, 10))

        address_lbl = ctk.CTkLabel(self.contact, text = "Address : ")
        address_lbl.grid(row = 3, column = 0, padx = 20, sticky = "w", pady = (20, 30))

        self.address_txt = ctk.CTkEntry(self.contact, placeholder_text = "Enter in a comma separated, single line")
        self.address_txt.grid(row = 3, column = 1, pady = (20, 30))

        self.submit_button = ctk.CTkButton(self, text = "Submit", command = self.submit_data)
        self.submit_button.grid(row = 1, column = 0, columnspan = 2, pady = 20) 
        
    def submit_data(self):

        objnew = insert_db()

        cust_id = self.customer_id_txt.get()
        cust_fname = self.fname_txt.get()
        cust_minit = self.midname_txt.get()
        cust_lname = self.lastname_txt.get()
        cust_dob = self.dob_txt.get()
        cust_phone = self.phone_txt.get()
        cust_email = self.email_txt.get()
        cust_address = self.address_txt.get()

        new_cust = Customer(cust_id, cust_fname, cust_minit, cust_lname, cust_dob, cust_phone, cust_email, cust_address)

        status = objnew.insert_customer(new_cust)

        if status:
            print("suxs")
        else:
            print("fail")

