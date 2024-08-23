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
[!NOTE]
> All the assert methods accept a msg argument that, if specified, is used as the error message on failure 
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
