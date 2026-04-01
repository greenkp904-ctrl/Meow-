import customtkinter as ctk
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from GUI.load_customers import *
from GUI.insert_customers import *
from GUI.update_customers import UpdateCustomersTab

# Set up the appearance
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class BankApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Chettikkulangara Bank - Admin Dashboard")

        if sys.platform == "win32":
            self.state("zoomed")
        elif sys.platform.startswith("linux"):
            self.attributes("-zoomed", True)

        # Configure grid layout (1 row, 2 columns)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) # Main workspace expands

        # ==========================================
        # 1. LEFT SIDEBAR FRAME
        # ==========================================
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1) # Pushes the bottom buttons down

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Chettikkulangara\nBank", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Sidebar Navigation Buttons
        self.btn_customers = ctk.CTkButton(self.sidebar_frame, text="Customers", command=self.show_customer_frame)
        self.btn_customers.grid(row=1, column=0, padx=20, pady=10)

        self.btn_transactions = ctk.CTkButton(self.sidebar_frame, text="Transactions", command=self.show_transaction_frame)
        self.btn_transactions.grid(row=2, column=0, padx=20, pady=10)

        # Placeholder for future features (Disabled for now)
        self.btn_accounts = ctk.CTkButton(self.sidebar_frame, text="Accounts (Locked)", state="disabled")
        self.btn_accounts.grid(row=3, column=0, padx=20, pady=10)

        self.btn_loans = ctk.CTkButton(self.sidebar_frame, text="Loans (Locked)", state="disabled")
        self.btn_loans.grid(row=4, column=0, padx=20, pady=10)

        # Bottom Sidebar Button
        self.btn_exit = ctk.CTkButton(self.sidebar_frame, text="Exit", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.destroy)
        self.btn_exit.grid(row=6, column=0, padx=20, pady=(10, 20))

        # ==========================================
        #2. MAIN WORKSPACE FRAMES
        # ==========================================
        # We create all frames here, but only place one on the grid at a time.

        # --- Customer Frame ---
        self.customer_frame = ctk.CTkFrame(self, corner_radius=10)
        self.customer_frame.grid_rowconfigure(1, weight=1)
        self.customer_frame.grid_columnconfigure(0, weight=1)
        
        self.cust_header = ctk.CTkLabel(self.customer_frame, text="Customer Management", font=ctk.CTkFont(size=24, weight="bold"))
        self.cust_header.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        
        # Adding Tabs inside the Customer Frame (Add, View, Update)
        self.cust_tabs = ctk.CTkTabview(self.customer_frame)
        self.cust_tabs.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.cust_tabs.add("Add Customer")
        self.cust_tabs.add("View Customers")
        self.cust_tabs.add("Update Customer")
        
        #=================View Customers=========================

        view_customers = self.cust_tabs.tab("View Customers")

        self.view_customers_ui = ViewCustomersTab(master=view_customers, fg_color="transparent")
        self.view_customers_ui.pack(fill="both", expand=True)

        #=================Insert Customers=======================

        insert_customers = self.cust_tabs.tab("Add Customer")

        self.insert_customers_ui = InsertCustomersTab(master=insert_customers, fg_color="transparent")
        self.insert_customers_ui.pack(fill="both", expand=True)

        #=================Insert Customers=======================

        update_customers = self.cust_tabs.tab("Update Customer")
        self.update_customers_ui = UpdateCustomersTab(master=update_customers, fg_color="transparent")
        self.update_customers_ui.pack(fill = "both", expand = True)
     
        # --- Transaction Frame ---

        self.transaction_frame = ctk.CTkFrame(self, corner_radius=10)
        self.transaction_frame.grid_rowconfigure(1, weight=1)
        self.transaction_frame.grid_columnconfigure(0, weight=1)

        self.trans_header = ctk.CTkLabel(self.transaction_frame, text="Transaction Management", font=ctk.CTkFont(size=24, weight="bold"))
        self.trans_header.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        ctk.CTkLabel(self.transaction_frame, text="Deposit / Withdrawal forms will go here...").grid(row=1, column=0)

        # ==========================================
        # 3. INITIALIZATION
        # ==========================================
        # Show the Customer frame by default when the app starts
        self.show_customer_frame()

    # --- Navigation Logic ---
    def hide_all_frames(self):
        """Removes all frames from the grid (hides them)"""
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