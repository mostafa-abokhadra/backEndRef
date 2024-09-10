### Modules Scope
- each module has it's own private scope so there is not confilct when you use the same variable name in two different modules
- node js does that using IIFE (immediately invoked function expression), before a module's code is executed node js will wrap it with a function wrapper that provides module scope
```js
(function(){
    // module code actually live in here
})()
```
- you write `function(){}` then wrapped with parantheses `(function(){})` to convert it to function exepression, then adding `()` after the expression to immediately invode it, then write your code inside the `{}`
- using IIFE node can execute each module with it's own private scope

**to specify parameter and pass arguments to IIFE**:
```js
(function(param1){
    console.log(param1) // hellow
})("hello")
```