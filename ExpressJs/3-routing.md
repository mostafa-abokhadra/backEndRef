### Routing
- Routing refers to determining how an application responds to a client request to a particular endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).
- Each route can have one or more handler functions, which are executed when the route is matched.

#### syntax
```js
app.METHOD(PATH, HANDLER)
```
- app is an instance of express.
- METHOD is an HTTP request method, in lowercase.
- PATH is a path on the server.
- HANDLER is the function executed when the route is matched

### routes
```js
app.get('/', (req, res) => {
    // code
})
app.post('/signIn', (req, res) => {
    // code
})
app.put('/users/:id', (req, res) => {
    // code
})
app.delete('/users/:id', (req, res) => {
    // code
})
```