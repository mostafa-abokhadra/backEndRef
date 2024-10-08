### setup method
- some parts of test cases can be repetitive. Luckily, we can factor out set-up code by implementing a method called setUp(), which the testing framework will automatically call for every single test we run:
```py
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
```

> [!NOTE]
> In Python’s `unittest` framework, the order in which test methods are run is based on the alphabetical sorting of the method names (as strings). This is an important detail because it might affect the behavior of your tests, especially if your tests are not independent of each other.

##### How It Works:

- When you create test methods in a class that inherits from `unittest.TestCase`, `unittest` will run them in the order determined by sorting the method names alphabetically.
- This sorting is done based on the built-in string ordering in Python, which means it follows standard lexicographic (dictionary) order.

##### Example:

```python
import unittest

class ExampleTest(unittest.TestCase):
    def test_b(self):
        print("Running test_b")

    def test_a(self):
        print("Running test_a")

    def test_c(self):
        print("Running test_c")

if __name__ == '__main__':
    unittest.main()
```

In this case, although the methods are defined in the order `test_b`, `test_a`, `test_c`, they will be executed in the following order:

1. `test_a`
2. `test_b`
3. `test_c`

This is because the method names are sorted alphabetically: `test_a` < `test_b` < `test_c`.

### Why Does This Matter?

1. **Independence of Tests**: In unit testing, it is best practice for each test to be independent of the others. However, if your tests depend on a specific execution order (which is usually discouraged), the built-in string sorting might affect your results.

2. **Test Naming Conventions**: The order of execution might be important for some tests, so you might want to control the order by using a specific naming convention (e.g., numbering the test methods like `test_01_something`, `test_02_another`).

3. **Unexpected Behavior**: If you’re not aware of the string sorting, you might get unexpected test execution orders, which could lead to confusion during debugging.

### Customizing Test Order

If you need more control over the order of your test methods, you can either:
- Use a naming convention that aligns with the order you want.
- Use a test suite to explicitly define the order.

### Summary

- `unittest` determines the order of test execution by sorting the test method names as strings.
- The default sorting is alphabetical (lexicographic).
- Test independence is crucial to avoid order-related issues.
- For more control, you can name your tests strategically or use a test suite.

Understanding this default behavior helps ensure that your test execution order does not unintentionally affect your test results.

### tearDown()
- Similarly, we can provide a tearDown() method that tidies up after the test method has been run:
```py
mport unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
```
- If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.

Such a working environment for the testing code is called a test fixture. A new TestCase instance is created as a unique test fixture used to execute each individual test method. Thus setUp(), tearDown(), and __init__() will be called once per test.

- there is also setUpClass(), tearDownClass(), setUpModule(), tearDownModule()