import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkTable import CTkTable
from Database_Management.banking_logic import BankingLogic

class TransactionTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        
        # --- Header ---
        #ctk.CTkLabel(self, text="Transaction Management", 
                    # font=ctk.CTkFont(size=22, weight="bold")).grid(row=0, column=0, pady=(20, 10))

        # --- Input Form ---
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, padx=40, pady=10, sticky="ew")
        self.form_frame.grid_columnconfigure((1, 3), weight=1)

        ctk.CTkLabel(self.form_frame, text="Account No:").grid(row=0, column=0, padx=10, pady=10)
        self.acc_entry = ctk.CTkEntry(self.form_frame, placeholder_text="ACC-XXXX")
        self.acc_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Type:").grid(row=0, column=2, padx=10, pady=10)
        self.type_var = ctk.StringVar(value="Deposit")
        self.type_menu = ctk.CTkOptionMenu(self.form_frame, values=["Deposit", "Withdrawal"], variable=self.type_var)
        self.type_menu.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Amount (₹):").grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry = ctk.CTkEntry(self.form_frame, placeholder_text="0.00")
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # --- Action Buttons ---
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.grid(row=2, column=0, pady=10)

        self.exec_btn = ctk.CTkButton(self.btn_frame, text="Execute Transaction", 
                                      fg_color="#28a745", command=self.run_trans)
        self.exec_btn.pack(side="left", padx=10)

        self.refresh_btn = ctk.CTkButton(self.btn_frame, text="Refresh History", 
                                         command=self.view_history)
        self.refresh_btn.pack(side="left", padx=10)

        # --- History Table Section ---
        ctk.CTkLabel(self, text="Transaction History", font=ctk.CTkFont(size=16, weight="bold")).grid(row=3, column=0, pady=(20, 5))
        
        self.table_frame = ctk.CTkScrollableFrame(self, height=350, corner_radius=10)
        self.table_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

    def run_trans(self):
        acc = self.acc_entry.get().strip()
        amt_str = self.amount_entry.get().strip()
        t_type = self.type_var.get()
        
        if not acc or not amt_str:
            CTkMessagebox(title="Error", message="All fields are required.", icon="cancel")
            return

        try:
            amt = float(amt_str)
            db = BankingLogic()
            success, msg = db.process_transaction(acc, amt, t_type)
            
            if success:
                CTkMessagebox(title="Success", message=f"Transaction Complete!", icon="check")
                self.view_history() # Refresh table
                self.amount_entry.delete(0, 'end')
            else:
                CTkMessagebox(title="Failed", message=msg, icon="cancel")
        except ValueError:
            CTkMessagebox(title="Error", message="Invalid Amount.", icon="cancel")

    def view_history(self):
        """Fetches and displays history for the account."""
        acc = self.acc_entry.get().strip()
        if not acc:
            return # Don't show error on initial load if field is empty

        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        headers = ["Transaction ID", "Type", "Amount", "Date"]
        table_data = [headers]

        db = BankingLogic()
        records = db.get_transaction_history(acc)
        
        if records:
            for row in records:
                table_data.append([str(item) for item in row])
        else:
            table_data.append(["-", "No Records", "-", "-"])

        self.table = CTkTable(master=self.table_frame, values=table_data, header_color="#1f538d")
        self.table.pack(expand=True, fill="both", padx=10, pady=10)