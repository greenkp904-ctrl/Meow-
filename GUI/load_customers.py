import customtkinter as ctk
from Database_Management import *
from CTkTable import CTkTable

class ViewCustomersTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.btn_refresh = ctk.CTkButton(self, text = "Refresh Database", command = self.load_customer_table)
        self.btn_refresh.pack(pady=(10, 5))

        self.table_frame = ctk.CTkScrollableFrame(self, width = 700, height = 400, corner_radius = 10)
        self.table_frame.pack(pady = 10, padx = 20, fill = "both", expand = True)

        self.load_customer_table()

    def load_customer_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        headers = ["ID", "Name", "DOB", "Phone", "Email"]

        table_data = [headers]

        customer_records = display_customer()
        for row in customer_records:
            full_name = f"{row[1]} {row[2]} {row[3]}"
            table_data.append([row[0], full_name, row[4], row[5], row[6]])

        self.table = CTkTable(master=self.table_frame, values=table_data, header_color="#1f538d")
        self.table.pack(expand=True, fill="both", padx=10, pady=10)

        