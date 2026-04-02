import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkTable import CTkTable
from Database_Management.employee_management import EmployeeManager

class EmployeeManagementTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        
        # --- Header ---
        ctk.CTkLabel(self, text="Employee Management", 
                     font=ctk.CTkFont(size=22, weight="bold")).grid(row=0, column=0, pady=(20, 10))

        # --- Registration Form ---
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, padx=40, pady=10, sticky="ew")
        self.form_frame.grid_columnconfigure((1, 3), weight=1)

        ctk.CTkLabel(self.form_frame, text="Employee ID:").grid(row=0, column=0, padx=10, pady=10)
        self.emp_id_entry = ctk.CTkEntry(self.form_frame, placeholder_text="e.g., E001")
        self.emp_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Name:").grid(row=0, column=2, padx=10, pady=10)
        self.name_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Full Name")
        self.name_entry.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Designation:").grid(row=1, column=0, padx=10, pady=10)
        self.desig_entry = ctk.CTkEntry(self.form_frame, placeholder_text="e.g., Manager")
        self.desig_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Salary (₹):").grid(row=1, column=2, padx=10, pady=10)
        self.salary_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Monthly Salary")
        self.salary_entry.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self.form_frame, text="Branch IFSC:").grid(row=2, column=0, padx=10, pady=10)
        self.ifsc_entry = ctk.CTkEntry(self.form_frame, placeholder_text="BK001")
        self.ifsc_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.submit_btn = ctk.CTkButton(self, text="Register Employee", fg_color="green", command=self.save_employee)
        self.submit_btn.grid(row=2, column=0, pady=20)

        # --- View Table ---
        ctk.CTkLabel(self, text="Current Employees", font=ctk.CTkFont(size=16, weight="bold")).grid(row=3, column=0, pady=(10, 5))
        
        self.table_frame = ctk.CTkScrollableFrame(self, height=300, corner_radius=10)
        self.table_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        self.load_employee_table()

    def load_employee_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        headers = ["Emp ID", "Name", "Designation", "Salary", "Branch IFSC"]
        table_data = [headers]

        manager = EmployeeManager()
        records = manager.get_all_employees()
        
        if records:
            for row in records:
                table_data.append([str(item) for item in row])
        else:
            table_data.append(["-", "No Employees Found", "-", "-", "-"])

        self.table = CTkTable(master=self.table_frame, values=table_data, header_color="#1f538d")
        self.table.pack(expand=True, fill="both", padx=10, pady=10)

    def save_employee(self):
        e_id = self.emp_id_entry.get().strip()
        name = self.name_entry.get().strip()
        desig = self.desig_entry.get().strip()
        sal = self.salary_entry.get().strip()
        ifsc = self.ifsc_entry.get().strip()

        if not all([e_id, name, desig, sal, ifsc]):
            CTkMessagebox(title="Error", message="All fields are required.", icon="cancel")
            return

        manager = EmployeeManager()
        if manager.add_employee(e_id, name, desig, float(sal), ifsc):
            CTkMessagebox(title="Success", message="Employee Registered!", icon="check")
            self.load_employee_table()
            # Clear entries
            for entry in [self.emp_id_entry, self.name_entry, self.desig_entry, self.salary_entry, self.ifsc_entry]:
                entry.delete(0, 'end')
        else:
            CTkMessagebox(title="Error", message="Failed to register employee.", icon="cancel")