### unittest
- Creating test cases is accomplished by subclassing unittest.TestCase.
```python
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
```

### Doctest
- The doctest module searches for pieces of text that look like interactive Python sessions in docstrings.
- Doctests have a different use case than proper unit tests: they are usually less detailed and don’t catch special cases or obscure regression bugs. They are useful as an expressive documentation of the main use cases of a module and its components. However, doctests should run automatically each time the full test suite runs.
```python
def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```
When running this module from the command line as in python module.py, the doctests will run and complain if anything is not behaving as described in the docstrings.
