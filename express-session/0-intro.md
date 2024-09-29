### express-session
- it is a nodeJs module
```bash
npm install express-session
```
```js
const session = require('express-session');
```

> [!NOTE]
> Session data is not saved in the cookie itself, just the <mark>session ID</mark>. Session data is stored server-side.