class Employee:
    def __init__(self, id, name, salary, department_id, department, gender):
        self.id = id
        self.name = name
        self.salary = int(salary)
        self.department = department
        self.department_id = department_id
        self.gender = gender

    def give_raise(self, percent):
        self.salary = int(self.salary + (self.salary * percent / 100))

    def encode(self):
        return "{0};{1};{2};{3};{4};{5}".format(self.id, self.name, self.salary, self.department_id, self.department, self.gender)