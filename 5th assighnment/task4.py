class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus

def print_employees(emps):
    for e in emps:
        print(f"{e.name}: {e.get_role()}, salary: {e.get_salary()}")

#demonstration
e1 = Employee("Arsen jorsey", 50000)
m1 = Manager("Daur", 1000000, 100000)
print_employees([e1, m1])