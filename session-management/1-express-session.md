### express-session
- it is a nodeJs module
```bash
npm install express-session
```
```js
const session = require('express-session');
```

> [!NOTE]
> - Session data is not saved in the cookie itself, just the <mark>session ID</mark>. Session data is stored server-side.
> - Since version 1.5.0, the cookie-parser middleware no longer needs to be used for this module to work. This module now <mark>directly reads and writes cookies on req/res</mark>. Using cookie-parser may result in issues if the secret is not the same between this module and cookie-parser.

> [!causion]
> the default server-side session storage is <mark>MemoryStore</mark>, is purposely not designed for a production environment. It will leak memory under most conditions, does not scale past a single process, and is meant for debugging and developing.

Here's a breakdown of the warning:

1. **Memory leaks**: MemoryStore keeps all session data in the server's memory (RAM). Over time, as more sessions are created and the data increases, it will consume more and more memory without releasing it effectively. This causes a **memory leak**, where memory usage grows without being cleaned up, eventually leading to crashes or performance issues.

2. **Not scalable**: Since MemoryStore operates within a single process (or instance) of your web server, it's not suited for applications that need to scale across multiple processes or servers. If you have a multi-server setup or need horizontal scaling (where multiple servers share the workload), MemoryStore won't be able to handle it, because sessions stored in one process won’t be available to another.

3. **Meant for debugging and development**: The MemoryStore is intended for local testing or development environments where performance, scalability, and memory issues aren't as critical. It's easy to set up and use during development, but when you move to a production environment, you need a more reliable solution that doesn't leak memory and can work across multiple servers or processes.

### In production:
Instead of using **MemoryStore**, you would typically use more robust session storage solutions, such as:
- **Redis**: An in-memory data store that supports scalability and persistence.
- **Database-backed sessions**: Storing session data in a database like PostgreSQL or MySQL.
- **File-based sessions**: Storing sessions on disk.

### option
- express-session accepts these properties in the <mark>options object</mark>.

### cookie
- Settings object for the session ID cookie.
- The default value is `{ path: '/', httpOnly: true, secure: false, maxAge: null }`
- **another options can be set in this object**
    - **cookie.domain**
Specifies the value for the Domain Set-Cookie attribute. By default, no domain is set, and most clients will consider the cookie to apply to only the current domain.