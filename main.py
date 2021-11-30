#1   לא ניתן לייצר מופע שלה הדרך היחידה היא להשתמש בקוד של המחלקה דרף המחלקות שיורשות אותה.
#2 כדאי ליצור פרמטרים שיהיו תקפים לכל הקלאס
#6 בכדי להדפיס את הערכים שנשמרו באבא



from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def __init__(self,id,name,age,adress):
        self.id = id
        self.name = name
        self.age = age
        self.adress = adress
    @abstractmethod    
    def  calculate_salary(self):
        pass

        
    def __str__(self):
     return f'id = {self.id} name = {self.name} age = {self.age} ' +\
         f'adress = {self.adress} '
            
        
