
# #functions
# from ast import Mod
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

# #prime no.

# def prime(num):
#     if num <= 1:
#         print("Prime Number")
#         return

#     for i in range(2, num):
#         if num % i == 0:
#          print("Not a Prime Number")
#          return
#     else:
#      print("prime number")

# num = int(input("Enter a number: "))
# prime(num)

# #factorial number
# def factorial(n):
#    fact=1
#    for i in range(1,n+1):
#       fact=fact*i
#       print(fact)
# num=int(input("enter the number:"))
# factorial(num)

# #palindrome
# def palindrome(n):
#    if n==n[:-1]:
#       print("palindrome")
#    else:
#       print("not palindrome")
# num=input("enter no:")
# palindrome(num)      

# #largest no. between(1-20)
# def largest():
#     list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#     largest = list[0]

#     for num in list:
#         if num > largest:
#             largest = num
#     return largest
# print("Largest number is:", largest())


#calculator 
def calculator(a,b):
    return a+b,a-b,a*b,a/b
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
op=input("enter operation:")
add,sub,mul,div=calculator(a,b)
if op=="+":
    print("Addition:",add)
elif op=="-":
    print("Subtraction:",sub)
elif op=="*":
    print("Multiplication:",mul)
elif op=="/":
    print("Division:",div)
else:
    print("invalid operation")