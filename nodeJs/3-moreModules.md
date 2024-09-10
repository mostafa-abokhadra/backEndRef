### import export patterns
```js
// 1
module.exports = functionName;

// 2

module.exports = (a, b) {
    return a + b
}
// then const add = require('./add')

// 3, to import more than one function
module.exports = {
    add: add,
    subtract: subtract
}
// in latest ECMA you can just specify the function name if the key and the value are the same
module.exports = {
    add,
    subtract
}
```