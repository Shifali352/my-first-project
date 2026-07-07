# create a tuple
t=(1)
print(type(t))

#converting a string to tuple
t_1=tuple("hello world")
print(t_1)
print(type(t_1))

t_2=tuple(input("enter elements of tuple="))
print(t_2)

#tranversing a tuple
t=("1,2,3,4,5")
for i in t:
    print(i)

    
t=(1,2,3)
print(t*3)

t=(1,2,3,4,5)
seq=t[1:-1]
print(seq)

t=(1,2,3,4,5,6,7,8,9)
tp=t[0:10:2]
print(tp)

