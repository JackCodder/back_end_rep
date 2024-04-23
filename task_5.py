class Employee:
    def __init__(self, salary=1000):
        self.salary = salary

    def get_paid(self):
        return f"Зарплата сотрудника = {self.salary}$"


class Manager(Employee):
    def __init__(self, salary=1500):
        self.salary = salary

    def get_paid(self):
        return f"Зарплата менеджера = {self.salary}$"


class Worker(Employee):
    def __init__(self, salary=500):
        self.salary = salary

    def get_paid(self):
        return f"Зарплата работника = {self.salary}$"
    

manager_1 = Manager()
worker_1 = Worker()

print(manager_1.get_paid())
print(worker_1.get_paid())
