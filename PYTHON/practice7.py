#Create a new file "Practice.txt" using python. add the following data in it:
# hii everyone
# we are learning File I/O
# Using java 
# I like programming In Java
# with open("practice.txt","w") as f:
#     f.write("hi everyone\n are learning fileI/O\n")
#     f.write("Using Java.\nI like programming in java")


#WAP that replace all occurences of "java" with "python" in above file.abs
# with open("practice.txt","r") as f:
#     data= f.read()
# new_data=data.replace("Java","Python")
# print(new_data)
# with open("practice.txt","w") as f:
#   f.write(new_data)


#Search if the word "learning" exists in the file or not.
# def check_for_word():
#     word="xlearning"
#     with open ("practice.txt","r") as f:
#         data=f.read()
#         if(data.find(word)!=-1):
#             print("Found")
#         else:
#             print("not found")
# check_for_word()


#WAp to find in which line of the file does the word "learning" occur first.
# print -1 if word not found
# def check_for_word():
#     word="programming"
#     with open ("practice.txt","r") as f:
#         data=f.read
#         if(word in data):
#             print("Found")
#         else:
#             print("not found")
# def check_for_line():
#     word="programming" 
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
            
#     return -1

# check_for_line()
# print(check_for_line())


#From a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("practice.txt","r") as f:
    data=f.read()
    print(data)
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)
    
   