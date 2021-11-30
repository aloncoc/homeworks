from main import Employee

class Kablan(Employee):
    def __init__(self,id,name,age,adress,per_project,project_num):
        super().__init__(id,name,age,adress)
        self.per_project = per_project
        self.project_num = project_num
        
    def calculate_salary(self):
        return  self.per_project * self.project_num


    def __str__(self):
        return super().__str__() + f'Kablan salary = {self.calculate_salary()} '

k=Kablan(12,'david',32,'herzeliya',3450,4)
print(k)
