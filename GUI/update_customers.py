import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
# Ensure these imports match your project structure
from Database_Management.member_management.update_db import update_db
from Models import Customer 
import sqlite3

class UpdateCustomersTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configure the main grid for two columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # ================== 1. SEARCH HEADER (Always Visible) ==================
        self.search_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.search_frame.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.search_lbl = ctk.CTkLabel(self.search_frame, text="Enter Customer ID:")
        self.search_lbl.pack(side="left", padx=10)
        
        self.search_txt = ctk.CTkEntry(self.search_frame, placeholder_text="e.g., C101")
        self.search_txt.pack(side="left", padx=10)
        
        self.fetch_btn = ctk.CTkButton(self.search_frame, text="Fetch Details", 
                                       command=self.fetch_and_reveal)
        self.fetch_btn.pack(side="left", padx=10)

        # ================== 2. PERSONAL INFO FRAME (Hidden Initially) ==================
        self.personal = ctk.CTkFrame(self, fg_color="transparent")
        
        ctk.CTkLabel(self.personal, text='Personal Information', 
                     font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # ID (Disabled so user can't change the Primary Key)
        ctk.CTkLabel(self.personal, text="Customer ID:").grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.cust_id_display = ctk.CTkEntry(self.personal, state="disabled")
        self.cust_id_display.grid(row=1, column=1, pady=10)

        # First Name
        ctk.CTkLabel(self.personal, text="First Name:").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.fname_txt = ctk.CTkEntry(self.personal)
        self.fname_txt.grid(row=2, column=1, pady=10)

        # Middle Name
        ctk.CTkLabel(self.personal, text="Middle Name:").grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.midname_txt = ctk.CTkEntry(self.personal)
        self.midname_txt.grid(row=3, column=1, pady=10)

        # Last Name
        ctk.CTkLabel(self.personal, text="Last Name:").grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.lastname_txt = ctk.CTkEntry(self.personal)
        self.lastname_txt.grid(row=4, column=1, pady=10)

        # DOB
        ctk.CTkLabel(self.personal, text="Date Of Birth:").grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.dob_txt = ctk.CTkEntry(self.personal)
        self.dob_txt.grid(row=5, column=1, pady=10)

        # ================== 3. CONTACT INFO FRAME (Hidden Initially) ==================
        self.contact = ctk.CTkFrame(self, fg_color="transparent")
        
        ctk.CTkLabel(self.contact, text='Contact Information', 
                     font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Phone
        ctk.CTkLabel(self.contact, text="Phone Number:").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.phone_txt = ctk.CTkEntry(self.contact)
        self.phone_txt.grid(row=1, column=1, pady=10)

        # Email
        ctk.CTkLabel(self.contact, text="Email:").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.email_txt = ctk.CTkEntry(self.contact)
        self.email_txt.grid(row=2, column=1, pady=10)

        # Address
        ctk.CTkLabel(self.contact, text="Address:").grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.address_txt = ctk.CTkEntry(self.contact)
        self.address_txt.grid(row=3, column=1, pady=10)

        self.save_btn = ctk.CTkButton(self, text="Save Changes", 
                                      fg_color="green", hover_color="darkgreen",
                                      command=self.save_data)
        self.delete_btn = ctk.CTkButton(self, text = "Delete Record", fg_color = "red", hover_color = "#AA0000", command=self.delete_record)

    def fetch_and_reveal(self):
        target_id = self.search_txt.get().strip()
        
        # This calls your DB logic (ensure display_specific is imported)
        from Database_Management import display_specific
        fetched_data = display_specific(target_id)

        if fetched_data and len(fetched_data) > 0:
            # 1. Reveal the UI elements using grid
            self.personal.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
            self.contact.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
            self.save_btn.grid(row=2, column=0, pady=40, padx=(100, 10), sticky="ew")
            self.delete_btn.grid(row=2, column=1, pady=40, padx=(10, 100), sticky="ew")
            # 2. Populate the fields
            row = fetched_data[0]
            
            # Update ID display (temporary unlock to insert)
            self.cust_id_display.configure(state="normal")
            self.cust_id_display.delete(0, "end")
            self.cust_id_display.insert(0, row[0])
            self.cust_id_display.configure(state="disabled")

            # Helper to clear and fill entries
            for entry, val in zip([self.fname_txt, self.midname_txt, self.lastname_txt, 
                                   self.dob_txt, self.phone_txt, self.email_txt, self.address_txt], 
                                  row[1:]):
                entry.delete(0, "end")
                entry.insert(0, str(val) if val else "")

            CTkMessagebox(title="Found", message=f"Data for {target_id} loaded.", icon="check", option_1="OK")
        else:
            self.hide_form()
            CTkMessagebox(title="Error", message="Customer ID not found.", icon="cancel")

    def hide_form(self):
        self.personal.grid_forget()
        self.contact.grid_forget()
        self.save_btn.grid_forget()

    def save_data(self):
        updated_id = self.cust_id_display.get() # Primary Key
        new_fname = self.fname_txt.get()
        new_mname = self.midname_txt.get()
        new_lname = self.lastname_txt.get()
        new_dob = self.dob_txt.get()
        new_phone = self.phone_txt.get()
        new_email = self.email_txt.get()
        new_addr = self.address_txt.get()

        print(f"DEBUG: Attempting to save new name: {new_fname}")

        # Create the model object
        new_cust_obj = Customer(updated_id, new_fname, new_mname, new_lname, 
                                new_dob, new_phone, new_email, new_addr)

        # Call the DB Update logic
        db_handler = update_db()
        if db_handler.update_customer(new_cust_obj):
            CTkMessagebox(title="Success", message="Customer updated successfully!", icon="check")
            # self.hide_form() # Optional: hide after save
        else:
            CTkMessagebox(title="Failed", message="Database update failed.", icon="cancel")

    def delete_record(self):
        # 1. Open the Warning Box with Yes/No options
        msg = CTkMessagebox(
            title="Confirm Deletion",
            message="Are you sure you want to permanently delete this record?\nThis action cannot be undone.",
            icon="warning",
            option_1="No",
            option_2="Yes",
            button_color="#FF0000",   # The "Very Bright Red" for the buttons
            button_hover_color="#AA0000"
        )
        
        # 2. Capture the user's choice
        response = msg.get()
        
        # 3. Only run the DB logic if they clicked "Yes"
        if response == "Yes":
            # Get the ID from the (disabled) ID entry box
            cust_id = self.cust_id_display.get()
            
            # Create a temporary object for the delete method
            from Models import Customer
           
            
            db_handler = update_db()
            if db_handler.delete_customer(cust_id):
                CTkMessagebox(title="Deleted", message="Record removed successfully.", icon="check")
                self.hide_form() # Clear the UI
                self.search_txt.delete(0, "end")
            else:
                CTkMessagebox(title="Error", message="Database deletion failed.", icon="cancel")
        else:
            # They clicked "No" or closed the window - do nothing
            print("Deletion cancelled by user.")