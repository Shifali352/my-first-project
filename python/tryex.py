try:
    a=int(input("enter a number:"))
    print(f"Multiplication table of {a}")
    for i in range(1,11):
        print(f"{a} * {i} = {a*i}")
except Exception as e:
    print("invalid input") 

    # sum of numbers
try:
    x = int(input("enter a number"))
    y = int(input("enter another number"))
    z = x + y
    print(f"the sum of {x} and {y} is {z}")
except ValueError:
    print("invalid input")

# def FUNC():
#     try:
#         l=[10,20,30]
#         index=int(input("enter an index:"))
#         print(l[index])
#     except:
#         print(" invalid index")
#     return 0
#     finally:
# print("execution completed")

# x=FUNC()
# print(x)














# #lambda function
# x=lambda a: a+3
# print(x(5))

# y=lambda a,b,c: a+10+b-9+c
# print(y(5,3,2))
# def myfunc(n):
#     return lambda a: a+n
# n=10
# x=myfunc(n)
# print(x(5))