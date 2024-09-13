### Call-Backs
- in js functions are first class objects
- a function can be passed as an argument to a function
- a function can also be returned as values from other functions
- any function that is passed to another function is called <mark>a call back function </mark> in js
- a function that is accept a function as its argument or returns another function is called <mark>higher order function</mark>

```js
function greet(name) {
    console.log(`Hello ${name}`);
}
function higerOrderFunction(Callback) {
    callback("mostafaAbokhadra")
}
higherOrderFunction(greet)
```