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

app.post()
app.put()
app.patch()
app.delete()