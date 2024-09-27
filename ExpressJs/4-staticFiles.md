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
Express looks up the files in the order in which you set the static directories with the express.static middleware function.
> [!NOTE]
> NOTE: For best results, use a <mark>reverse proxy</mark> cache to improve performance of serving static assets.

### virtual path
To create a virtual path prefix (where the path does not actually exist in the file system) for files that are served by the express.static function, specify a mount path for the static directory, as shown below:
```js
app.use('/static', express.static('public'))
```
Now, you can load the files that are in the public directory from the /static path prefix.