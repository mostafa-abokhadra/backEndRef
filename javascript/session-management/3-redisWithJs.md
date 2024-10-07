### redis with js
```bash
npm i redis connect-redis
```
```js
const redis = require("redis")
const connectRedis = require("connect-redis")
```
```js
const redisStrore = connectRedis(session)
const redisClient = redis.createClient({
    port: 6379,
    host: "localhost"
})
```
```js
// in session object use
store: redisStore({client: redisClient})
```