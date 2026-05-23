num1 = 100
num2 = -100
print(num1)
print(num2)
print(type(num1))

hexa =0xA
print(hexa)
octa = 0o12
print(octa)
bina = 0b1010
print(bina)

large = 1234567890123456789012345678901234567890
print(large)

print(10/2)
print(10//3) #floor division
print(10%3) #modulo operator

temp = 98.3
print(temp)
print(type(temp))

expo = 2e-4
print(expo)

compl1 = 4 + 5j
print(compl1.real)
print(compl1.imag) 
print(type(compl1))

num1 = 10
float1 = float(num1)
print(float1)

float2 = 10.9
num2 = int(float2)
print(num2)

print(max(10, 20, 30))
print(min(10, 20, 30))
print(divmod(10, 3))
print(pow(2, 3))

#string
#collection of characters
# 1)"" 2)'' 3)""" """ 4)''' '''
# define multiline string, then we will use """"
str1 ="Hello"
str2 ='Welcome'
str3 ="""
       welcome to Gen AI & Agentic AI
       we will cover real appln also
       we will cover deployment also
       
     
       """
print(str1)
print(str2)
print(str3)

name = "shiva"
age = 28
print("My name is %s and age is %d" %(name ,age))
print("My name is {} and age is {}".format(name,age))
print(f"My name is {name} and age is {age}")

#boolean
#True(1) and False(0)
flag = True
flag1 = False
print(flag)
print(flag1)
print(True + True)
#print(True / False)
print(True + 1 + True + False)

 # list
 # ordered collection of elements
 # []
 # heterogeneous elements

list1 = [10, 20 , 30, 40, 50]
print(list1[0])
print(list1[-5])
print(list1[0:3])
print(list1[1:4])
print(list1[:4])
print(list1[3:]) #uses list slicing in Python.
print(list1[::-1])

#tuple
#ordered collection of elements
#() parenthesis
#immutable (we can't modify the data)
t1 = (10, 20, 30, 40, 50)
print(t1[0],t1[-5])
print(t1[0:3])
print(t1[-3:-1])
print(t1[2:])
print(t1[:2])
print(t1[::-1])
print(type(t1))

#dictionary
#used to store data in key value pair
d1 = {
       "name": "shiva",
       "age": 28,
       "marks": "95"
}
print(d1["name"], d1["age"], d1["marks"])
print(type(d1))
print(d1.keys())
print(d1.values())
print(d1.items())

#set
#wont allow duplicate values
# {}
#unordered collection of elements
s1 = {10, 10}
print(s1)
print(type(s1))
s2 = {10, 20, 30, 10,20, 30,"Hello",True,"Hello"}
print(s2)

#None
#used to represent the absence of a value
#empty / no value
emp1 = None
print(emp1)
print(type(emp1))
emp1 = "EMP001"
print(emp1)

#data types we are completed
#number - int, float, complex
#string - "" , '' , """ """ , ''' ''' we represent string

#boolean - True =1 and False =0
#list - ordered collection of elements, [] , heterogeneous elements , mutable
#tuple - ordered collection of elements, () parenthesis, immutable
#dictionary - used to store data in key value pair, {}, keys() ,values() ,items()
#set - wont allow duplicate values, {} , unordered collection of elements
#None - used to represent the absence of a value, empty / no value

#tuple converted to list
t1 = (10, 20, 30, 40, 50)
#list() is the predefined function , used to convert tupe to list
list1 = list(t1)
list1[0] = 1000
#tuple() is the predefined function , used to convert list to tuple
t2 = tuple(list1)
print(t2)


