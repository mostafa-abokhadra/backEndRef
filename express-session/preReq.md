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