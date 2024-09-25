### Routing 
- <mark>req.url</mark> gives us the query string
- we can use it with if statment to respond differently
```js
const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, "Content-Type": "text/plain")
        res.end("home page")
    } else if (req.url === "/about"){
        res.writeHead(200, "Content-Type": "text/plain")
        res.end("about page")
    }
})
```