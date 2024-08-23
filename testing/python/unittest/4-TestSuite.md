# TestSuite
- It is recommended that you use TestCase implementations to group tests together according to the features they test. unittest provides a mechanism for this: the test suite, represented by unittest’s TestSuite class. In most cases, calling unittest.main() will do the right thing and collect all the module’s test cases for you and execute them
- a TestSuite is a collection of test cases, test suites, or both. It allows you to group multiple test cases and suites together and run them as a single entity. This is useful when you want to control the order in which tests are executed or combine tests from different modules.
- a TestSuite is essentially a container that can hold multiple TestCase instances (individual test methods), other TestSuite instances, or both. When you run a TestSuite, all the contained tests are executed <mark>in the order they were added to the suite</mark>.

### Key Concepts and Components

1. **TestCase**: Represents an individual test method, typically defined by inheriting from `unittest.TestCase`. Each test method starts with `test_`.
2. **TestSuite**: A collection of test cases or other test suites. You can define a `TestSuite` to bundle a specific group of tests together.
3. **TestLoader**: A utility provided by `unittest` to automatically find and load tests from a test module or directory.
4. **TextTestRunner**: Runs the tests in a `TestSuite` and outputs the results to the console.

### Creating and Using a `TestSuite`

You can manually create a `TestSuite` by adding test cases one by one. Here’s an example:

```python
import unittest

class ExampleTest1(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 1)
    
    def test_two(self):
        self.assertEqual(2, 2)

class ExampleTest2(unittest.TestCase):
    def test_three(self):
        self.assertTrue(True)
    
    def test_four(self):
        self.assertFalse(False)

# Creating a TestSuite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ExampleTest1('test_one'))
    suite.addTest(ExampleTest1('test_two'))
    suite.addTest(ExampleTest2('test_three'))
    suite.addTest(ExampleTest2('test_four'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

### Automatically Loading Tests into a `TestSuite`

You can also use the `TestLoader` to automatically discover and load tests:

```python
def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Automatically load all tests from ExampleTest1 and ExampleTest2
    suite.addTests(loader.loadTestsFromTestCase(ExampleTest1))
    suite.addTests(loader.loadTestsFromTestCase(ExampleTest2))
    
    return suite
```
<mark>This method is more scalable, especially when you have many test cases.</mark>

### Combining Multiple `TestSuites`

You can combine multiple `TestSuites` into a larger suite:

```python
def master_suite():
    suite1 = suite_example_test1()
    suite2 = suite_example_test2()
    master = unittest.TestSuite([suite1, suite2])
    return master
```

### Running a `TestSuite`
You can run a `TestSuite` using:

```python
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(master_suite())
```

### Use Cases for `TestSuite`

1. **Controlling Test Order**: If the order of test execution is important (e.g., tests rely on a specific sequence), you can explicitly define the order in a `TestSuite`.
2. **Grouping Related Tests**: You might want to group tests by functionality (e.g., authentication tests, database tests) into separate suites.
3. **Selective Test Execution**: Instead of running all tests, you can define a `TestSuite` to run only a subset of tests, which is useful during development.
4. **Combining Tests Across Modules**: You can create a suite that combines tests from multiple modules or packages, allowing you to structure your tests more flexibly.

### Summary

- A `TestSuite` is a container for organizing and running multiple tests together.
- You can manually add tests to a `TestSuite` or automatically load them using `TestLoader`.
- `TestSuite` is useful for controlling test execution order, grouping related tests, and combining tests across different modules.
- Suites are run using a `TestRunner`, usually `TextTestRunner`.

Using `TestSuite` gives you greater control over how your tests are structured and executed, which is beneficial as your test suite grows in complexity.

> [!NOTE]
> In some cases, the existing tests may have been written using the doctest module. If so, doctest provides a `DocTestSuite class` that can automatically build unittest.TestSuite instances from the existing doctest-based tests.