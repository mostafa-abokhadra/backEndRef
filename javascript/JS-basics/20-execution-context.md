## execution context
JavaScript execution context is a fundamental concept that defines the environment in which JavaScript code is executed. It plays a vital role in how JavaScript functions and interacts with its surrounding environment, and understanding it is essential to write efficient and effective JavaScript code. An execution context is a data structure that contains information about the environment in which the JavaScript code is executed.

Each execution context has a scope chain that determines what variables and functions the context has access to. The scope chain is determined by the lexical environment of the execution context and is used to look up variables and functions when code is executed.

The variable object is another important component of an execution context. It is a data structure that contains information about the variables, functions, and parameters defined in the execution context. The variable object is used to store and manage the variables and functions in the context and is updated dynamically as the code is executed.

The this keyword is also an important part of the execution context. The value of this is determined by the context in which a function is called. In the global execution context, this refers to the global object. In a function execution context, this refers to the object that the function is a method of, or the global object if the function is not a method of any object.

Hoisting is another concept that is closely related to execution context. In JavaScript, variable and function declarations are hoisted to the top of their respective execution contexts. This means that they can be used before they are declared in the code.

Finally, the execution stack is a data structure that stores execution contexts in a last-in, first-out (LIFO) order. When a function is called, a new execution context is created and pushed onto the top of the stack. When a function returns, its execution context is popped off the stack.

The execution context is a fundamental concept in JavaScript that defines the environment in which code is executed. It contains information about the variables, functions, and parameters defined in that environment, as well as the scope chain and the this keyword. By understanding the execution context, developers can write more efficient and effective JavaScript code, ultimately leading to better performance and more reliable applications.

### Ref
- [dev](https://dev.to/jahid6597/javascript-execution-context-a-deep-dive-4kno#:~:text=JavaScript%20Execution%20Context%20is%20the,creation%20phase)
- [mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model)
