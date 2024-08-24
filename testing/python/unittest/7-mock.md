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

### unittest.mock
- . It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
