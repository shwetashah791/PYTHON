# class Student:
#     name="karan kumar"   
# s1=Student()
# print(s1)
# print(s1.name)

# s2=Student()
# print(s2.name)


# class Car:
#     color="blue"
#     brand="mercedes"
# car1=Car()
# print(car1.color)
# print(car1.brand)


# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
#         print("adding new student inDatabase..")
        
# s1=Student("karan")
# print(s1.name)

# s2=Student("arjun")
# print(s2.name)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student inDatabase..")
        
# s1=Student("karan",98)
# print(s1.name,s1.marks)

# s2=Student("arjun",76)
# print(s2.name,s1.marks)


# class Student:
#     college_name="ABC college"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student inDatabase..")
        
# s1=Student("karan",98)
# print(s1.name,s1.marks)

# s2=Student("arjun",76)
# print(s2.name,s1.marks)

# print(Student.college_name)


#METHODS
class Student:
    college_name="ABC college"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome student,",self.name)
    def get_marks(self):
        return self.marks
           
s1=Student("karan",98)
s1.welcome()
print(s1.get_marks)
