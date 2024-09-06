### Null (36)

```js
// always consider to have a default value for your data
let data = 0;
print(data || 2)
// here your data is gonna equal 2 in case of data 
// variable have any flase value e:g
// 0, null, undefined, "", flase
// if you want to know if a value is true or false
// use Boolean() constructor
Boolean(100) // true
Boolean("") // flase
```

### Nullish Coalescing operator (??)
- it has the same use case as logical or operator in the above example, but the value will be returned only if the data is undefined or null, so if the data is false it's ok it will be returned as it is
```js
let myVar;
console.log(myVar ?? 99) // 99
myVar = 0;
console.log(myVar ?? 99) // 0
myVar =""
console.log(myVar ?? 55) // ""
```