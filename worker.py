from main import  Employee


class Worker(Employee):
    def __init__(self,id,name,age,adress,hours_per_day,hours_rate):
        super().__init__(id,name,age,adress)
        self.hours_per_day = hours_per_day
        self.hours_rate = hours_rate

    def calculate_salary(self):
        return self.hours_per_day * self.hours_rate
    def __str__(self):
        return f'worker salary = {self.calculate_salary()} '+\
            super().__str__()
w = Worker(14,'Daniel',24,'Rishon',8,47)
print(w)
