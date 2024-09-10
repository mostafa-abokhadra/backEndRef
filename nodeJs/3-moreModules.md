### import export patterns

1. **single function**
```js
module.exports = functionName;
```
2. **single function short**
```js
module.exports = (a, b) {
    return a + b
}
// then const add = require('./add')
```
3. **more that one function**
```js
// math.js
module.exports = {
    add: add,
    subtract: subtract
}
```
in latest ECMA you can just specify the function name if the key and the value are the same
```js
// math.js
module.exports = {
    add,
    subtract
}
// index.js
const math = requrire("./math")
math.add()
math.subtract()
```
> [!NOTE]
> when we use module.exports we basically attaching properties to export object that exists on every module