### Built-in Modules (core default)

#### some of the most common Built-in modules
1. Path
2. events
3. fs
4. stream
5. http

# path
- it provide utilitis for working with file and directory paths
```js
const path = require("node:path");
```
- prefix with <mark>node:</mark> to indicate that it's a built-in module

### __filename and __dirname
- __filename is the path of current file
- __dirname is the path to dir for current file
```js
console.log(__filename)
console.log(__dirname)
```

### path.basename
- will print only the last portion of the file bath (current file name only)
```js
console.log(path.basename(__filename)) 
path.basename(__dirname)
```