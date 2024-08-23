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
### mock
- **unittest.mock**: It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
```bash
 pip install mock
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


### pytest
- py.test is a no-boilerplate alternative to Python’s standard unittest module.
- Despite being a fully-featured and extensible test tool, it boasts a simple syntax. Creating a test suite is as easy as writing a module with a couple of functions
```bash
 pip install pytest
```
```python
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```
```bash
# then running the py.test command:
py.test
```
- is far less work than would be required for the equivalent functionality with the unittest module!

### Hypothesis
- Hypothesis is a library which lets you write tests that are parameterized by a source of examples. It then generates simple and comprehensible examples that make your tests fail, letting you find more bugs with less work.
```bash
pip install hypothesis
```

### tox
- tox is a tool for automating test environment management and testing against multiple interpreter configurations.
```bash
pip install tox
```
