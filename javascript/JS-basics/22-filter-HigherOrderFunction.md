## Filter
- it returns a new array of elements that passed certain test
- it returns the element itself
- if filters got a return value of true from the first operation in its callback function it returns the element as it is

```js
// filter people starts with the letter 'a' or 'A'
let friends = ['ahmed', 'osama', 'abeer', 'amin', 'mostafa', 'Ali', 'amer', "noha", 'noor']
const result = friends.filter((name) => {
return name.startsWith('a') || name.startsWith('A')
})
console.log(result) // [ 'ahmed', 'abeer', 'amin', 'Ali', 'amer' ]

// filetr only even numnbers
let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const even = nums.filter((num) => {
     return num % 2 === 0;
})
console.log(even)
```
