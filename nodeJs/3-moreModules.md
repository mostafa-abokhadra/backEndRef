### import export patterns
```js
// 1
module.exports = functionName;

// 2

module.exports = (a, b) {
    return a + b
}
// then const add = require('./add')

//3
```