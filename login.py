import tkinter as tk
from tkinter import messagebox
from employee_app import EmployeeManagerApp

class Login:
    def __init__(self, root):
        self.root = root
        root.title("Login")
        root.resizable(False, False)
        self.create_gui()

    def create_gui(self):
        self.create_logo()
        self.create_username_entry()
        self.create_password_entry()
        self.create_login_button()

    def create_logo(self):
        src = "logo.png"
        self.logo = tk.PhotoImage(file=src)
        self.logo_label = tk.Label(self.root, image=self.logo)
        self.logo_label.grid(column=0, row=0, sticky='w', padx=5, pady=5, in_=self.root, columnspan=2)

    def create_username_entry(self):
        self.username_label = tk.Label(self.root, text="Username")
        self.username_label.grid(column=0, row=1, sticky='w', padx=5, pady=5, in_=self.root)

        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.grid(column=1, row=1, sticky='w', padx=5, pady=5, in_=self.root)
    
    def create_password_entry(self):
        # create password entry with beautiful style entry and show password as *
        self.password_label = tk.Label(self.root, text="Password")
        self.password_label.grid(column=0, row=2, sticky='w', padx=5, pady=5, in_=self.root)
        
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.grid(column=1, row=2, sticky='w', padx=5, pady=5, in_=self.root)

    def create_login_button(self):
        self.login_button = tk.Button(self.root, text="Login", width=10, command=self.login_button_click)
        self.login_button.grid(column=1, row=3, sticky='w', padx=5, pady=5, in_=self.root)
    
    def login_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        f = open("accounts.txt", "r")
        username_data = f.readline().strip()
        password_data = f.readline().strip()
        f.close()

        if username == username_data and password == password_data:
            self.root.destroy()
            root = tk.Tk()
            app = EmployeeManagerApp(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Wrong username or password!")
    