# teachers={
# "John":"Java",
# "Jane":"Python",
# "Mike":"C++",
# }
# print(teachers["John"])


# d={"Vowel1":"A",
#    "Vowel2":"E",
#    "Vowel3":"I",
#    "Vowel4":"O",
#    "Vowel5":"U"
#   }

# for key in d:
#    print(key,end=' ')
#    print(d[key],end=' ')



# #adding elements to dictionary
# employee={"Name":"John",
#             "Age":30,
#             "Role":"Developer",
#             "salary":50000,
#             }
# employee['dept']="sales"
# print(employee)

# #updating elements in dictionary
# employee={"Name":"John",
#             "Age":30,           
#             "Role":"Developer",
#             "salary":50000,
#             }
# employee['salary']=60000
# print(employee)

# #PROGRAM

# n=int(input("How many students? "))
# compwinners={}
# for a in range(n):
#    name=input("Enter name: ")
#    marks=int(input("Enter marks: "))
#    compwinners[name]=marks
# print(compwinners)
# print("The Dictionarynow is:")    

# #Deleting elements from dictionary
# Emp13={"Name":"John",
#        "Age":30,
#        "Role":"Developer",
# }
# del Emp13["Role"]
# print(Emp13)

# #USING pop() METHOD

# Emp14={"Name":"John",
#         "Age":30,
#         "Role":"Developer",
# }
# Emp14.pop("Age")
# print(Emp14)


# emp={"Name":"John",
#      "Age":30,
#        "Role":"Developer",
# }                                                       
# print('Age' in emp)
# print('dept' in emp)

# #length function
# student={"name":"karan",
#         "age":20,
#         "grade":"A"}
# print(len(student))


# student={"name":"karan",
#         "age":20,
#         "grade":"A"}
# print(student.clear())



# student={"name":"karan",
#         "age":20,
#         "grade":"A"}
# my_list=student.items()
# for z in my_list:
#     print(z)


# student={"name":"karan",
# "age":20,
#         "grade":"A"}
# print(student.get("age"))



# student={"name":"karan",
#         "age":20,
#         "grade":"A"}
# print(student.keys())


# employee_1={"Name":"John",
#            "Age":30,
#                "Role":"Developer",}
# employee_2={"Name":"Jane",
#            "Age":25,
#                "Role":"Designer",}
# employee_1.update(employee_2)
# print(employee_1)
# print(employee_2)


#program
#list1=['a','e','i']
#list2=[1,2,3]
#list3=['hi','hello','welcome']
#print("orginally:")
#print("list1=",list1)
#print("list2=",list2)
#print("list3=",list3)
#list1.append(list2)
#list1.insert(0,list3)
#print("After appending and inserting:")
#print("list1=",list1)




#list1=['a','e','i']
#list2=[1,2,3]
#list3=['hi','hello','welcome']
#print("orginally:")
#print("list1=",list1)
#print("list2=",list2)
#print("list3=",list3)
#list3.extend(list1)
#list3.extend(list2)
#print("After extending:")
#print(list3)




#program that finds an element index/position without using index()
#list1=['a','e','i','o','u']
#element=input("Enter element to find its index: ")
#for i in range(len(list1)):
 #   if list1[i]==element:
  #      print("Index of",element,"is",i)
   #     break
#else:
 #    print(element,"not found in the list")



# #functions
# from ast import Mod
# from importlib.resources import simple
# from numpy import add

# def calculation(x):
#    return x*x+2*x+3
# result=calculation(2)
# print(result)

# def arithmetc(a,b):
#    return a+b,a-b,a*b,a/b,a%b
# num_1=int(input("Enter first number: "))
# num_2=int(input("Enter second number: "))
# add,sub,mul,div,mod=arithmetc(num_1,num_2)
# print("Addition:",add)
# print("Subtraction:",sub)
# print("Multiplication:",mul)
# print("Division:",div)
# print("Modulus:",mod)


# #simple interest
# def simple_interest(p,r,t):
#    si=(p*r*t)/100
#    return si
# principal=float(input("Enter principal amount: "))
# rate=float(input("Enter rate of interest: "))
# time=float(input("Enter time in years: "))
# interest=simple_interest(principal,rate,time)
# print("Simple Interest is:",interest)

# import program
# program.greet("Alice")
# a=program.p1["name"]
# print(a)


# def interest(principal,time=2,rate=5):
#    return principal*rate*time
# prin=float(input("Enter principal amount: "))
# print("Simple Interest is:")
# si1=interest(prin)
# print("rs.",si1)
# roi=float(input("Enter rate of interest: "))
# time_period=int(input("Enter time in years: "))
# print("Simple Interest is:")
# si2=interest(prin,time_period,roi/100)
# print("rs.",si2)


# #program to find the marks, grades using functions
# def calc_grade(marks):
#    return 'A' if marks>=90 else 'B' if marks>=80 else 'C' if marks>=70 else 'D' if marks>=60 else 'F'
# num_students=int(input("Enter number of students: "))
# student_records={}
# for _ in range(num_students):
#    name=input("Enter student name: ")
#    marks=int(input("Enter marks obtained: "))
#    grade=calc_grade(marks)
#    student_records[name]={'marks':marks,'grade':grade}
# print("Student Records:")
# for student,record in student_records.items():
#    print(f"Name: {student}, Marks: {record['marks']}, Grade: {record['grade']}")

# import program
# program.greet("Alice")
# a=program.p1["name"]
# print(a)
