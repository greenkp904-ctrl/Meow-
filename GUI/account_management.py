import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkTable import CTkTable
from Database_Management.account_management import AccountManager

class AccountsManagementTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        
        # --- Header ---
        ctk.CTkLabel(self, text="Account Management", 
                     font=ctk.CTkFont(size=22, weight="bold")).grid(row=0, column=0, pady=(20, 10))

        # --- Registration Form ---
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, padx=40, pady=10, sticky="ew")
        self.form_frame.grid_columnconfigure((1, 3), weight=1)

        ctk.CTkLabel(self.form_frame, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10)
        self.cust_id_entry = ctk.CTkEntry(self.form_frame, placeholder_text="C101")
        self.cust_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Type:").grid(row=0, column=2, padx=10, pady=10)
        self.acc_type_var = ctk.StringVar(value="Savings")
        self.acc_type_menu = ctk.CTkOptionMenu(self.form_frame, values=["Savings", "Current"], variable=self.acc_type_var)
        self.acc_type_menu.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Deposit (₹):").grid(row=1, column=0, padx=10, pady=10)
        self.balance_entry = ctk.CTkEntry(self.form_frame, placeholder_text="500")
        self.balance_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="IFSC Code:").grid(row=1, column=2, padx=10, pady=10)
        self.ifsc_entry = ctk.CTkEntry(self.form_frame, placeholder_text="BK001")
        self.ifsc_entry.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        self.submit_btn = ctk.CTkButton(self, text="Open New Account", fg_color="green", command=self.create_account)
        self.submit_btn.grid(row=2, column=0, pady=10)

        # --- View Table Section ---
        ctk.CTkLabel(self, text="Existing Accounts List", font=ctk.CTkFont(size=16, weight="bold")).grid(row=3, column=0, pady=(20, 5))
        
        self.table_frame = ctk.CTkScrollableFrame(self, height=350, corner_radius=10)
        self.table_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        self.load_account_table()

    def load_account_table(self):
        """Refreshes the table with fresh data from the database."""
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        headers = ["Account No", "Customer ID", "Type", "Balance", "Status", "IFSC"]
        table_data = [headers]

        manager = AccountManager()
        records = manager.display_accounts()
        
        if records:
            for row in records:
                table_data.append([str(item) for item in row])
        else:
            table_data.append(["-", "-", "No Accounts Found", "-", "-", "-"])

        self.table = CTkTable(master=self.table_frame, values=table_data, header_color="#1f538d")
        self.table.pack(expand=True, fill="both", padx=10, pady=10)

    def create_account(self):
        c_id = self.cust_id_entry.get().strip()
        a_type = self.acc_type_var.get()
        try:
            bal = float(self.balance_entry.get().strip())
        except:
            CTkMessagebox(title="Error", message="Invalid Deposit Amount", icon="cancel")
            return
        ifsc = self.ifsc_entry.get().strip()

        if not c_id or not ifsc:
            CTkMessagebox(title="Error", message="All fields required", icon="cancel")
            return

        manager = AccountManager()
        acc_no = manager.open_new_account(c_id, a_type, bal, ifsc)
        
        if acc_no:
            CTkMessagebox(title="Success", message=f"Account {acc_no} created!", icon="check")
            self.load_account_table() # Refresh the view
            self.cust_id_entry.delete(0, 'end')
            self.balance_entry.delete(0, 'end')
        else:
            CTkMessagebox(title="Fail", message="Error creating account. Check Customer ID and IFSC.", icon="cancel")