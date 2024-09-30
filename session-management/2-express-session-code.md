### express-session-code
```bash
npm install express-
npm install uuid
```
```js
const session = require("express-session")
const uuid4 = require("uuid").V4
```
```js
app.use(session({
  genid: function(req) {
    return genuuid() // use UUIDs for session IDs
  },
  secret: 'keyboard cat'
}))
```