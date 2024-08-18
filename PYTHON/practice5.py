#print numbers from 1 to 100
# i=1
# while i<=100:
#    print(i)
#    i+=1
   
#print numbers from 100 to 1.
# i=100
# while i<=1:
#    print(i)
#    i-=1
   
#print the multipliaction table  of number n.
# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
# i=1
# while i<=10:
#     print(i*i)
#     i+=1

# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1

# heroes=["ironman","thor","superman","batman"]
# idx=0
# while idx<len(heroes):
#    print(heroes[idx])
#    idx+=1

#search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]
# nums=[1,4,9,16,25,36,49,64,81,100,36]

# x=36

# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("FOUND at idx", i)
#     else:
#         print("finding..")
#     i+=1

#print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
# nums=[1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)
    
#search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]
# nums=[1,4,9,16,25,36,49,64,81,100,49]
# x=49
# idx=0
# for el in nums:
#     if(el==x):
#         print("number found at idx", idx)
#         break
#     idx+=1


#print numbers form 1 to 100
# for i in range(1,101):
#     print(i)

#print numbers for 100 to 1
# for i in range(100,0,-1):
#     print(i)

#print the multiplication table n
# n=int(input("enter number:"))
# for i in range(1,11):
#     print(n*i)


#WAP to find the sum of first n  natural numbers.(using while)
# n=5
# sum=0
# for i in range (1,n+1):
#     sum+=i
# print("total sum=",sum)

# n=7 
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("total sum+",sum)

# Wap to find the factorial of first n numbers. (using for)
n=5 
fact=1
i=1
while i<=n:     #while loop
    fact*=i
    i+=1
print("factorial=",fact)

n=5
fact=1
for i in range(1,n+1):   # for loop
    fact*=i
print("factorial=",fact)