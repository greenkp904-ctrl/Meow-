import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkTable import CTkTable
from Database_Management.branch_management import BranchManager

class BranchTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        
        # --- Registration Section ---
        ctk.CTkLabel(self, text="Branch Registration", font=("Arial", 20, "bold")).grid(row=0, column=0, pady=(20, 10))

        self.reg_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.reg_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.reg_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.ifsc_entry = ctk.CTkEntry(self.reg_frame, placeholder_text="IFSC Code")
        self.ifsc_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.name_entry = ctk.CTkEntry(self.reg_frame, placeholder_text="Branch Name")
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        self.loc_entry = ctk.CTkEntry(self.reg_frame, placeholder_text="Location")
        self.loc_entry.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.save_btn = ctk.CTkButton(self, text="Register Branch", command=self.save_branch)
        self.save_btn.grid(row=2, column=0, pady=10)

        # --- View Branches Section (Like Customer Tab) ---
        ctk.CTkLabel(self, text="Existing Branches", font=("Arial", 16, "bold")).grid(row=3, column=0, pady=(20, 5))
        
        self.table_frame = ctk.CTkScrollableFrame(self, height=300, corner_radius=10)
        self.table_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        self.load_branch_table()

    def load_branch_table(self):
        # Clear existing table widgets
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        headers = ["IFSC Code", "Branch Name", "Location"]
        table_data = [headers]

        # Fetch from DB
        manager = BranchManager()
        branch_records = manager.display_branches()
        
        for row in branch_records:
            table_data.append([row[0], row[1], row[2]])

        # Create Table
        self.table = CTkTable(master=self.table_frame, values=table_data, header_color="#1f538d")
        self.table.pack(expand=True, fill="both", padx=10, pady=10)

    def save_branch(self):
        ifsc = self.ifsc_entry.get().strip()
        name = self.name_entry.get().strip()
        loc = self.loc_entry.get().strip()
        
        if not ifsc or not name:
            CTkMessagebox(title="Error", message="IFSC and Name are required.", icon="cancel")
            return

        manager = BranchManager()
        if manager.add_branch(ifsc, name, loc):
            CTkMessagebox(title="Success", message="Branch Registered!", icon="check")
            self.load_branch_table() # Refresh table automatically
            # Clear entries
            self.ifsc_entry.delete(0, 'end')
            self.name_entry.delete(0, 'end')
            self.loc_entry.delete(0, 'end')
        else:
            CTkMessagebox(title="Error", message="Registration failed.", icon="cancel")