### comparison operators (31-)
```js
100 == "100" // true, because it's compare value only not datatypes
10 != "10" // false
100 === 100 // false, called identical operator 
            // it compares both the value and type 
10 !== "10" // true

// others
>, >=, <, <=
```

### easy interview question
```js
console.log('mostafa' === 'abokhadra') // false
// add to the above code w/o changing any existing code
// so the results become true
console.log(typeof 'mostafa' === typeof 'abokhadra');
```

### logical operators
```js
// not operator (!)
!true // false
!(10 == "10") // flase
// others
&&, ||
```