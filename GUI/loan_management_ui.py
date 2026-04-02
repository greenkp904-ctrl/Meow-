import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkTable import CTkTable
from Database_Management.loans_management import LoanManager

class LoansManagementTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        
        # --- Header ---
        ctk.CTkLabel(self, text="Loan Management", 
                     font=ctk.CTkFont(size=22, weight="bold")).grid(row=0, column=0, pady=(20, 10))

        # --- Application Form ---
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, padx=40, pady=10, sticky="ew")
        self.form_frame.grid_columnconfigure((1, 3), weight=1)

        ctk.CTkLabel(self.form_frame, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10)
        self.cust_id_entry = ctk.CTkEntry(self.form_frame, placeholder_text="e.g., C101")
        self.cust_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Loan Type:").grid(row=0, column=2, padx=10, pady=10)
        self.loan_type_var = ctk.StringVar(value="Home")
        self.loan_menu = ctk.CTkOptionMenu(self.form_frame, values=["Home", "Car", "Education", "Business"], variable=self.loan_type_var)
        self.loan_menu.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Amount (₹):").grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Enter amount")
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.submit_btn = ctk.CTkButton(self, text="Submit Loan Application", fg_color="green", command=self.apply_loan)
        self.submit_btn.grid(row=2, column=0, pady=10)

        # --- View Table Section ---
        ctk.CTkLabel(self, text="Loan Records", font=ctk.CTkFont(size=16, weight="bold")).grid(row=3, column=0, pady=(20, 5))
        
        self.table_frame = ctk.CTkScrollableFrame(self, height=350, corner_radius=10)
        self.table_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        self.load_loan_table()

    def load_loan_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        headers = ["Loan ID", "Type", "Rate (%)", "Status", "Amount", "Cust ID"]
        table_data = [headers]

        manager = LoanManager()
        records = manager.get_all_loans()
        
        if records:
            for row in records:
                table_data.append([str(item) for item in row])
        else:
            table_data.append(["-", "-", "-", "No Loans Found", "-", "-"])

        self.table = CTkTable(master=self.table_frame, values=table_data, header_color="#1f538d")
        self.table.pack(expand=True, fill="both", padx=10, pady=10)

    def apply_loan(self):
        c_id = self.cust_id_entry.get().strip()
        l_type = self.loan_type_var.get()
        amt = self.amount_entry.get().strip()

        if not c_id or not amt:
            CTkMessagebox(title="Error", message="Please fill all fields.", icon="cancel")
            return

        manager = LoanManager()
        loan_id = manager.apply_for_loan(c_id, l_type, float(amt))
        
        if loan_id:
            CTkMessagebox(title="Success", message=f"Loan {loan_id} Applied!", icon="check")
            self.load_loan_table()
            self.amount_entry.delete(0, 'end')
        else:
            CTkMessagebox(title="Fail", message="Error applying for loan. Check Customer ID.", icon="cancel")