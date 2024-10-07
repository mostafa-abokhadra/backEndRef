### Restriction on Modifying Cookies via `Cookie` Header

When making HTTP requests using JavaScript (via `fetch()` or `XMLHttpRequest`), you **cannot directly modify or send custom cookies** by setting the `Cookie` header. Browsers enforce this restriction for **security reasons**. Specifically, the `Cookie` header is controlled by the browser, and any cookies that are relevant to the request (based on domain, path, and other attributes) will be automatically sent by the browser.

#### Example: Fetch Request without Cookie Header Control

```javascript
fetch('https://example.com/api', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer token123',  // Custom headers like Authorization are allowed
    'Cookie': 'session_id=abc123'        // This will be ignored, as browsers prevent manual cookie setting
  }
})
```

In the above example, trying to set the `Cookie` header manually will be ignored by the browser. The browser will only send cookies that it has stored and that meet the criteria for inclusion in the request (e.g., same domain, proper `SameSite` rules, etc.).

### Why is this Restriction in Place?

This restriction helps to prevent **cross-site scripting (XSS)** attacks and other security risks where malicious scripts might try to manipulate session cookies or other sensitive data stored in cookies. 

For example:
- **If JavaScript could modify the `Cookie` header directly**, an attacker could inject JavaScript that sends a malicious request with a custom session ID or other security-sensitive cookies, potentially hijacking sessions.
- **Sensitive cookies**, like session tokens or authentication cookies, are often marked as `HttpOnly`, meaning they can't be accessed or modified via JavaScript for security purposes.

### Security Reasons for Using `HttpOnly` Cookies

One of the primary ways to mitigate risks of XSS and cookie manipulation is by marking cookies with the `HttpOnly` flag. Here’s why:

#### What is `HttpOnly`?

- **`HttpOnly`** is a cookie attribute that, when set, **prevents JavaScript from accessing the cookie**. This means cookies marked with `HttpOnly` cannot be read, modified, or deleted using `document.cookie`.
- `HttpOnly` cookies are still sent automatically with each HTTP request to the server but remain inaccessible to JavaScript.

#### Why Use `HttpOnly`?

1. **Prevents XSS Exploits**:
   If an attacker manages to inject malicious JavaScript into a webpage (via an XSS vulnerability), they could potentially steal sensitive cookies like session tokens, login credentials, or authentication tokens. If a cookie is marked `HttpOnly`, it cannot be accessed by JavaScript, reducing the risk of sensitive data theft.

   Without `HttpOnly`:
   ```javascript
   // XSS attack: Malicious script could steal sensitive cookie data
   console.log(document.cookie);  // Outputs session tokens, etc.
   ```

   With `HttpOnly`:
   ```javascript
   // Malicious script can't access the cookie
   console.log(document.cookie);  // Outputs nothing for HttpOnly cookies
   ```

2. **Enhances Authentication Security**:
   Cookies used for sensitive information like authentication tokens or session IDs should always be marked `HttpOnly`. This ensures that they are **only accessible via server-side code** and are not exposed to client-side scripts, protecting them from being compromised.

#### Example: Secure Cookie with `HttpOnly` and `Secure` Flags

```http
Set-Cookie: session_token=abcd1234; HttpOnly; Secure; SameSite=Strict;
```

- **`HttpOnly`**: Prevents JavaScript from accessing the session token.
- **`Secure`**: Ensures that the cookie is only sent over HTTPS, preventing it from being intercepted during transmission.
- **`SameSite=Strict`**: Ensures that the cookie is only sent when requests originate from the same site (helps protect against Cross-Site Request Forgery (CSRF) attacks).

### Summary of Security Considerations

- **You cannot manually set the `Cookie` header** in JavaScript via `fetch()` or `XMLHttpRequest`. The browser controls this behavior to prevent malicious scripts from manipulating sensitive cookies.
- **`HttpOnly` cookies** cannot be accessed or modified by JavaScript, providing extra security for sensitive data, such as session IDs or authentication tokens.
- **Use the `Secure` and `SameSite` attributes** to further protect cookies from being intercepted or misused.

In general, restricting JavaScript’s ability to manipulate cookies and using secure cookie attributes (`HttpOnly`, `Secure`, `SameSite`) are key defenses against various types of attacks, including XSS and CSRF.