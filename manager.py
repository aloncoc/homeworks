from main import Employee
class Manager(Employee):
    def __init__(self,id,name,age,adress,number_emlpoyes,employee_rate):
        super().__init__(id,name,age,adress)
        self.number_employes = number_emlpoyes
        self.employee_rate = employee_rate

    def calculate_salary(self):
        return self.number_employes * self.employee_rate

    def __str__(self):
        return f' managar salary = {self.calculate_salary()} '+ \
               super().__str__()
m = Manager(12,'david',32,'herzeliya',3450,4)
print(m)
