from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.__list_employees = []

    def add_employee(self, new_employee):
        self.__list_employees.append(new_employee)

    def remove_employee(self, id):
        for item in self.__list_employees:
            if item.id == id:
                self.__list_employees.remove(item)
                return True
        return False

    def get_employee_by_id(self, id):
        for item in self.__list_employees:
            if item.id == id:
                return item
        return None

    def get_all_employees(self):
        return self.__list_employees
    
    def load_employee(self):
        f = open("NV.txt", "r", encoding="utf-8")
        self.__list_employees.clear()
        for line in f:
            line = line.strip()
            words = line.split(";")
            new_employee = Employee(words[0], words[1], words[2], words[3], words[4], words[5])
            self.__list_employees.append(new_employee)
        
    def save_employee(self):
        f = open("NV.txt", "w", encoding="utf-8")
        for item in self.__list_employees:
            f.write(item.encode())
            f.write("\n")
        f.close()