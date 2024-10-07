### iterable
- the object contains data that can be iterated through
- e:g list, set, string, tuple, dictionary

### iterator
- object (like a pointer) used to iterate over iterable using next() method that return 1 element at a time
- you can generate iterator for the iterable using iter() method
- for loop already call iter() on ther iterable behind the scene
- when there is no next elements it gives StopIteration
- it's almost like c++ iterator but in a python easy way

```python
myString = "mostafa" # iterable
iterator = iter(myString)
print(next(myString)) # m
print(next(mystring)) # o

for letter in "bokhadra":
# is the same as
for letter in iter("bokhadra"):
```

**if you want to implement iteration logic for you class**
```python
# define these two methods
__iter__
__next__
```

### Ref
[w3s](https://www.w3schools.com/python/python_iterators.asp)
[elzro](https://youtu.be/MwBk42xwjjA?si=zX8oKN24slWSVupz)