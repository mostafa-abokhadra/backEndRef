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