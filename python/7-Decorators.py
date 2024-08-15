# function are objects
# decorator take a function and add some functionality and returns it
# it is a higher order function(function accept function as parameter)


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