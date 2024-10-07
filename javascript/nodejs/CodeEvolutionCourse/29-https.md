### HTTPS mdoule
- it is a secure version of the http module
```js
const https = require("node:https")
```
- https.requests doesn't use the thread pool to run asynchronously
- so https.request doesn't affect by the number of CPU cores either
- that is because http.requests is a network input/output operation and not a CPU bound operation
- libuv instead delegates the work to operating system kernel and whenever possible, it will poll the kernel and see if the request has completed