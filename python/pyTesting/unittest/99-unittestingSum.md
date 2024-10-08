### unitTest
- test written for testing a unit of code
- one unit test runs independently of any other unit test, code, etc..
- external dependencies are managed with doubles(Mocks/Fakes/Stubs)
- should complete within milliseconds as there is a lot of unit tests for a project or a module
- unittest should be able to execute independently e:g the below code don't make any sense if it's treated as individual lines, you need minimum the two lines to test the execution
```c++
int num;
cin >> num;
```

### how to write unittests (AAA)
- each individual unittest should have: Arrange - Act - Assert
```py
from module import add
class Testing(unittest.TestCase):
    def setUp(self):
        # arrange
        self.a = 10
        self.b = 20
    
    def tearDown(self):
        self.a = 0
        self.b = 0

    def test_add():
        # act
        res = sum(n1, n2)
        # assert
        self.assertEqual(res, n1 + n2)
```
### Test Doubles
- we use them to test our code that depend on certain external responses, e:i if the database server has some problems we don't want our code to fail as the problem is in the backend not with our code, so mock server replace that for you
- used in lieu of بدلا من external dependencies
- e:g database, api, library, network connections
- easy to simulate different scenarios
- **E:g**: Mocks, Fasckes, Stubs

### Mocks
- replaces external interface
- it is not used for checking function behaviour or return values from the function call
- but it is used instead to check whether or not mock function called or not, wheter or not your function called the conncetion socket or not, how many times it gets called, it number of calls is as expected or not, what parameters are passed when it called
- so it asserts right call, right number of times with the right parameters

### steps
- import unittest
- subclass from unittest.TestCase
- start your test functions names with test_something

### assert functions
- assertEqual(a, b)
- assertNotEqual(a, b)
- assertTrue(x)
- assertFalse(x)
- assertIs(a, b) # a is b
- assertIsNot(a, b) # a is not b
- assertIsNone(x) x is None
- assertIsNotNone(x)
- assertIn(a, b) # a in b
- assertNotIn(a, b)
- assertIsInstance(a, b) # isinstance(a, b)
- assertNotIsInstance(a, b) # not isinstance(a, b)
- assertRaises(typeError) # verify that a specific exception gets raised.
- assertGreater(a, b) # a > b
- assertGreateEqual(a, b)
- assertLess(a, b)
- assertLessEqual(a, b)
- assertCountEqual(a, b) # a and b have the same elements in the same number, regardless of their order.
- assertListEqual(a, b)
- assertTupleEqual(a, b)
- assertDictEqual(a, b)
- assertSetEqual(a, b)
> [!NOTE]
> All the assert methods accept a msg argument that, if specified, is used as the error message on failure 
```
self.assertEqual(a, b, msg="a message when error occur")
```

### setUp()
- called immediately before calling the test method
- any exception raised by this method will be considered an error rather than a test failure. 

### tearDown()
- called immediately after the test method has been called 
- called even if the test method raised an exception
- any exception raised by this method will be considered an error rather than a test failure. 
- will only be called if the setUp() succeeds, regardless of the outcome of the test method

### setUpClass() and tearDownClass()
- called before tests in an individual class are run.
- called with the class as the only argument.
- must be decorated as a classmethod()
```py
@classmethod
def setUpClass(cls):
    ...
@classmethod
def tearDownClass(cls):
    ...
```
### assertRaises()
- assertRaises(exception, callable, *args, **kwds) or assertRaises(exception, *, msg=None)
Test that an exception is raised when callable is called with any positional or keyword arguments that are also passed to assertRaises(). The test passes if exception is raised, is an error if another exception is raised, or fails if no exception is raised. To catch any of a group of exceptions, a tuple containing the exception classes may be passed as exception.

### assertSequenceEqual()
- assertSequenceEqual(first, second, msg=None, seq_type=None)
- Tests that two sequences are equal. If a seq_type is supplied, both first and second must be instances of seq_type or a failure will be raised.

### test code that raises an exception
```py
def throw_ex(var):
    if var == 100:
        raise Exception("not valid")
    else:
        return True

def test_ex(self):
    self.assertRaises(Exception, throw_ex, 100)# or
    with self.assertRaises(Exception) as context:
        throw_ex(100)
    print(context.exception)

```

# Ref
- [expertRef](https://www.youtube.com/watch?v=NPp2pvhGbkM)
- [expertRef2](https://www.youtube.com/watch?v=HKTyOUx9Wf4)
- [expertRef3](https://www.youtube.com/watch?v=TKDnkQSyg2M&list=PL_dsdStdDXbodu-2ZNCdzzxQF9YkBRtwb&index=2)
- [expertRef4](https://www.youtube.com/watch?v=LxbiAHGkPhk&list=PL_dsdStdDXbodu-2ZNCdzzxQF9YkBRtwb&index=3)


