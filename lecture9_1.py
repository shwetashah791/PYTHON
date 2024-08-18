# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
        
#     def reset_pass(self):
#         print(self.__acc_pass)
        
# acc1=Account("12345","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass)


# class Person:
#     __name="anonymous"
    
#     def __hell0(self):
#         print("hello person")
        
#     def welcome(self):
#         self.__hello()
        
# p1=Person()

# print(p1.welcome())



#IHERITANCCE
#single inheritance
# class car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class ToyotaCar(car):
#     def __init__(self,name):
#         self.name=name
# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("prius")

# print(car1.color)

#multilevel inhertance
# class car:
#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped.")
        
# class ToyotaCar(car):
#     def __init__(self,brand):
#         self.brand=brand
        
# class Fortune(ToyotaCar):
#     def __inti__(self,type):
#         self.type=type
        
# car1=Fortune("diesel")
# car1.start()


#multiple inheritance
# class A:
#     varA="welcome to class A"
    
# class B:
#     varB="welcome to class B"
    
# class C(A,B):
#     varC="welcome to class c"
    
# c1=C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


#SUPER METHOD
# class Car:
#     def __init__(self,type):
#         self.type=type
        
#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped.")
 
        
# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()
        
        
# car1=ToyotaCar("prius","electric")
# print(car1.type)


#CLASS METHOD
# class Person:
#     name="anonymous"
    
#     def changeName(self,name):
#         self.name=name
        
# p1=Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)


# class Person:
#     name="anonymous"
    
#     def changeName(self,name):
#         self.name=name
        
# p1=Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)


# class Person:
#     name="anonymous"
    
#     @classmethod
#     def changeName(cls,name):
#         cls.name=name
        
# p1=Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)


#PROPERTY DECORATOR
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
#     def percentage(self):
#         self.percentage=str((self.phy+self.>chem+self.math)/3)+"%"
# stu=Student(98,97,99)
# print(stu1.percentage)

# stul.phy=86
# print(stu1.phy)
# stul.calcPercentage()
# print(stu1.percentage)   


# class Student:
#     def __init(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
    
        
# @property
# def percentage(self):
#     return str(self.phy+self.chem+self.math)/3+"%"

# stu1=Student(98,97,99)
# print(stu1.percentage)

# stu1.phy=86
# print(stu1.percentage)


#POLYMORPHISM
# print(1+2)#3
# print(type("apna"))
# print("apna" +"college")
# print([1,2,3] + [4,5,6])

# class Complex:
#     def __init(self, real ,img):
#         self.real=real
#         self.img=img
        
#     def showNumber(self):
#         print(self.real,"i+",self.img,"j")

# num1=Complex(1,3)
# num1.showNumber()

# num2=Complex(4,6)
# num2.showNumber()

# class Complex:
#     def __init(self, real ,img):
#         self.real=real
#         self.img=img
        
#     def showNumber(self):
#         print(self.real,"i+",self.img,"j")
    
#     def __add__(self,num2):   # dunder function
#         newReal=self.real +num2.real
#         newImg=self.img +num2.img
#         return Complex(newReal,newImg)
# num1=Complex(1,3)
# num1.showNumber()

# num2=Complex(4,6)
# num2.showNumber()

# num3=num1+num2
# num3.showNumber()