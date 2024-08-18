#Create student class that takes name and marks of 3 subjects as arguments in constructor. This create a method to print the average.
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your average score:",sum/3)
# s1=Student("tony stark",[99,98,97])
# s1.get_avg()

# s1.name = "iron man" 
# s1.get_avg()


#Create Account with 2 attributes- balances and account no. Creae  methods for debit ,credit and printing the balance
class Account:
   def __init__(self,bal,acc):
       self.balance=bal
       self.account_no=acc
   def debit(self,amount):
       self.balance-=amount
       print("Rs",amount,"was debited")
       print("total balance=",self.get_balance())
   def credit(self,amount):
       self.balance+=amount
       print("Rs",amount,"was credited")
       print("total balance=",self.get_balance())
   def get_balance(self):
       return self.balance
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(5000)
acc1.debit(1000)
acc1.debit(9000)
print(acc1.balance)
print(acc1.account_no)