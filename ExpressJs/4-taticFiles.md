### static files
To serve static files such as images, CSS files, and JavaScript files, use the **express.static** built-in middleware function in Express.

#### syntax
```js
express.static(root, [options])
```
For example, use the following code to serve images, CSS files, and JavaScript files in a directory named public:
```js
app.use(express.static('public'))
```
To use multiple static assets directories, call the express.static middleware function multiple times:
```js
app.use(express.static('public'))
app.use(express.static('files'))
```