# functions (57-62)
- default value of functions parameter is undefined
```js
function doSomething(name, age) {
    // default value for parameter
    if (age === undefined)
        age = 'unKnown'
    // another way
    age = age || 'unKnown'
    return `${name} ${age}`
}
// ES6 way
function doSomething(name, age='unknown'){}
```

### Rest parameter
- when you don't know how many arguments you will be passing to the function

```js
function doSomething(name, country, ...numbers) {
    console.log(Array.isArray(numbers)) // true
}
doSomething('mostafa', 'egypt', 1, 2, 3, 4, 5)
```
> [!caution]
> rest parameter must be the last parameter\
> also you can't have 2 rest parameters for the same function

### anonymous function
- normal named function can be user either before its definition or after its definition
- anonymus function should be used only after its definition otherwise an error is going to occur
```js
console.log(sum(1, 3))
function sum(n1, n2) {
    return n1 + n2
}

let calc = function (n1, n2) {
    return n1 + n2
}
console.log(calc(1, 3))
```
> [!TIP]
> - anonymous functions is mainly used when we don't need to call that function again, their only purpose to perform a speicfic task and that's it, for example thery are commonly used with event listeners and setTimeout callback 
> - Anonymous functions are useful for one-time operations, such as inline callbacks in setTimeout or event handlers, where naming the function is unnecessary.
