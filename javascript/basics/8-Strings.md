### String methods

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