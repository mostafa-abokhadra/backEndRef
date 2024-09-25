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
})
app.post()
app.put()
app.patch()
app.delete()
```
