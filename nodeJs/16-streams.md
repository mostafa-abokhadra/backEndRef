### Streams
- revies stream and buffer file-12
- steams is infact a built-in module that inherits from the event emitter calss
- we rarely use streams directly, other modules internally use streams for their functioning
- fs module uses streams to read and write data

### Example
- we will create 2 files, <mark>file1.txt and file2.txt</mar> and then we will transfere file1 content to file2

```js
const fs = require("node:fs")
```

### createReadStream()
- to read data we use <mark>readable stream</mark> using createReadStream()
- it accept the <mark>filePath</mark> and an <mark>Options-Object</mark>
```js
const readableStream = fs.createReadStream("./file.txt", {
    encoding: "utf-8"
})
```
- this readable stream now will read data in chunks from file.txt



