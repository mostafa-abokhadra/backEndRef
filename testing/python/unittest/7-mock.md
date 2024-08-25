### A mock
- is an object that clone the behavior of a real object.
- is a simulated object or module that acts as a stand-in for a real object or module.
- used in testing to isolate the behavior of a particular module or component and to verify that it behaves as expected, without having to rely on the behavior of other parts of the system.
- test the isolated unit even when Backend is not available

### benefits of using mocks
1. **Improved test reliability**: help to isolate the behavior of individual modules or components, making the tests more reliable and easier to understand.
2. **Faster test execution**: do not have to wait for real objects or modules to respond.
3. **Increased test coverage**: helps to test all possible scenarios and edge cases, improving overall test coverage and helping to catch more bugs and issues.
4. **Reduced test dependencies**: help to reduce the dependencies between tests, making it easier to modify and maintain the test suite over time.
5. **Improved code quality**: 

### why we use mock object
- The unit testing purpose is to approve each unit of software designed and verify that the generated code is working perfectly, interdependent on external dependencies.
- Most of the cases, Code under test has some external dependencies like APIs, and It would be better to create a mock object instead of generating test cases on the real object of the dependencies.
- A web application consists of two components: Frontend and Backend server that are dependent on each other and run simultaneously.
- The developer of the Frontend is dependent on the backend developer for a server, APIs, and other external services.
- In the testing or development phase, a major challenge is to handle the various external dependencies.
- Real Environment exchanges their data through a server where user-end services are handled by a different server and admin services are handled by another server.
- Developer facing difficulty while developing software. On the other hand tester not able to do efficient unit testing when software is dependent on external dependencies.
- In order to provide effective testing, mock server is required. Mock server cut out the dependency on a real server and allows tester to do testing independently. Figure gives a virtual Representation of Mock server. 
[photo](https://media.geeksforgeeks.org/wp-content/uploads/20190424215004/mockgeeks1.jpg)

### pattern to be followed for Unit testing with Mock objects:
1. Build an Instance or object of Mock object.
2. Define States of Mock objects under defined environment.
3. Set expectations, status codes, responses, error display in mock object.
4. Set Mock object as parameter under domain code.
5. Verify Mock objects under unit testing.

### key feauters of mock object
1. **Mocking Objects**: It allows you to replace real objects in your code with mock objects. This is useful when you want to isolate the code you are testing from its dependencies.

2. **Simulating Behavior**: You can specify how the mock should behave, what it should return, and what side effects it should have. For example, you can mock a database call or an HTTP request so that your tests run quickly and don't depend on external resources.

3. **Making Assertions**: unittest.mock provides built-in methods for checking how a mock was used, such as checking if a method was called, how many times it was called, and with what arguments.

### unittest.mock
- It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

```py
import unittest
import requests

def add(a, b):
    return a + b

class Tests(unittest.TestCase):

    def len_joke():
        joke = get_joke()
        return len(joke)
        # this function should be refactored as it depends on get_joke()
        # instead we should pass the joke as a parameter
        # this function depends on get_joke functoin that make a call to an externl api
        # but what if the server is down? what if my internet provider is down?
        # we use mock to isolate our len_joke from it's dependencies by mocking get_joke function
        
    def get_joke():
        url = "https://usl.com"
        res = requests.get(url)
        # if res.ok: 
        # or
        if res.status_code == 200:
            joke = res.json()['somekey']
        else:
            joke = "noJokes"
        return joke

if __name__ == '__main__':
    unittest.main()
```