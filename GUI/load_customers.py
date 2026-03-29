import customtkinter as ctk
from Database_Management.member_management.select import display_customer
from CTkTable import CTkTable

class ViewCustomersTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.btn_refresh = ctk.CTkButton(self, text="Refresh Database", command=self.load_customer_table)
        self.btn_refresh.pack(pady=(10, 5))

        self.table_frame = ctk.CTkScrollableFrame(self, width=700, height=400, corner_radius=10)
        self.table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.load_customer_table()

    def load_customer_table(self):
        # Clear existing table data
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        # 1. Added "Address" to the headers
        headers = ["ID", "Name", "DOB", "Phone", "Email", "Address"]
        table_data = [headers]

        customer_records = display_customer()
        
        if customer_records:
            for row in customer_records:
                # Clean up the name nicely (handles empty middle names without awkward double spaces)
                m_name = row[2] if row[2] else ""
                full_name = f"{row[1]} {m_name} {row[3]}".replace("  ", " ").strip()
                
                # 2. Grab the address from row[7]
                address = row[7] if row[7] else "N/A"
                
                # Append all data to the table row
                table_data.append([row[0], full_name, row[4], row[5], row[6], address])

        # Generate the table UI
        self.table = CTkTable(master=self.table_frame, values=table_data, header_color="#1f538d")
        self.table.pack(expand=True, fill="both", padx=10, pady=10)