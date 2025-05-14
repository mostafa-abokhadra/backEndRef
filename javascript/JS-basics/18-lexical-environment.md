# Lexical environment
- is a data structure that stores variables and functions defined in the current scope, along with references to all outer scopes. It is also known as the lexical scope.
- Lexical scope is a fundamental concept in programming that determines the accessibility of variables and functions based on where they are defined in the source code.
- In simple terms, lexical scope is the scope of a variable or function determined at compile time by its physical location in the code.
- Unlike dynamic scope, which depends on how functions are called at runtime, lexical scope is static and remains the same throughout the program's execution.

- ## scope levels
- **Global Scope**: Variables defined outside any function or block, accessible anywhere in the program.
- **Local Scope**: Variables defined inside a function or block, accessible only within that specific function or block.
- **Nested Scope**: Inner functions have access to variables in their parent functions.
- **Block Scope**: Variables defined with let and const are limited to the block they are declared in, like loops or conditionals.

The lexical environment is used to resolve variable names. When the JavaScript interpreter encounters a variable name, it first searches for the variable in the lexical environment of the current scope. If the variable is not found in the current scope, the interpreter searches the lexical environment of the outer scope, and so on.\

The interpreter continues searching the lexical environment until it finds the variable or it reaches the global scope. If the variable is not found anywhere in the lexical environment, the interpreter throws a ReferenceError exception\

### Ref
- [medium](https://medium.com/@mohdtalib.dev/lexical-environment-in-javascript-a2112b78a3cb)
