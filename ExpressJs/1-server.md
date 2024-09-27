### Express server
```js
const express = require('express')
const app = express()
app.listen(3000)
```
- when we call express function we created an application which allows us to set up our entire server, the above code has zero routes
- to create new routes
```js
app.get('/path', (req, res) => {
    // code whenever we are trying to access '/'
    res.sendStatus(500)
    res.status(500).send("error")
    res.status(500).json({error: "500"})
    res.send("hi")
    res.json({})
    res.download("fileForUserToDownload")
    res.render('filePath.html') // all your html files should be in views folder
})
```
- for render to work install view engine either ejs or pug
```bash
npm i ejs
```
```js
app.set('veiw engine', 'ejs')
```
- and now name your html files with the extension .ejs instead of .html
- install EJS language support in Vs
- you can pass data with render to your views
```js
res.render('index', {name: "mostafa abokhadra"})
```
- in you .ejs file
```html
<% name %>
```
- if name is not defined you will get an error, so instead use 
```html
<% locals.name || "default" %>
```
- create folder named <mark>routes</mark> and inside create routes related to something in separate files

### Routers
- router works exactly as you 
```js
//users.js
const express = require("express")
const router = express.Router()
// routes related to users
router.get("/users", (req, res)=>{})
router.get("/users/new", (req, res)=>{})
moudle.exports = router
// in the bottom of your server file
// const userRouter = require('./routes/users')
// to link all these routes
app.use('/users', userRouter)
```
instead of always write users before each route e:g users/new, users/delete etc.. , you can simply just type the after user part e:i /new or /delete and the router will know that it is users route from your file name

```js
router.get("/users/:id", (req, res) => {})
res.send(`get user ${req.params.id}`)
```

- to specify deferent method for the same route
```js
router.route("/:id").get("getcodeNormally").put("putcode").delete()
```

- to run specific code whenever certain paramter is send with the request
- you should call next() function after your code
```js
router.param("id", (req, res, next, id) => {
    // code
    next()
})
```

- to access post request information
```js
app.use(express.urlencoded({extended: true}))

req.body.tagName
```
app.post()
app.put()
app.patch()
app.delete()

### Ref
[express](https://www.youtube.com/watch?v=SccSCuHhOw0)