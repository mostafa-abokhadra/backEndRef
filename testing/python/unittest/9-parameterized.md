# parameterized 

Parameterized testing is a technique in unit testing that allows you to run the same test with different sets of input data. This is useful when you want to test a function or method with a variety of inputs to ensure it behaves as expected in different scenarios, without writing multiple test methods.

### Why Use Parameterized Tests?
- **Efficiency**: Instead of writing multiple test cases for each input scenario, you can write a single test case and supply different inputs.
- **Readability**: Keeps your test code clean and less repetitive.
- **Maintainability**: Easier to add or change test cases by modifying the input data rather than duplicating code.

### How to Parameterize Tests in Python's `unittest` Framework

Python's `unittest` framework does not have built-in support for parameterized tests, but you can achieve this using external libraries like `parameterized` or `ddt`. 

#### Example Using the `parameterized` Library

First, you need to install the `parameterized` library if you haven't already:

```bash
pip install parameterized
```

Then, you can write a parameterized test like this:

```python
import unittest
from parameterized import parameterized

# A simple function to test
def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    
    @parameterized.expand([
        ("positive_numbers", 1, 2, 3),
        ("zero_and_positive", 0, 5, 5),
        ("negative_numbers", -1, -1, -2),
        ("mixed_signs", -1, 1, 0),
    ])
    def test_add(self, name, a, b, expected):
        result = add(a, b)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
```

#### Breakdown of the Code:
- **`@parameterized.expand([...])`**: This decorator is used to supply different sets of parameters to the test method. Each tuple in the list represents a set of parameters, where the first element is usually a name or description, followed by the inputs and the expected output.
  
- **Test Method (`test_add`)**: The method `test_add` is called multiple times, once for each tuple provided to the `@parameterized.expand` decorator. The inputs `a`, `b`, and the `expected` result are passed as arguments to the method.

- **Assertions**: Inside the test method, we use `self.assertEqual` to check if the result of `add(a, b)` matches the expected output.

#### Example Using the `ddt` Library

Another popular library is `ddt` (Data-Driven Tests), which works similarly.

First, install the `ddt` library:

```bash
pip install ddt
```

Then, you can write your parameterized test like this:

```python
import unittest
from ddt import ddt, data, unpack

@ddt
class TestAddFunction(unittest.TestCase):

    @data(
        (1, 2, 3),
        (0, 5, 5),
        (-1, -1, -2),
        (-1, 1, 0)
    )
    @unpack
    def test_add(self, a, b, expected):
        result = add(a, b)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
```

#### Breakdown of the Code:
- **`@ddt`**: This decorator is applied to the test class, indicating that the class contains data-driven tests.
- **`@data(...)`**: This decorator is used to supply the different sets of data to the test method.
- **`@unpack`**: This decorator is used to unpack the tuples provided by the `@data` decorator into individual arguments for the test method.

### Advantages of Parameterized Tests:
- **Reduce Redundancy**: Allows you to avoid writing multiple test methods for similar tests.
- **Focus on Data**: Makes it easier to focus on the different inputs and expected outputs, rather than the test logic itself.
- **Easier to Maintain**: You can add, remove, or modify test cases by simply altering the input data.

### When Not to Use Parameterized Tests:
- When each test requires a completely different setup.
- When test cases have highly complex and varied logic.

### Summary
Parameterized testing in `unittest` helps you efficiently test functions with multiple inputs without writing repetitive code. By using libraries like `parameterized` or `ddt`, you can make your tests cleaner and more maintainable, focusing on the data rather than the repetitive structure of similar test cases.

> [!NOTE]
> because unittest does not support test decorators, only tests created with @parameterized.expand will be executed

Here are a few additional important points to consider when using parameterized tests with Python's `unittest` framework:

### 1. **Parameterized Setup and Teardown Methods**
   - If your tests involve complex setup and teardown processes (e.g., creating mock objects, setting up a database connection), parameterized tests can still work effectively. You just need to ensure that your setup and teardown methods (`setUp` and `tearDown`) are robust enough to handle different inputs.
   - You might need to parameterize the setup itself if different parameters require different initial setups.

### 2. **Handling Edge Cases and Exceptions**
   - Parameterized tests can also be used to ensure your code correctly handles edge cases and raises exceptions as expected. You can include test cases that pass invalid or extreme input values to verify that the function under test behaves as intended.
   - For example, testing a function's response to `None`, empty strings, or very large numbers.

### 3. **Combining Parameterized Tests with Test Fixtures**
   - In some cases, you might want to use test fixtures (like `unittest.TestCase`’s `setUpClass` or `setUpModule`) in conjunction with parameterized tests. Ensure that your fixtures are designed to work with multiple test cases or that they don’t interfere with the parameterized inputs.

### 4. **Naming Conventions and Clarity**
   - When using parameterized tests, especially with the `parameterized` library, it's helpful to provide descriptive names for each test case. This makes it easier to identify which specific input set is causing a failure if one occurs.
   - Good naming conventions help make the test output more readable and help with debugging.

### 5. **Dealing with Large Data Sets**
   - If you have a large number of parameterized test cases, consider organizing your input data into separate functions or data structures for readability and maintainability.
   - You can dynamically generate test data, especially if your inputs follow a predictable pattern or are derived from external sources like a CSV file.

### 6. **Debugging Parameterized Tests**
   - Debugging parameterized tests can sometimes be tricky, especially if you're dealing with complex input data. Make sure your test framework's output is clear about which parameters were used in failing tests. Libraries like `parameterized` allow you to name your test cases, which can aid in debugging.

### 7. **Custom Parameterized Decorators**
   - In cases where you have special requirements, you can write your custom parameterized decorators. This is useful if the available libraries don't fully meet your needs or if you want more control over how parameters are handled.

### 8. **Interdependencies Between Parameters**
   - If the parameters you're testing are interdependent (meaning one parameter affects how another should be tested), you need to be careful in how you design your test cases. Ensure that each test case is isolated and doesn't create side effects that might affect subsequent tests.

### 9. **Testing Performance with Parameterized Tests**
   - If you're using parameterized tests to test performance (e.g., how quickly a function runs with different inputs), be mindful of the potential for increased test duration. Parameterized tests can lead to a significant increase in the number of test executions, so make sure your test suite remains efficient.

By keeping these points in mind, you'll be better equipped to leverage parameterized testing in Python's `unittest` framework effectively, ensuring your tests are thorough, maintainable, and efficient.