# elzero 1 - 10
# it can do anything :)
"""
    web: django, flask
    games: pyGame
    desktop apps: pyGUI, Tkinter
    Hacking
    machine learnings, data science
    ai, robots
    automation of tasks
    web scrapping (harvest)
    android games
"""
# interpreted meaning the code is processed in run time
# so no need for comile first like c lang for example, etc..
# pyCharm is an IDE for python that you can use like VS

# to run python file -> /bin/python filename.py or python filename.py 
# or ./filename.py # but your file should include #!/usr/bin/python3
# at the first line or better #!/use/bin/env python3

# the only case that you can use semicolon in python is
# when you write multiple commands at the same line
print("hello mostafa ",end=""); print("abokhadra:)") # hello mostafa abokhadra:)
# normally print function add a new line automatically ,
# to disable this we use end=""

# comments
# using # symbol
# note that """ """ is not a multiple line comment!
# it's just a string that is not assigned to any var
# so it act as a multiple line comment

# variables not containing the data it's only refer
# or point to it's location in the memmory
# all data in python is objects
# int, float, str, bool, tuple, set, list, dict
myName = "mostafa" # camelCase
my_name = "mostafa" # snake_case
a, b, c = 1, 2, 3
# it's a dymamically typed lang meaning you can change data
# types in the run time
help("keywords") # will show you all reserved keywords of the 
# lang, you can't name your var the same name as any of these
type(myName) # str