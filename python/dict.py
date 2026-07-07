# teachers={
#     "john":"java",
#     "jane":"python",
    
# }
# print(teachers["jane"])


# d={"vowel1":"A",
#    "vowel2":"B",
#    "vowel3":"c",
#    "vowel4":"d"
# }
# for key in d:
#     print(key,end=' ')
#     print(d[key],end=' ')

# employee={"name": "john",
#           "age": 45,
#           "role": "developer",
#           "salary": "40000"}
# employee["dept"] = "it"
# print(employee)


# employee={"name": "john",
#           "age": 45,
#           "role": "developer",
#           "salary": 40000}
# employee["salary"] = 50000
# print(employee)


# #pop
# student = {
#     "name": "Shefali",
#     "age": 15,
#     "grade": "10th"
# }
# student.pop("age")
# print(student)

# #length
# student = {
#     "name": "Shefali",
#     "age": 15,
#     "class": 10
# }
# print(len(student))

# #clear
# student = {
#     "name": "Shefali",
#     "age": 15,
#     "class": 10}

# print(student.clear())

# #get
# student = {
#     "name": "john",
#     "age": 15,
#     "class": 10}

# print(student.get("name"))

 #Create lists
# list2 = [1, 2, 3]
# list3 = [4, 5, 6]
# list2.append(7)      
# list3.insert(0, 0)   

# list1 = list2 + list3

# print("List1 =", list1)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.append(7)

# # Using extend()
# list1.extend(list2)
# print("List1 =", list1)


#append() and insert()
list1=['a','e','i']
list2=[1,2,3]
list3=['hi','hello','welcome']
print("orginally:")
print("list1=",list1)
print("list2=",list2)
print("list3=",list3)
list1.append(list2)
list1.insert(0,list3)
print("After appending and inserting:")
print("list1=",list1)



#extend()
list1=['a','e','i']
list2=[1,2,3]
list3=['hi','hello','welcome']
print("orginally:")
print("list1=",list1)
print("list2=",list2)
print("list3=",list3)
list3.extend(list1)
list3.extend(list2)
print("After extending:")
print(list3)




#finds the element index/position without using index()
list1=['a','e','i','o','u']
element=input("Enter element to find its index: ")
for i in range(len(list1)):
   if list1[i]==element:
       print("Index of",element,"is",i)
       break
else:
    print(element,"not found in the list")


