### Node server
- we create that using HTTP module
- http module also extends eventEmitter class
```js
const http = require ("node:http")
```
### createServer()
- it accepts a call back function
- the call back accept a request and a response
- the callback function is actually a request listener
- wherever a request reaches the server this callback will be executed
- the req argument has information about the encoming request
- the server response arg we use it to build the response that will be sent back to the client
- so node will handle the request and we have to write code to send back the response
- we also have to infrom our server to listen to any encoming requests, for that we store the server created using createServer() in a constant
- then on the server constant use listen mehtod passing to it a port number
```js
const server = http.createServer((req, res)=>{
    res.writeHead(200) // adding statusCode
    res.end("hello world") // end the response with
})
server.listen(3000)
```
