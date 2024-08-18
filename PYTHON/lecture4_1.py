# info={
#     "name" : "apnacollege",
#     "subjects" : ["python","C","java"],
#     "topics" :("dict","set"),
#     "age" : 35,
#     "is_adult" : True,
#     12.99 : 94.4
# }
# print(type(info))
# print((info))
# print(info["name"])
# print(info["age"])
# print(info["subjects"])
# print(info["topics"])

# info={
#     "name" : "apnacollege",
#     "subjects" : ["python","C","java"],
#     "topics" :("dict","set"),
#     "age" : 35,
#     "is_adult" : True,
#     12.99 : 94.4
# }
# # info["name"] =23
# # info["surname"] ="khapra"
# # print(info)

# null_dict={}
# null_dict["name"]="apnacollege"
# print(null_dict)

#nested dictionary

student={
    "name":"rahul kumari",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95        
    }
}
# print(student)
# print(student["subject"]["chem"])
# print(student["subject"])

# print(student.keys())
# print(len(student))
# print(len(list(student.keys())))
# print(student.values())
# print(student.items())
# print(list(student.items()))
# print(pairs[0])
# print(student["name"])  #error
# rint(student.get("name2"))   # gives none

student.update({"city" : "delhi"})
print(student)

new_dict ={"city" : "delhi" , "age": 16}
student.udate(new_dict)
print(student)