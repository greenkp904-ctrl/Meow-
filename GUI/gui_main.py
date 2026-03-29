import customtkinter as ctk
import sys
import os

# Ensure the root directory is in the path so imports work correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from GUI.load_customers import *
from Models.models import Customer
from Database_Management.member_management.insert_db import insert_db
from Database_Management.member_management.update_db import update_customer_record, get_customer_details, delete_customer_record

# Set up the appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class BankApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chettikkulangara Bank - Admin Dashboard")
        self.geometry("1000x600")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ==========================================
        # 1. LEFT SIDEBAR FRAME
        # ==========================================
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Chettikkulangara\nBank", 
                                      font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.btn_customers = ctk.CTkButton(self.sidebar_frame, text="Customers", command=self.show_customer_frame)
        self.btn_customers.grid(row=1, column=0, padx=20, pady=10)

        self.btn_transactions = ctk.CTkButton(self.sidebar_frame, text="Transactions", command=self.show_transaction_frame)
        self.btn_transactions.grid(row=2, column=0, padx=20, pady=10)

        self.btn_accounts = ctk.CTkButton(self.sidebar_frame, text="Accounts (Locked)", state="disabled")
        self.btn_accounts.grid(row=3, column=0, padx=20, pady=10)

        self.btn_loans = ctk.CTkButton(self.sidebar_frame, text="Loans (Locked)", state="disabled")
        self.btn_loans.grid(row=4, column=0, padx=20, pady=10)

        self.btn_exit = ctk.CTkButton(self.sidebar_frame, text="Exit", fg_color="transparent", 
                                     border_width=2, text_color=("gray10", "#DCE4EE"), command=self.destroy)
        self.btn_exit.grid(row=6, column=0, padx=20, pady=(10, 20))

        # ==========================================
        # 2. MAIN WORKSPACE FRAMES
        # ==========================================
        self.customer_frame = ctk.CTkFrame(self, corner_radius=10)
        self.customer_frame.grid_rowconfigure(1, weight=1)
        self.customer_frame.grid_columnconfigure(0, weight=1)
        
        self.cust_header = ctk.CTkLabel(self.customer_frame, text="Customer Management", 
                                       font=ctk.CTkFont(size=24, weight="bold"))
        self.cust_header.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        
        self.cust_tabs = ctk.CTkTabview(self.customer_frame)
        self.cust_tabs.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.cust_tabs.add("Add Customer")
        self.cust_tabs.add("View Customers")
        self.cust_tabs.add("Update Customer")
        
        self.setup_add_customer_tab()
        self.setup_update_customer_tab()
        
        view_tab = self.cust_tabs.tab("View Customers")
        self.view_customers_ui = ViewCustomersTab(master=view_tab, fg_color="transparent")
        self.view_customers_ui.pack(fill="both", expand=True)

        self.transaction_frame = ctk.CTkFrame(self, corner_radius=10)
        self.transaction_frame.grid_rowconfigure(1, weight=1)
        self.transaction_frame.grid_columnconfigure(0, weight=1)

        self.trans_header = ctk.CTkLabel(self.transaction_frame, text="Transaction Management", 
                                        font=ctk.CTkFont(size=24, weight="bold"))
        self.trans_header.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        ctk.CTkLabel(self.transaction_frame, text="Deposit / Withdrawal forms will go here...").grid(row=1, column=0)

        self.show_customer_frame()

    # --- TAB SETUP METHODS ---

    def setup_add_customer_tab(self):
        tab = self.cust_tabs.tab("Add Customer")
        form_frame = ctk.CTkScrollableFrame(tab, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.ent_id = ctk.CTkEntry(form_frame, width=300, placeholder_text="Customer ID")
        self.ent_id.pack(pady=5)
        self.ent_fname = ctk.CTkEntry(form_frame, width=300, placeholder_text="First Name")
        self.ent_fname.pack(pady=5)
        self.ent_mname = ctk.CTkEntry(form_frame, width=300, placeholder_text="Middle Name")
        self.ent_mname.pack(pady=5)
        self.ent_lname = ctk.CTkEntry(form_frame, width=300, placeholder_text="Last Name")
        self.ent_lname.pack(pady=5)
        self.ent_dob = ctk.CTkEntry(form_frame, width=300, placeholder_text="DOB (YYYY-MM-DD)")
        self.ent_dob.pack(pady=5)
        self.ent_phone = ctk.CTkEntry(form_frame, width=300, placeholder_text="Phone")
        self.ent_phone.pack(pady=5)
        self.ent_email = ctk.CTkEntry(form_frame, width=300, placeholder_text="Email")
        self.ent_email.pack(pady=5)
        self.ent_address = ctk.CTkEntry(form_frame, width=300, placeholder_text="Address")
        self.ent_address.pack(pady=5)

        self.btn_save = ctk.CTkButton(form_frame, text="Save Customer", command=self.save_customer_action)
        self.btn_save.pack(pady=20)

    def setup_update_customer_tab(self):
        tab = self.cust_tabs.tab("Update Customer")
        u = ctk.CTkScrollableFrame(tab, fg_color="transparent")
        u.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(u, text="1. Search or Delete by ID", font=ctk.CTkFont(weight="bold")).pack()
        self.ent_old_id = ctk.CTkEntry(u, width=300, placeholder_text="Enter ID to Search/Delete")
        self.ent_old_id.pack(pady=5)
        
        btn_action_frame = ctk.CTkFrame(u, fg_color="transparent")
        btn_action_frame.pack(pady=10)
        
        self.btn_load = ctk.CTkButton(btn_action_frame, text="Load Current Data", fg_color="green", command=self.load_data_to_form)
        self.btn_load.grid(row=0, column=0, padx=10)

        self.btn_delete = ctk.CTkButton(btn_action_frame, text="Delete User", fg_color="red", command=self.delete_customer_action)
        self.btn_delete.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(u, text="2. Modify Details (Leave blank to keep old data)", font=ctk.CTkFont(weight="bold")).pack(pady=(20,0))
        
        self.ent_new_id = ctk.CTkEntry(u, width=300, placeholder_text="New ID")
        self.ent_new_id.pack(pady=5)
        self.ent_up_fname = ctk.CTkEntry(u, width=300, placeholder_text="First Name")
        self.ent_up_fname.pack(pady=5)
        self.ent_up_mname = ctk.CTkEntry(u, width=300, placeholder_text="Middle Name")
        self.ent_up_mname.pack(pady=5)
        self.ent_up_lname = ctk.CTkEntry(u, width=300, placeholder_text="Last Name")
        self.ent_up_lname.pack(pady=5)
        self.ent_up_dob = ctk.CTkEntry(u, width=300, placeholder_text="DOB (YYYY-MM-DD)")
        self.ent_up_dob.pack(pady=5)
        self.ent_up_phone = ctk.CTkEntry(u, width=300, placeholder_text="Phone")
        self.ent_up_phone.pack(pady=5)
        self.ent_up_email = ctk.CTkEntry(u, width=300, placeholder_text="Email")
        self.ent_up_email.pack(pady=5)
        self.ent_up_address = ctk.CTkEntry(u, width=300, placeholder_text="Address")
        self.ent_up_address.pack(pady=5)

        self.btn_update = ctk.CTkButton(u, text="Update Everything", fg_color="orange", 
                                       command=self.update_customer_action)
        self.btn_update.pack(pady=20)

    # --- ACTION LOGIC ---

    def load_data_to_form(self):
        data = get_customer_details(self.ent_old_id.get())
        if data:
            entries = [self.ent_new_id, self.ent_up_fname, self.ent_up_mname, self.ent_up_lname, 
                       self.ent_up_dob, self.ent_up_phone, self.ent_up_email, self.ent_up_address]
            for ent in entries:
                ent.delete(0, 'end')

            self.ent_new_id.insert(0, str(data[0]))
            self.ent_up_fname.insert(0, str(data[1]))
            self.ent_up_mname.insert(0, str(data[2]) if data[2] else "") 
            self.ent_up_lname.insert(0, str(data[3]))
            self.ent_up_dob.insert(0, str(data[4]))
            self.ent_up_phone.insert(0, str(data[5]))
            self.ent_up_email.insert(0, str(data[6]))
            self.ent_up_address.insert(0, str(data[7]))
            print("Data loaded! Modify what you need and hit Update.")
        else:
            print("Customer ID not found.")

    def delete_customer_action(self):
        target_id = self.ent_old_id.get()
        success = delete_customer_record(target_id)
        if success:
            print("Customer removed successfully!")
            self.ent_old_id.delete(0, 'end') 
            self.view_customers_ui.load_customer_table() 
        else:
            print("Delete failed. Check if the ID exists.")

    def save_customer_action(self):
        new_customer = Customer(
            Customer_ID=self.ent_id.get(),
            First_Name=self.ent_fname.get(),
            Middle_Name=self.ent_mname.get(),
            Last_Name=self.ent_lname.get(),
            DOB=self.ent_dob.get(),           
            Phone=self.ent_phone.get(),
            Email=self.ent_email.get(),
            Address=self.ent_address.get()    
        )
        db_handler = insert_db()
        if db_handler.insert_customer(new_customer):
            print("Successfully added to Database!")
            for entry in [self.ent_id, self.ent_fname, self.ent_mname, self.ent_lname, 
                          self.ent_dob, self.ent_phone, self.ent_email, self.ent_address]:
                entry.delete(0, 'end')
            
            self.view_customers_ui.load_customer_table()
        else:
            print("Failed to save customer. Check if the ID already exists.")

    def update_customer_action(self):
        target_id = self.ent_old_id.get()
        if not target_id:
            print("Please enter a Target ID to update.")
            return

        # 1. Fetch current data behind the scenes
        current_data = get_customer_details(target_id)
        
        if not current_data:
            print("Error: Target ID not found in database.")
            return

        # 2. SMART MERGE: If a box is empty, use the existing database value instead!
        # current_data layout: 0:ID, 1:FName, 2:MName, 3:LName, 4:DOB, 5:Phone, 6:Email, 7:Address
        final_id      = self.ent_new_id.get()    or current_data[0]
        final_fname   = self.ent_up_fname.get()  or current_data[1]
        final_mname   = self.ent_up_mname.get()  or current_data[2]
        final_lname   = self.ent_up_lname.get()  or current_data[3]
        final_dob     = self.ent_up_dob.get()    or current_data[4]
        final_phone   = self.ent_up_phone.get()  or current_data[5]
        final_email   = self.ent_up_email.get()  or current_data[6]
        final_address = self.ent_up_address.get() or current_data[7]

        # 3. Send the safe merged data to the database
        success = update_customer_record(
            target_id, final_id, final_fname, final_mname, final_lname, 
            final_dob, final_phone, final_email, final_address
        )
        
        if success:
            print("Customer updated safely without losing old data!")
            # Clear all boxes
            entries = [self.ent_old_id, self.ent_new_id, self.ent_up_fname, self.ent_up_mname, 
                       self.ent_up_lname, self.ent_up_dob, self.ent_up_phone, self.ent_up_email, self.ent_up_address]
            for ent in entries:
                ent.delete(0, 'end')
                
            self.view_customers_ui.load_customer_table()
        else:
            print("Update failed.")

    # --- NAVIGATION ---

    def hide_all_frames(self):
        self.customer_frame.grid_forget()
        self.transaction_frame.grid_forget()

    def show_customer_frame(self):
        self.hide_all_frames()
        self.customer_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    def show_transaction_frame(self):
        self.hide_all_frames()
        self.transaction_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()