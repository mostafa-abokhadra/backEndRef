### String methods (27-30)

```js
let name = "mostafa"
name[0] // m
name.charAt(1) //o
name.length // 7

let lastName = "   abokhadra    "
lastName.trim() // reomove leading and trailing whiter spaces

lastName.toUpperCase() // all letters to uppercase
lastName.toLowerCase() // all letters to lowercase
lastName.trim().charAt(3).toUpperCase() // K
```

### indexOf() And lastIndexOf()
returns -1 if don't find the value
```js
let name = "mostafa abokhadra"
name.indexOf("abo") // 8
name.indexOf("abo", 9) // -1
name.indexOf("a") // 4
name.lastIndexOf('a') // 16
//it start searching from the end of the string 
```
### slice
```js
name.slice(5) // fa abokhadra
name.slice(0, 8) // mostafa
name.slice(-5, -3)
```

### Repeat()
```js
let ok = "ok"
ok.repeat(5) // okokokokok
```

### split()
```js
let name = "mostafa abokhadra"
name.split() //["msotafa", "abokhadra"]
name = "mostafa abokhadra"
name.split("") ['m', 'o', etc]
name.split("someDelimiter", "limitOfSplitting")
name = "m,o,s,t,afa"
name.split(",", 2) ['m', 'o', "s,t,afa"]
```

### substring()
```js
name.substring(2, 9)
// there is also substr()
```

### include
returns true or false
```js
name.include("abokhadra", 8) // true
```

### startsWith()
```js
name.startsWith('m') // true
```

### endsWith()
```js
name.endsWith('a') // true
```

### practice
```js
let a = "Elzero Web School"

//use above variable to solve the following questions

// output must be -> Zero
console.log(a.slice(2, 6).charAt(0).toUpperCase())

// output must be -> HHHHHHHH
console.log(a.charAt(a.indexOf('h')).toUpperCase().repeat(8))

// output must be -> //["Elzero"]
console.log(a.split(" ", 1))

// output must be -> // Elzero school
console.log(a.substr(0, 6) + a.substr(10))

// output must be first and last characters are small and the rest of the characters 
console.log(a[0].toLowerCase() + a.slice(1, -1).toUpperCase() + a.charAt(-1).toLowerCase())
```