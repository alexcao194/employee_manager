import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog, messagebox
from employee_manager import EmployeeManager
from employee import Employee

class EmployeeManagerApp:
    def __init__(self, root):
        self.root = root
        root.title("Employee Manager")
        root.resizable(False, False)
        self.employee_manager = EmployeeManager()
        self.employee_manager.load_employee()
        self.create_gui()
        self.update_treeview()

    def create_gui(self):
        self.create_treeview()
        self.create_buttons()
        self.create_detail_frame()

    # Tạo treeview
    def create_treeview(self):
        self.tree = ttk.Treeview(self.root, column=("c1", "c2", "c3", "c4"), show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="STT")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="ID")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Name")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Department")
        self.tree.grid(column=0, row=0, sticky='nsew', in_=self.root)
        self.tree.bind("<ButtonRelease-1>", self.treeview_click)


    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.grid(column=1, row=0, sticky='nsew', in_=self.root)
        add_button = tk.Button(frame, text="Add", width=10, command=self.add_button_click)
        add_button.grid(column=0, row=0, sticky='nsew', in_=frame)
        remove_button = tk.Button(frame, text="Remove", width=10, command=self.remove_button_click)
        remove_button.grid(column=0, row=1, sticky='nsew', in_=frame)
        raise_button = tk.Button(frame, text="Raise", width=10, command=self.raise_button_click)
        raise_button.grid(column=0, row=3, sticky='nsew', in_=frame)
        reload_button = tk.Button(frame, text="Reload", width=10, command=self.reload_button_click)
        reload_button.grid(column=0, row=4, sticky='nsew', in_=frame)
        save_button = tk.Button(frame, text="Save", width=10, command=self.save_button_click)
        save_button.grid(column=0, row=5, sticky='nsew', in_=frame)

    def create_detail_frame(self):
        self.detail_frame = tk.Frame(self.root)
        self.id_label = tk.Label(self.detail_frame, text="ID")
        self.id_label.grid(column=0, row=0, sticky='w', in_=self.detail_frame)
        self.id_data = tk.Label(self.detail_frame, text="")
        self.id_data.grid(column=1, row=0, sticky='w', in_=self.detail_frame)
        self.name_label = tk.Label(self.detail_frame, text="Name")
        self.name_label.grid(column=0, row=1, sticky='w', in_=self.detail_frame)
        self.name_data = tk.Label(self.detail_frame, text="")
        self.name_data.grid(column=1, row=1, sticky='w', in_=self.detail_frame)
        self.salary_label = tk.Label(self.detail_frame, text="Salary")
        self.salary_label.grid(column=0, row=2, sticky='w', in_=self.detail_frame)
        self.salary_data = tk.Label(self.detail_frame, text="")
        self.salary_data.grid(column=1, row=2, sticky='w', in_=self.detail_frame)
        self.department_label = tk.Label(self.detail_frame, text="Department")
        self.department_label.grid(column=0, row=3, sticky='w', in_=self.detail_frame)
        self.department_data = tk.Label(self.detail_frame, text="")
        self.department_data.grid(column=1, row=3, sticky='w', in_=self.detail_frame)
        self.department_id_label = tk.Label(self.detail_frame, text="Department ID")
        self.department_id_label.grid(column=0, row=4, sticky='w', in_=self.detail_frame)
        self.department_id_data = tk.Label(self.detail_frame, text="")
        self.department_id_data.grid(column=1, row=4, sticky='w', in_=self.detail_frame)
        self.gender_label = tk.Label(self.detail_frame, text="Gender")
        self.gender_label.grid(column=0, row=5, sticky='w', in_=self.detail_frame)
        self.gender_data = tk.Label(self.detail_frame, text="")
        self.gender_data.grid(column=1, row=5, sticky='w', in_=self.detail_frame)
        self.detail_frame.grid(column=0, row=1, sticky='nsew', columnspan=2, in_=self.root)


    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        employee_list = self.employee_manager.get_all_employees()
        for i, employee in enumerate(employee_list):
            self.tree.insert("", "end", values=(i + 1, employee.id, employee.name, employee.department))

    # Hàm xử lý sự kiện click vào treeview
    def treeview_click(self, event):
        # Lấy item được chọn
        selected_item = self.tree.selection()
        if selected_item:
            employee_id = self.tree.item(selected_item)['values'][1]
            employee = self.employee_manager.get_employee_by_id(employee_id)
            self.update_detail(employee)

    # Hàm xử lý sự kiện click vào nút Add
    def add_button_click(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add employee")
        add_window.resizable(False, False)

        id_label = tk.Label(add_window, text="ID")
        id_label.grid(column=0, row=0, sticky='w', in_=add_window)
        id_entry = tk.Entry(add_window, width=50)
        id_entry.grid(column=1, row=0, sticky='w', in_=add_window, columnspan=2)

        name_label = tk.Label(add_window, text="Name")
        name_label.grid(column=0, row=1, sticky='w', in_=add_window)
        name_entry = tk.Entry(add_window, width=50)
        name_entry.grid(column=1, row=1, sticky='w', in_=add_window, columnspan=2)

        salary_label = tk.Label(add_window, text="Salary")
        salary_label.grid(column=0, row=2, sticky='w', in_=add_window)
        salary_entry = tk.Entry(add_window, width=50)
        salary_entry.grid(column=1, row=2, sticky='w', in_=add_window, columnspan=2)

        department_combo = ttk.Combobox(add_window, width=48)
        department_combo.grid(column=1, row=3, sticky='w', in_=add_window, columnspan=2)
        department_combo['values'] = ["Sale", "Marketing", "IT", "Accounting", "HR"]
        department_combo.current(0)
        department_label = tk.Label(add_window, text="Department")
        department_label.grid(column=0, row=3, sticky='w', in_=add_window)

        gender_value = tk.StringVar()
        gender_label = tk.Label(add_window, text="Gender")
        gender_label.grid(column=0, row=4, sticky='w', in_=add_window)
        male_radio_button = tk.Radiobutton(add_window, value="Male", text="Male", variable=gender_value)
        female_radio_button = tk.Radiobutton(add_window, value="Female", text="Female", variable=gender_value)
        male_radio_button.grid(column=1, row=4, sticky='w', in_=add_window)
        female_radio_button.grid(column=2, row=4, sticky='w', in_=add_window)
        

        def add_button_click_in_add_window():
            id = id_entry.get()
            name = name_entry.get()
            salary = salary_entry.get()
            department = department_combo.get()
            department_id = department_combo.get()[0:2].upper()
            gender = gender_value.get()
            if id == "" or name == "" or salary == "" or department == "" or department_id == "" or gender == "":
                messagebox.showerror("Error", "Please input all fields!")
                return
            if id in [item.id for item in self.employee_manager.get_all_employees()]:
                messagebox.showerror("Error", "ID existed!")
                return
            new_employee = Employee(id, name, salary, department_id, department, gender)
            self.employee_manager.add_employee(new_employee)
            self.update_treeview()
            messagebox.showinfo("Success", "Add employee successfully!")
            add_window.destroy()

        add_button = tk.Button(add_window, text="Add", width=10, command=add_button_click_in_add_window)
        add_button.grid(column=1, row=5, sticky='nsew', in_=add_window)

        for child in add_window.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def remove_button_click(self):
        try:
            id = self.tree.item(self.tree.selection())['values'][1]
        except IndexError:
            messagebox.showerror("Error", "Please select an employee!")
            return
        if self.employee_manager.remove_employee(id):
            self.tree.delete(self.tree.selection())
            messagebox.showinfo("Success", "Remove employee successfully!")
        else:
            messagebox.showerror("Error", "Employee not found!")

    def raise_button_click(self):
        try:
            id = self.tree.item(self.tree.selection())['values'][1]
        except IndexError:
            messagebox.showerror("Error", "Please select an employee!")
            return
        percent = simpledialog.askfloat("Raise", "Input raise percent(%)")
        if percent is not None:
            employee = self.employee_manager.get_employee_by_id(id)
            employee.give_raise(float(percent))
            self.update_detail(employee)

    def reload_button_click(self):
        self.employee_manager.load_employee()
        self.update_treeview()
        messagebox.showinfo("Success", "Reload employee successfully!")

    def update_detail(self, employee):
        self.id_data['text'] = employee.id
        self.name_data['text'] = employee.name
        self.salary_data['text'] = employee.salary
        self.department_data['text'] = employee.department
        self.department_id_data['text'] = employee.department_id
        self.gender_data['text'] = employee.gender

    def save_button_click(self):
        self.employee_manager.save_employee()
        messagebox.showinfo("Success", "Save employee successfully!")


