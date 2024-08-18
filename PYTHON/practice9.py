#Define a ciecle class to create a circle with radius r using the constructor. Define an Area()method of the class which calculates the area of the circle. Define a Periemeter() method of the class which allows you to calculate the perimeter of the circle
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         return 2*3.14*self.radius **2
    
#     def perimeter(self):
#         return 2*3.14*self.radius
    
# c1=Circle(21)
# print(c1.area())
# print(c1.perimeter())

#Define a Employee class with attribute role, department and salary. this class 
class Employee:
    def __init__(self, role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",slef.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75000")

engg1=Engineer("Elon Musk",40)
engg11.showDetails
e1=Employee("accountant","Finance","60,000")
e1.showDetails()
