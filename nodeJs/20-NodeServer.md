### Node server
- we create that using HTTP module
- http module also extends eventEmitter class
```js
const http = require ("node:http")
```
### createServer()
- it accept a call back function
- the call back accept a request and a response
- the callback function is actually a request listener
- wherever a request reaches the server this callback will be executed
- the req argument has information about the encoming request
- the server response arg we use it to build the response that will be sent back to the client
- so node will handle the request and we have to write code to send back the response
```js
http.createServer((req, res)=>{
    res.writeHead(200)
    res.end("hello world")
})
```