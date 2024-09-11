### Json (js object Notation)
a data interchange format commonly used with web servers
```json
// data.json
{
    "name": "mostafa",
    "lastName": "abokhadra"
}
```
```mjs
// main.js
const data = require("./data")
console.log(data);
```
> [!NOTE]
> require function first search for data.js if not found search for data.json, so it's best practice to always include .json extension when you try to import json file