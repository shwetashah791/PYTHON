# #WAP to print the length of a list.(list is the parameter)
# cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
# heroes=["thor","ironman","captain america","shaktiman"]
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(heroes)

#WAP to print the elements of a list in a single line.(list is the parameter)

# cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
# heroes=["thor","ironman","captain america","shaktiman"]
# def print_len(list):
#     print(len(list))
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
        
# print_list(heroes)
# print_list(cities)


#WAP to find the factorial of n.(n is the parameter)
# n=5
# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# calc_fact(3)

#wap to conver USD to INR
# def converter(usd_val):
#     inr_val=usd_val*83
#     print(usd_val,"USD=",inr_val,"INR")
# converter(73)


#Write a recursive function to calculate the sum of first n natural numbers
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1)+n
# sum=calc_sum(5)
# print(sum)

#WAP a recursive function to print all elements in a list
# hint: use list & index as parameter
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
fruits=["mango","litchi","apple","banana"]

print_list(fruits)