``` bash
npm i bcrypt
```
```js
const hashedPass = bcrypt.hashSync(req.body.password, 10)
```