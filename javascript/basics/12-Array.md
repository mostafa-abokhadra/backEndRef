### Array (40-47)
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

##### sort()
```js
myArr.sort()
```

##### revers()
- it reverse the array upside down (not sorting)
```js
myArr.revers()
```

### slic()
- slice returns a new array don't change the actual array
- accept start and end position both optional
```js
myArr.slice() // will slice the whole array (returns it as it is)
myArr.slice(1, 3) // slice array element in positions 1 and 2 in separate array
myArr.slice(-3) // will start slicing from position -3 to the end
myArr.slice(-4, -2)
```

### splice()
- splice add and remove
- it accept starting position, then in the second arg it accept the number of element you want to delete, and the last arg is element you want to add
```js
myArr.splice(0, 0, "val1", "val3")
// will delete 2 element starting from position 2 and add the new values in their places
myArr.splice(2, 2, "val1", "val3")
```

### concat()
- joining items and arrays
```js
myArr.concat(myArr2, myArr3, "stringValue", [1, 2, 3])
```

### join()
- it concat all array elements in one string separated by a delimeter you choose
```js
myArr.join() // default delimeter is comma ,
myArr.join("") // no separator in between
myArr.join("|")
```