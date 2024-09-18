### promise based fs module
```js
const fs = reqire('node:fs/promises');
```
- you can add then and catch blocks
- then execute when no error occur, catch execute when error occur
```js
fs.readFile("filePath", "utf-8")
.then(data => console.log(data))
.catch(error => console.log(error))
```
