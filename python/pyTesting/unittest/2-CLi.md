### unittest
-  It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

> [!IMPORTANT]
> 1. **test fixture**: A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
> 2. **testcase**: is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
> 3. **test suite**: is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
> 4. **test runner**: A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

### CLI
The unittest module can be used from the command line to run tests from modules, classes or even individual test methods:
```bash
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
python -m unittest tests/test_something.py
```
> [!NOTE]
> This `python -m unittest tests/test_something.py` allows you to use the shell filename completion to specify the test module. The file specified must still be importable as a module.
> that is because the way this work is by convertint the path to a module name by removing the ‘.py’ and converting path separators '/' into '.',  If you want to execute a test file that isn’t importable as a module you should execute the file directly instead.

**explaination**
When you use the command:
```bash
python -m unittest tests/test_something.py
```
Here’s what’s happening:
1. **`python -m unittest`**: This runs Python’s built-in `unittest` module as a script. The `-m` option tells Python to run a module as if it were a script.
2. **`tests/test_something.py`**: This is the path to the test file. The command allows you to specify the file using shell filename completion, making it easier to select the test file from your directory structure.
3. **Module Importation**: The specified file must be importable as a Python module. The path is automatically converted into a module name:
   - The `.py` extension is removed.
   - Any directory separators (like `/` or `\`) are replaced with dots (`.`), treating it as a package/module structure.
For example, `tests/test_something.py` would be treated as the module `tests.test_something`.
4. **Why Must It Be Importable?**: The file needs to be importable because `unittest` imports and loads the test modules to discover and run the test cases inside.
### Non-Importable Test Files
If the file is not structured like an importable module <mark>(for instance, if it’s located in a directory that isn’t a Python package or has unconventional file paths)</mark>, the conversion to a module name might fail. In such cases, you can run the file directly like this:
```bash
python tests/test_something.py
```
This bypasses the module import and runs the test file directly as a script, allowing you to avoid any issues related to module import paths.

### TestDiscovery
Test discovery in Python’s unittest framework is a feature that automatically finds and runs test cases within your project. It is especially useful when you have multiple test files and want to run them all without specifying each one individually.

**it works when you simply run**
```bash
python -m unitest discover # or
python -m unitest
```
##### Default Behavior
- **Search Directory**: By default, the discover command looks in the current directory (where you run the command).
- **Pattern Matching**: The discovery process looks for files that match the pattern test*.py (e.g., test_example.py, test_something.py).
- **Test Case Identification**: Inside each matching file, unittest looks for classes that inherit from unittest.TestCase. Within those classes, it identifies methods that start with the prefix test as individual test cases.
##### Customizing Test Discovery
You can customize the test discovery process by specifying the directory, pattern, and other options. For example:

```bash
python -m unittest discover -s tests -p "test_*.py"
```
1. **-s tests**: Specifies the start directory where the discovery should begin, Traverse the tests directory and its subdirectories. Here, it’s the tests directory.
2. **-p "test_.py"**: Defines the pattern for test file names. The default is test*.py, but you can customize it to anything like test_*.py, etc.
