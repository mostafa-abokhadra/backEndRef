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
from unittest.mock import patch, MagicMock

def add(a, b):
    return a + b

    def len_joke():
        joke = get_joke()
        return len(joke)
        # this function should be refactored as it depends on get_joke()
        # instead we should pass the joke as a parameter
        # this function depends on get_joke functoin that make a call to an externl api
        # but what if the server is down? what if my internet provider is down?
        # we use mock to isolate our len_joke from it's dependencies by mocking get_joke function
        # from unittest.mock import patch

    def get_joke():
        url = "https://usl.com"
        res = requests.get(url)
        # if res.ok: 
        # or
        if res.status_code == 200:
            joke = res.json()['value']['joke']
        else:
            joke = "noJokes"
        return joke

class Tests(unittest.TestCase):

    @patch('get_joke')
    # takes a string parameter -> a path to the object you want to mock, e:g if the needed to mock object is in another file
    # @patch('module.get_joke')
    # the decerator patch create a special fake object a MagicMock() object and pass the reference to it to the decorated function, in this example to the mock_get_joke parameter
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one' # set the return value of the mock or fack get_jock fucntion
        self.assetEqual(len_joke(), 3)
    
    # now let's test get_joke itself as it also has dependencies
    # e:i requests.get fucntion
    @patch('requests')
    def test_get_joke(self, mock_requests):
        # mocking get function from requests
        # get function returns a response object from the response class
        # so we have to mock respons object too
        mock_response = MagicMock()
        mock_response.status_code = 200
        # json is a method that parses a json object and returns a py dictionary so return value is dictionary
        mock_response.json.return_value = {'value': {'joke': "somejoke"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'somejoke')
    
        @patch('requests')
    def test_fialed_get_joke(self, mock_requests):
         # you can pass the attributes in the constructor
        mock_response = MagicMock(status_code=404)
        # json is a method that parses a json object and returns a py dictionary so return value is dictionary
        mock_response.json.return_value = {'value': {'joke': "somejoke"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'No joke')

if __name__ == '__main__':
    unittest.main()
```

### mocking exceptions
```py
    import requests.exceptions
    from requests.exceptions import Timeout, HTTPError
    def get_joke():
        url = "https://url.com"
        try:
            res = requests.get(url, timeout=30)
            response.raise_for_status() # instead of manually checking if status_code == 200 which is not accurate
            # as there is 5 http status_code that indicate success
            # it raises HttpError exception if status_code is not successful e:i 400s or 500s
        except requests.exceptions.Timout:
            return 'No joke'
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.HTTPError:
            return 'HttpError was raised'
        else:
            if res.status_code == 200:
                joke = res.json()['value']['joke']
            else:
                joke = "noJokes"
            return joke

    @patch('requests')
    def test_raise_for_status(self, mock_requests):
        # you can pass the attributes in the constructor
        mock_requests.exceptions = requests.exceptions
        mock_res = MagicMock(status_code=403)
        mock_res.raises_for_status.side_effect = HTTPError("msg")
        mock_requests.get.return_value = mock_res
        self.assertEqual(get_joke(), 'HTTP Error was raised')
```

# Ref
- [1](https://www.youtube.com/watch?v=xT4SV7AH3G8&t=901s)
- [1](https://www.youtube.com/watch?v=RqR0AvEujrU)