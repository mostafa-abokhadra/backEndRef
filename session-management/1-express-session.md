### express-session
- it is a nodeJs module
```bash
npm install express-session
```rser mid
```js
const session = require('express-session');
```

> [!NOTE]
> - Session data is not saved in the cookie itself, just the <mark>session ID</mark>. Session data is stored server-side.
> - Since version 1.5.0, the cookie-padleware no longer needs to be used for this module to work. This module now <mark>directly reads and writes cookies on req/res</mark>. Using cookie-parser may result in issues if the secret is not the same between this module and cookie-parser.

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
    - **cookie.secure**
    - **cookie.expires**
    - **cookie.httpOnly**
    - **cookie.maxAge**
    - **cookie.partitioned**
    - **cookie.path**

### cookie.secure NOTE
### `cookie.secure` Attribute: Explanation and Usage

The `Secure` attribute for cookies is a critical security feature that ensures cookies are only sent over **secure (HTTPS)** connections. By enabling this attribute, you protect sensitive information stored in cookies from being transmitted over unencrypted HTTP connections, which can be vulnerable to interception by attackers.

### `cookie.secure`: Setting the `Secure` Flag

In JavaScript or server-side frameworks like Node.js, when the `secure` attribute is set to `true`, the browser will only send the cookie over HTTPS connections. If `secure: false` (the default), the cookie can be transmitted over both HTTP and HTTPS.

#### Example of Setting the `Secure` Attribute:
Here’s how you can set a secure cookie in Node.js using the popular `express` framework:

```javascript
res.cookie('sessionId', 'abcd1234', { secure: true, httpOnly: true, maxAge: 3600000 });
```

- **`secure: true`**: Ensures the cookie will only be sent over HTTPS.
- **`httpOnly: true`**: Ensures the cookie is inaccessible via JavaScript (`document.cookie`), which enhances security against XSS attacks.
- **`maxAge`**: Sets the expiration time for the cookie.

### Important Considerations When Using `secure: true`

1. **Requires HTTPS**: 
   - The `Secure` attribute requires your site to be served over HTTPS. Browsers will not send the cookie over an insecure (HTTP) connection if the `Secure` flag is set.
   - If you attempt to set a cookie with `secure: true` on an HTTP connection, **the cookie will not be set or transmitted**.

2. **Default Behavior**:
   - By default, the `Secure` attribute is **not** set, which means that cookies can be sent over both HTTP and HTTPS connections.
   - It's strongly recommended to set `secure: true` for cookies that contain sensitive information like authentication tokens, session IDs, or other private data.

3. **Compliant Clients**:
   - Most modern browsers fully support the `Secure` attribute. When this attribute is enabled, compliant clients will only send the cookie if the connection is secure (HTTPS).

4. **Impact of Misconfiguration**:
   - If `secure: true` is set but the website is accessed over HTTP, the cookie will **not be sent or stored**. This can lead to issues where cookies do not persist or session management fails.

### Usage in Express.js with Proxy Servers

If your Node.js application is behind a proxy (such as a load balancer or reverse proxy) and you're using `secure: true` for cookies, you need to ensure Express is aware of the proxy. Otherwise, Express will think the connection is HTTP (since the proxy connects over HTTP to your app) and won't set the secure cookies.

To fix this, set `trust proxy` in Express, which allows the app to trust the proxy and recognize the real HTTPS connection from the client:

```javascript
const express = require('express');
const app = express();

// Trust the proxy so secure cookies work behind the proxy
app.set('trust proxy', 1);

// Set secure cookies
app.get('/setcookie', (req, res) => {
  res.cookie('sessionId', 'abcd1234', { secure: true, httpOnly: true, maxAge: 3600000 });
  res.send('Cookie set');
});
```

### Why `secure: true` is Recommended

1. **Protection from Man-in-the-Middle Attacks**:
   When the `Secure` flag is set, cookies are only sent over encrypted HTTPS connections, preventing attackers from intercepting or modifying them in transit.

2. **Secure Data Transmission**:
   Any cookie marked as `Secure` will not be sent over HTTP, which is a plain-text connection. This is especially important for sensitive cookies like session IDs, which could otherwise be exposed.

### Common Issues with `secure: true`

1. **Cookies Not Sent on HTTP**: 
   If you access your site over HTTP while using `secure: true`, the browser will not send the cookie, leading to issues like session data not persisting or login failures. You must ensure your site is entirely served over HTTPS.

2. **Issues Behind Proxies**:
   If your Node.js app is behind a proxy (e.g., Nginx, AWS ELB), you may need to configure Express to trust the proxy (`app.set('trust proxy', true)`) so that the application recognizes that the original connection from the client was HTTPS.

### Summary

- **`secure: true`** ensures that cookies are only sent over HTTPS, enhancing security by protecting cookies from being transmitted over unencrypted HTTP connections.
- Use `secure: true` for all cookies containing sensitive information, especially session tokens and authentication cookies.
- **Ensure your site uses HTTPS** before setting `secure: true`, as cookies will not be sent over HTTP if the flag is enabled.
- **Configure your application to trust proxies** if you're using a proxy server, so secure cookies work properly behind it.

In general, using `secure: true` is a best practice for securing web applications, but it requires a properly configured HTTPS environment.