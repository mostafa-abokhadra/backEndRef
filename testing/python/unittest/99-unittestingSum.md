### steps
- import unittest
- subclass from unittest.TestCase
- start your test functions names with test_something

### assert functions
- assertEqual(something, correctResult)
- assertTrue()
- assertFalse()
- assertRaises(typeError) # verify that a specific exception gets raised.

### setUp()
- called immediately before calling the test method
- any exception raised by this method will be considered an error rather than a test failure. 

### tearDown()
- called immediately after the test method has been called 
- called even if the test method raised an exception
- any exception raised by this method will be considered an error rather than a test failure. 
- will only be called if the setUp() succeeds, regardless of the outcome of the test method