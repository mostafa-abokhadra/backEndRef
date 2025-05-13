# scope, block, lexical(67 - 70 )
- global scope can't access local variables like: functions
- local scope can access global variables
- if condition block e:i if () {} is also local scope, if you declered some var inside it won't be accessible outside the if block
- nested functions can access the higher functions variables, but parent function can't access its childre variables

### lesson 70 challenge
```js
const names = (...names) =>  return "String " + names.map((name) => `[${name}]`).join(', ') + " => Done !"
console.log(names('mostafa', "mahmoud", "abokhadr"))
```
