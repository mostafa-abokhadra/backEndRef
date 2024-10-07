- to access post request information
```js
app.use(express.urlencoded({extended: true}))
req.body.tagName
```
- to redirect
```js
res.redirect("newroute")
```