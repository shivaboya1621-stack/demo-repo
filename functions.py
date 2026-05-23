# function - business logic is called as function
#resue the business logic
# "def" is the keyword, used to define a function
# "pass" is the keyword, representing empty function

def func_one():
    print("Welcome to functions !!")

func_one()
func_one()
func_one()

#example 2 ( no para - no return type)
def addition():
    num1 = 200
    num2 = 100
    res = num1 + num2
    print(res)

addition()

#example 3 ( no para - with return type)
def addition():
    num1 = 200
    num2 = 100
    res = num1 + num2
    return res
x = addition()
print(x)

#example 4 ( with para - no return type)
def addition(num1,num2):
    res = num1 + num2
    print(res)

addition(200,100)

#example 5 (with para - with return type)
def addition(num1,num2):
    res = num1 + num2
    return res

x = addition(200,100)
print(x)

#write the code for square of a number using function
def square(num):
    res = num * num
    return res

x = square(5)
print(x)

def addition():
    num1 = 2
    num2 = 4
    res = num1 * num2
    print(res)

addition()

# keyword arguments
def test_func(name,age):
    print(name,age)

test_func(age=40,name="shiva")

#default arguments
def test_func(name="shiva"):
    print(name)

test_func()
test_func(name="Gen Ai")
test_func(name=None)

#variable length arguments
def test_func(*nums):
    print(nums,sum(nums))

test_func(10,20,30,40,50)
test_func(100,200,300)

#keyword variable arguments
def test_func(**data):
    print(data,type(data))

test_func(name="shiva",age=28)

#param1 & param2 are positional arguments
#*param is variable length arguments
#**param is keyword variable arguments
def test_func(param1,param2,*param3,**param4):
    print(param1,param2,param3,param4)

test_func(10,20,30,40,name="shiva",age=28)


def test_func(num1,num2):
    return num1+num2, num1-num2, num1*num2, num1/num2

res = test_func(200,100)
print(type(res))
print(res)

#global variable - can be accessed anywhere in the program
x =100
def test_func():
    #local variable - can be accessed only inside the function
    x = 200
    print(x) # accessing local variable

test_func()
print(x) # accessing global variable

#nested function - function inside a function
def outer():
    def inner():
        print("Hello")
    inner()
outer()


#function definition inside a function is called nested function
def test_func():
    print("HEllo")

x = test_func
print(x)
x() # x contains the definition of test_func, so we can call it using x()

#closure - function object that remembers values in enclosing scopes even if they are not present in memory
def outer(num1):
    def inner(num2):
        return num1+num2
    return inner
x = outer(200)
res = x(100)
print(res)

square = lambda x:x*x # lambda is a keyword used to create anonymous functions (functions without a name)
print(square(5))

addition =lambda num1,num2:num1+num2 # lambda function with multiple parameters
print(addition(200,100))

students = [("std1",50),("std2",40),("std3",60)]
students.sort(key=lambda x:x[1]) # sorting the list of tuples based on the second element (marks) using lambda function as the key
print(students)

#LEGB - Local, Enclosing, Global, Built-in
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
outer()

#Decorators - a function that takes another function as an argument and extends its behavior without modifying it
def decorator(func):
    def wrapper(): # wrapper is the inner function that will extend the behavior of the original function (func) syntax
        print("security 1")
        func()
        print("security 2")
    return wrapper
@decorator
def hello():
    print("MLA")
hello()

#map function - applies a given function to all items in an iterable (list, tuple, etc.) and returns a map object (which is an iterator)
#manipulate all elements in list
nums = [1,2,3,4,5] #[100,200,300,400,500]
res =list(map(lambda x:x*100,nums))
print(res)

#filter function - constructs an iterator from elements of an iterable for which a function returns true
#apply conditions to all elements in list
num = [1,2,3,4,5]
res = list(filter(lambda x:x%2==0,num))
print(res)

#reduce function - applies a rolling computation to sequential pairs of values in a list (or any iterable) and returns a single value
#it is used to find the sum of list elements
from functools import reduce
nums = [1,2,3,4,5]
res = reduce(lambda num1,num2:num1+num2,nums)
print(res)

#first class functions - functions that can be treated as first-class citizens (can be assigned to variables, passed as arguments, and returned from other functions)
#store "functions" in "variables"
#pass "functions" as arguments to other functions
#return "functions" from other functions
def test_func():
    print("Hello")

x = test_func # if we need the raw code remove the parentheses, if we add parentheses it will call the function and store the return value in x
x() # calling the function using the variable x

def test_func1():
    print("hello")

def test_func2(func):
    func() # calling the function passed as an argument

test_func2(test_func1) # passing the function test_func1 as an argument to test_func2



#pandas is a library used for data manipulation and analysis in Python. It provides data structures like Series and DataFrame, which are used to store and manipulate data in a tabular format. Pandas is built on top of NumPy and is widely used in data science and machine learning for data cleaning, transformation, and analysis.
# data analysis
#data cleaning
#data transformation   
#data visualization preparation
#csv/excel file handling
#frequently we will use in machine learning

# > pip install pandas

#import
#import pandas as pd

#print(pd.__version__)

# 1.switch to python_basics
   #cd python_basics or cd basics
#2.create requirements.txt
   # pandas

#3.create virtual environment
   # python -m venv venv 
   #or
   # python3 -m venv venv
#4.activate virtual environment
   #venv\Scripts\activate (windows)
   #source venv/bin/activate (linux/mac)

#5.install requirements.txt file
    # pip install -r requirements.txt
