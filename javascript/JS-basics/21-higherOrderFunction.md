## Higher order function
- a function that takes a function as a parameter, this parameter function can contain parameter itself, or it can return a function

## map
- it creates a new array from an existing array without changing original array
- it accept 2 parameters a callback function, and **this** parameter
- the callback function accept 3 parameters, the first param is manadatory and contains the element value itself, the second and 3rd params are optional, theser are the index and the array reference

```js
const nums = [1, 2, 3]
const resultedArray = nums.map((element, index, arr) => {
  return element + element 
})
console.log(resultedArray) // [2, 4, 6]
```

> [!TIP]
> you can convert a string to an array by using splilt e:i `string.split("")`

```js
// convert small to capital and capital to small
const name = "MosTAfA"
const result = name.split("").map((element, index) => {
  if (name.charCodeAt(index) >= 65 && name.charCodeAt(index) <= 90) // upercase range
    return String.fromCharCode(name.charCodeAt(index) + 32) // or
    // return element.toLowerCase()
  if (name.charCodeAt(index) >= 97 && name.charCodeAt(index) <= 122) // lowercase range
    return String.fromCharCode(name.charCodeAt(index) - 32) // or
    // return element.toUpperCase()

// or best solution
  return element === element.toUpperCase() ? element.toLowerCase() : element.toUpperCase();
}).join("")
console.log(result)
```
