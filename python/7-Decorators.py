# elzeor from 83 to

# function are objects
# decorator take a function and add some functionality and returns it
# it is a higher order function(function accept function as parameter)
# you can add more than one decorator to the same function

def myDecorator(func):
    def nestedFunc(): # for decoration
        print("before")
        func()
        print("after")   
    return nestedFunc

def sayhello():
    print("hello")

afterDecoration = myDecorator(sayhello)
afterDecoration()

""" the decorator function accept a function parameter
    it takes that functoin and decorate it according to
    the nested function rules
    so when you call the function sayhello() it will not get
    executed immediately as you called it using the decorator
    so decorator rules will applied first
    so first it's gonna print "before" then the function will be 
    executed and then "after" will be printed then the whole thing
    will be returned as a function
"""

# instead of writing these two lines:
afterDecoration = myDecorator(sayhello)
afterDecoration()
# you can simply just write above the say hello function 
# @myDecorator and call the function normally

@myDecorator
def sayhello():
    print("hello")

sayhello()

# if your fuction takes an argument then the wrapper function
# should take the same parameters if you want to use them in 
# your function call

def myDecorator(func):
    def nestedFunc(num1, num2):
        if num1 < 0 or num2 < 0:
            print("be aware one of the numbers is less than zero")
        func(num1, num2)  
    return nestedFunc

def decoratorTwo(func):
    def nestedFunc(num1, num2):
        print("from decorator two")
        func(num1, num2)
    return nestedFunc

@myDecorator
@decoratorTwo
def calculate(n1, n2):
    print(n1 + n2)

calculate(10, 20)