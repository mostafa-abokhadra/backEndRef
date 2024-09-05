## Introduction (1-10)

### in html page
```html
<script src=""> </script>
```
- you can add this line either in the (head tag) of html document or (at the end of the body tag)
if you put the code in the head tag you will get an error,  that is because the program is executing 
sequentially line by line, so when you put the script in the head tag it's like you are executing some code 
in an element that does not exist yet.
- so the best practice is to put it in the end of the body tag
- you can still put it in head tag if you want and use (onload event) to wait until the html page is loaded before executing js file.

###  comments
```js
// this is a comment or 
/* this is a comment */
//in the future, there is so many better way to document or
// explain your code rather than comments.
```
### outputs

we put the double or single quotes to print something because if we don't the language compiler 
will deal with the string as if it is a part of the language or a commands and will try to search 
for it in the commands list


```js
window.alert("Hello, World!"); // not used often as it stops the execution of all of the code after it, 
// instead we use popUp formated with css to demonstrate the same window.alert functionality
document.write("Hello, World!"); // not used, instead we will use createElement
document.write("<h1>Hello, World!</h1>"); // not used
console.log("hello"); // this will print in console not in page
process.stdout.write("print without newline at the end");
```

### console
```js
console.log("message")
console.error("err message") 
console.table(["neymar", "suarez", "messi"]) // print it in console as table
console.log("messi is the %cbest", "color: red") //this will be printed in the console and 
// the word "best" will be printed in color red as it is preceded by the directive '%c'
```

### dataTypes and typeof
```js
typeof "string" or typeof("string") // both syntax is correct
typeof [1, 2, 3] // it's type is object, but it's called array
Number // either int or float or double
null // it's type is object
// string, Object, boolean, undefined, bigint, symbol
```