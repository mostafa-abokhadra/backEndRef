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
  // store: RedisStore({client: redisClient})
  secret: 'MYSECRET',
  saveUninitialized: false,
  cookie: {
    secure: false, //convert to true in production
    httpOnly: true,
    MaxAge: 24 * 60 * 60
  }
  }))
```