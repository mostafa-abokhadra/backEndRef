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

app.get('/', (req, res) => {
    res.send('Hello World')
})

app.listen(port, () => {
    console.log("listening...")
})
```