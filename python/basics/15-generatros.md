### generators
- normal function that use yield key word instead of return
- it supports iteration and return generator iterator by calling yeild
- generator can have one or more yield
- by using next() it resumes from where it stoped in the last call not from start
- when called, it will not start automatically it only gives you the control
```python
def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

myGen = myGenerator()
print(next(myGen)) # 1

for number in mygen: # this loop will resume from where next() stoped
                     # you already used next for the first element, so for 
                     # loop will start from the second
    print(number)
for num in myGenerator():
    print(num)
```