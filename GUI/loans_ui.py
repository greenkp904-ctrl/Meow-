import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
# Ensure you create the AccountManager logic we discussed
# from Database_Management.account_management import AccountManager

class LoansTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        
        # --- Header ---
        ctk.CTkLabel(self, text="Loans here", 
                     font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, pady=20)

        # --- Form Frame ---
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, padx=40, pady=10, sticky="nsew")
        self.form_frame.grid_columnconfigure(1, weight=1)

        # Customer ID
        ctk.CTkLabel(self.form_frame, text="Customer ID:").grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.cust_id_entry = ctk.CTkEntry(self.form_frame, placeholder_text="e.g., C101")
        self.cust_id_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        # Account Type
        ctk.CTkLabel(self.form_frame, text="Account Type:").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.acc_type_var = ctk.StringVar(value="Savings")
        self.acc_type_menu = ctk.CTkOptionMenu(self.form_frame, values=["Savings", "Current", "Salary"], variable=self.acc_type_var)
        self.acc_type_menu.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        # Initial Balance
        ctk.CTkLabel(self.form_frame, text="Initial Deposit (₹):").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.balance_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Minimum 500")
        self.balance_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        # IFSC Code (Branch)
        ctk.CTkLabel(self.form_frame, text="Branch IFSC:").grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.ifsc_entry = ctk.CTkEntry(self.form_frame, placeholder_text="e.g., CBIN001")
        self.ifsc_entry.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        # --- Submit Button ---
        self.submit_btn = ctk.CTkButton(self, text="Create Account", fg_color="green", command=self.create_account)
        self.submit_btn.grid(row=2, column=0, pady=30)

    def create_account(self):
        c_id = self.cust_id_entry.get().strip()
        a_type = self.acc_type_var.get()
        bal = self.balance_entry.get().strip()
        ifsc = self.ifsc_entry.get().strip()

        if not c_id or not bal or not ifsc:
            CTkMessagebox(title="Error", message="All fields are required.", icon="cancel")
            return

        # Trigger logic (example placeholder)
        # manager = AccountManager()
        # acc_no = manager.open_new_account(c_id, a_type, float(bal), ifsc)
        
        # if acc_no:
        #    CTkMessagebox(title="Success", message=f"Account {acc_no} opened successfully!", icon="check")
        # else:
        #    CTkMessagebox(title="Fail", message="Could not create account. Verify IDs.", icon="cancel")