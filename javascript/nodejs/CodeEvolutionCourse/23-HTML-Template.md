- all previous way to send html files is good for static files, but what if we want to send dynamic html file?

### String replacement
- the basic method to inject some dynamic value into html file
```html
<h1>hello {{name}}</h1>
```
```js
const name = "mostaf abokhadra"
const html = fs.readFileSync("./index.html", "utf-8")
html = html.replace("{{name}}", name)
res.end(html)
```