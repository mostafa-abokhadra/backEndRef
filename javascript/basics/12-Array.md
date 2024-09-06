### Array (40)
```js
let myArr = ["mostafa", "abokhadra", [1, 2, 3]]
myArr[index] // myArr[0][2] 
myArr[2] = "newValue"
myArr[0] = [1, 2, 3]
typeof myArr // Object
Array.isArray(myArr) // true

// if you have an array that has 3 element
// and you insert a value in the position number 7
// now your array length is 8 and the precceding positions are empty
myArr.length
// you can use length to append at the end
myArr[myArr.length] = "newValue"
// you can also specify your array length
// even if it's larger
myArr.length = length
```

### Array methods

##### unshift()
- accept one or more values to add in front
```js
myArr.unshift("value", "anotherValue")
```

##### push()
- add to end
```js
myArr.push("value")
```

##### shift()
- remove first element and returns it
```js
myArr.shift()
```

##### pop()
- remove last element and returns it
```js
myArr.pop()
```

#####
```js
```

#####
```js
```

#####
```js
```

#####
```js
```

#####
```js
```