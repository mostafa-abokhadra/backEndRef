### Streams
- revies stream and buffer file-12
- steams is infact a built-in module that inherits from the event emitter calss
- we rarely use streams directly, other modules internally use streams for their functioning
- fs module uses streams to read and write data

### Example
- we will create 2 files, <mark>file1.txt and file2.txt</mar> and then we will transfere file1 content to file2

file1
```
mostafa Abokhadra
```
```js
const fs = require("node:fs")
```


