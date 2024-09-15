### characters in binary format
- we know that in order for the computer to deal with the data it should convert it first to the binary representation.
- numbers can be converted easily to binary and vice versa

**But what about cahracters and strnigs?**
- well, it's very simple as well, computer convert the cahracter to a number first then convert that number to it's binary format, the number of a character is called <mark>characterCode</mark>
```js
// type in the browser console
'V'.charCodeAt() // 86 (it use Unicode character set)
```

**But still how does the computer knows which number to assing for a given character?**
- it does that using <mark> Character sets </mark> which is a predefined lists of characters represented by numbers
- there is so many character sets that we can use but the most popular are <mark> ASCII and Unicode</mark>