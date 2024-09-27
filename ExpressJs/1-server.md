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
- to redirect
```js
res.redirect("newroute")
```
app.post()
app.put()
app.patch()
app.delete()

### Ref
[express](https://www.youtube.com/watch?v=SccSCuHhOw0)