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