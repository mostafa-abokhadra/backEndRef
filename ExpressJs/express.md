### install
```bash
cd myApp
npm init
npm install express
```

### createServer
```js
const express = require('express')
const app = express()
const port = 300


app.listen(port, () => {
    console.log("listening...")
})
```