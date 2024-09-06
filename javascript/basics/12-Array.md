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

##### indexOf()
- returns the index of the first occurance of element
- you can also specify the starting searching position
```js
myArr.indexOf("mostafa", 3)
```

##### lastIndexOf()
- start searching from behind
```js
myArr.lastIndexOf("value", -2)
```

##### include()
- return true if element exists
- also accept starting searching position
```js
myArr.include("abokhadra", 6)
```

#####
```js
```

#####
```js
```