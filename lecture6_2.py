#RECURSION
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)    #5 4=n-1 3=n-2 2=n-1 1

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(5) 

#RECURSION n!
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(9))