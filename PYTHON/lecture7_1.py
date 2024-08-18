#read
# f=open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# f = open("demo.txt", "r")

# data = f.read(5)
# print(data)

# f.close()



# f=open("demo.txt", "r")

# line1 = f.readline()
# print(line1)

# f.close()



# f=open("demo.txt", "r")

# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)

# f.close()


#write
# f = open("demo.txt","a")
# f.write("I want to learn java.123")
# f.close()

# f = open("demo.txt","a")
# f.write("\nafter that node.js")
# f.close()

# f = open("sample.txt","a")
# f.write("\nafter that node.js")
# # f.close()

f = open("sample.txt","r+")
f.write("abc")
print(f.read())
f.close()