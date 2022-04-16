# operators 
from ast import operator

from numpy import true_divide


a=54
b= 46

# Arithematic Operators
print("The value of a+b=",a+b)
print("The value of a-b=",a-b)
print("The value of a*b=",a*b)
print("The value of a/b=",a/b)
print("The value of a%/b=",a%b)


# Assignment operator

a= 55
print(a)
a-=2
print(a)
a+=2
print(a)
a/=5
print(a)
a*=5
print(a)


# Comparison operator

b=(20>10)
print(b)
b=(20<10)
print(b)
b=(20>=10)
print(b)
b=(20<=10)
print(b)
b=(20==10)
print(b)
b=(20!=10)
print(b)



# Logical operators

bool1=True
bool2= False
print("The value of bool1 and bool2 =",bool1 and bool2) # both true then true
print("The value of bool1 or bool2 =",bool1 or bool2)# any true then true
print("The value of not bool2 =",not bool2)  # true then false