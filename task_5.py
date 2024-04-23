class Employee:
    def __init__(self, salary=1000):
        self.salary = salary

    def get_paid(self):
        return f"Зарплата сотрудника = {self.salary}$"


class Manager(Employee):

    def get_paid(self):
        return f"Зарплата менеджера = {self.salary}$"


class Worker(Employee):
    def get_paid(self):
        return f"Зарплата работника = {self.salary}$"
    

manager_1 = Manager(1500)
worker_1 = Worker(500)

print(manager_1.get_paid())
print(worker_1.get_paid())
