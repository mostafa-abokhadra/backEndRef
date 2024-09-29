### cookies
- s a small piece of data a server sends to a user's web browser. The browser may store cookies, create new cookies, modify existing ones, and send them back to the same server with later requests.
- Typically, the server will use the contents of HTTP cookies to determine whether different requests come from the same browser/user and then issue a personalized or generic response as appropriate.

### example: simple SignIn
- The user sends sign-in credentials to the server, for example via a form submission.
- If the credentials are correct, the server updates the UI to indicate that the user is signed in, and responds with a cookie containing a session ID that records their sign-in status on the browser.
- At a later time, the user moves to a different page on the same site. The browser sends the cookie containing the session ID along with the corresponding request to indicate that it still thinks the user is signed in.
- The server checks the session ID and, if it is still valid, sends the user a personalized version of the new page. If it is not valid, the session ID is deleted and the user is shown a generic version of the page (or perhaps shown an "access denied" message and asked to sign in again).

![](./imgs/cookie-basic-example.png)

### uses of cookies
- **Session management**: User sign-in status, shopping cart contents, game scores, or any other user session-related details that the server needs to remember.
- **Personalization**: User preferences such as display language and UI theme.
- **Tracking**: Recording and analyzing user behavior.

> [!NOTE]
> you can see stored cookies in the <mark>Application</mark> panel in Chrome Developer Tools.

### sending cookies
After receiving an HTTP request, a server can send one or more Set-Cookie headers with the response, each one of which will set a separate cookie. to instructs the receiving browser to store a pair of cookies: A simple cookie is set by specifying a name-value pair like this, 
```
Set-Cookie: <cookie-name>=<cookie-value>
et-Cookie: yummy_cookie=choco
Set-Cookie: tasty_cookie=strawberry
```

- When a new request is made, the browser usually sends previously stored cookies for the current domain back to the server within a Cookie HTTP header:
<mark>Cookie: yummy_cookie=choco; tasty_cookie=strawberry</mark>

### cookie Expiration
- Permanent cookies are deleted after the date specified in the <mark>Expires</mark> attribute
- or after the period specified in the <mark>Max-Age</mark> attribute:
``
Set-Cookie: id=a3fWa; Expires=Thu, 31 Oct 2021 07:28:00 GMT;
Set-Cookie: id=a3fWa; Max-Age=2592000
``

> [!NOTE]
> Expires has been available for longer than Max-Age, however Max-Age is less error-prone, and takes precedence when both are set. The rationale behind this is that when you set an Expires date and time, they're relative to the client the cookie is being set on. If the server is set to a different time, this could cause errors.

### Explanation:

1. **Expires Attribute**: 
   - The `Expires` attribute defines the exact date and time when the cookie should expire. It's set in a specific format (usually GMT/UTC).
   - Example: `Expires=Wed, 21 Oct 2024 07:28:00 GMT`
   - **Issue**: The expiration is dependent on the client's system clock. If the client's clock is not synchronized with the server's clock (or is set to a different time zone), this can result in unexpected behavior, such as the cookie expiring too early or too late. This is why `Expires` can be error-prone.

2. **Max-Age Attribute**: 
   - The `Max-Age` attribute specifies the cookie's lifetime in seconds, starting from the moment it is set. After this duration, the cookie is considered expired.
   - Example: `Max-Age=3600` (sets the cookie to expire in 1 hour).
   - **Advantage**: Because `Max-Age` is relative (based on how many seconds from now), it avoids issues with time zone differences or clock synchronization between the server and the client. This makes it **less error-prone** than `Expires`.

3. **Precedence**:
   - When both `Expires` and `Max-Age` are set, **Max-Age takes precedence** because it's more reliable. This ensures that even if there is a discrepancy in the server-client clock synchronization, the cookie will still expire after the correct amount of time has passed.

### Key Point:
- **Expires** has been around longer and is still supported, but **Max-Age** is preferred for its reliability in avoiding time synchronization errors.

> [!NOTE]
> Session cookies are cookies without a Max-Age or Expires attribute, they are deleted when the current session ends. The browser defines when the "current session" ends, and some browsers use session restoring when restarting. This can cause session cookies to last indefinitely.

### Breakdown:

1. **Session Cookies**:
   - Session cookies are meant to last only for the duration of the user's session, meaning they should be deleted when the user closes the browser.
   - These cookies do not specify an expiration time (i.e., no `Max-Age` or `Expires` attribute).

2. **Browser-Defined Session**:
   - Different browsers have their own ways of determining when a session ends.
   - For most browsers, closing all tabs or windows will typically end the session and delete session cookies.
   - Some browsers might define the session differently, such as based on whether the user is logged in or if any browser process is still running.

3. **Session Restoring**:
   - Modern browsers often include a **session restore** feature, where tabs and their contents (including cookies) are saved when the browser is closed and restored when the browser is restarted.
   - This means that session cookies might be retained even after a browser is closed, causing the session to **persist indefinitely** if the browser restores it.
   - Essentially, the session doesn't truly "end" until the user manually clears the session data or disables session restoring, leading to cookies that were meant to be temporary lasting much longer than expected.

### Implications:
- While session cookies are supposed to be temporary, the use of session restore features in modern browsers can lead to **unexpected behavior**, where cookies persist across browser restarts.
- This can introduce security concerns, as a user might expect their session (and its cookies) to expire when they close the browser, but session restoring can extend their lifespan.

### Solutions:
- If it's critical that cookies expire after a certain time, using the **Max-Age** or **Expires** attribute is a better approach to ensure cookies are removed after a fixed duration.
- For extra security, web applications can implement server-side session management that explicitly invalidates session cookies when the server detects the session has ended or after a timeout.

In summary, while session cookies are intended to be temporary, features like session restoring can cause them to last longer than intended. Using explicit expiration attributes (like `Max-Age`) can help prevent this.