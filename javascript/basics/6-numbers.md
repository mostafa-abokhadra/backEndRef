### Numbers (23-24)

```js
console.log(1000000)
console.log(1_000_000) // syntactic sugar to facilitate reading
// still producing same output 1000000
console.log(1e6) // one then 6 zeroes
```

### MAX INTEGER
```js
console.log(Number.MAX_SAFE_INTEGER)
console.log(Number.MAX_VALUE) // you can't add on it
```

### Number methods

##### toString()
```js
(100).toString()
(100.45.toString())
```
##### toFixed()
```js
(100.11342.toFixed(2)) // returns a string -> 100.11
```
##### parseInt() and parseFloat()
```js
parseInt("100 mostafa") // returns integer from the number in the string -> 100
parseInt("mostafa100abokhadra") // NaN
parseFloat("100.500")
```
##### isIntegeer() and isNaN()
```js
Number.isInteger(100) // true
Number.isNaN("mostafa" / 20) // true
```