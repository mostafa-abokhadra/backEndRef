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

> [!NOTE]
> If your site authenticates users, it should regenerate and resend session cookies, even ones that already exist, whenever a user authenticates. This approach helps prevent session fixation attacks, where a third-party can reuse a user's session.

### 1. **Understanding Session Fixation Attacks**

A **session fixation attack** occurs when an attacker is able to set or predict the session ID (session cookie) for a user before they authenticate, and then later exploit this session to hijack the authenticated session.

#### Example Attack Scenario:
- **Step 1: Attacker sets a session for the victim**:
  - The attacker creates a valid session on the website by, for example, visiting the login page or accessing the site.
  - The attacker then sends the session ID (perhaps via a phishing link, URL parameter, or through cross-site scripting) to the victim, encouraging them to click on it and log in.
  - Example link: `http://example.com/login?session_id=abc123`, where `abc123` is the session ID controlled by the attacker.

- **Step 2: Victim logs in**:
  - The victim follows the link, logs into the website, and since the server doesn't regenerate a new session ID after authentication, the session remains as `abc123`.

- **Step 3: Attacker hijacks the session**:
  - Now that the user has logged in, the attacker already knows the active session ID (`abc123`) and can use it to access the victim's account without needing to log in themselves. Since the server hasn’t generated a new session after authentication, the attacker can impersonate the user and perform malicious actions.

### 2. **Why Session Regeneration is Critical**

The solution to session fixation is simple but highly effective: **regenerate the session ID** upon authentication.

- When a user logs in, the server should generate a completely **new session ID** that is unrelated to any session ID used during the unauthenticated browsing session. This prevents an attacker from continuing to use a session ID they might know or have set up.
- This new session ID is sent to the user in a fresh session cookie, making the attacker's previously known session ID invalid.
  
By regenerating the session ID after authentication:
- The server invalidates any session the attacker might know about.
- The attacker can no longer use the old session ID to impersonate the user.

### 3. **How to Implement Secure Session Management**

Here are some key details on **regenerating and resending session cookies**:

#### a) **Regenerating the Session ID**
Upon successful user authentication (i.e., when the user logs in):
- The server should create a new session ID for the user.
- Any existing session data from the unauthenticated session can be copied over to the new session (if necessary, for things like shopping carts), but the session ID itself must be completely new.
- For example, a new session ID can be generated using secure random number generators, often provided by cryptographic libraries.
  
In Python’s Flask framework:
```python
session.regenerate()
```
This hypothetical function would create a new session ID after the user logs in.

#### b) **Resending the Session Cookie**
After regenerating the session ID:
- The new session ID should be sent to the user's browser as a **new session cookie**.
- This ensures that the session ID the user now holds is unique and tied to their newly authenticated session.

This can be done by sending the `Set-Cookie` header in the HTTP response:
```http
Set-Cookie: session_id=new_secure_session_id; HttpOnly; Secure; SameSite=Strict;
```
- **HttpOnly** ensures that the cookie cannot be accessed via JavaScript, mitigating cross-site scripting (XSS) attacks.
- **Secure** ensures that the cookie is only sent over HTTPS, protecting it from being intercepted.
- **SameSite=Strict** prevents cross-site request forgery (CSRF) by only sending the cookie with requests originating from the same domain.

#### c) **Invalidating the Old Session**
- If an unauthenticated session existed before login, the server should invalidate or destroy the old session. This prevents the possibility of old, potentially insecure session IDs lingering.
- In many frameworks, you can explicitly destroy the old session once the new one is established. For example:
  ```python
  session.invalidate()
  ```

### 4. **Additional Security Measures to Strengthen Session Management**

To further secure session cookies and authentication, you should also consider the following practices:

#### a) **Short Expiration Time for Cookies**
- You can set a `Max-Age` or `Expires` attribute on the session cookie to limit how long a session remains valid. This reduces the risk of prolonged session hijacking.
  ```http
  Set-Cookie: session_id=new_secure_session_id; Max-Age=3600; HttpOnly; Secure;
  ```
  This sets the session cookie to expire in 1 hour.

#### b) **Invalidate Sessions on Logout**
- When the user logs out, you should destroy the session on the server and delete the session cookie. This ensures that no lingering session ID can be used after logout.
- For example, in Flask, you can call:
  ```python
  session.pop('user_id', None)  # Removes the user's session
  ```

#### c) **Use Strong Randomness for Session IDs**
- The session ID should be a long, random string that’s difficult to guess or brute-force. Using cryptographic random generators makes session IDs unpredictable.

#### d) **Monitor and Detect Suspicious Session Behavior**
- Implement server-side logic to detect unusual session activities, such as simultaneous use of the same session from different IP addresses or locations. This can help identify hijacked sessions.

### Summary of Benefits:
- **Session ID Regeneration**: Ensures that attackers can't hijack the session after a user authenticates, even if they know the previous session ID.
- **Resending Session Cookies**: Provides the user with a fresh session cookie that is only valid after login.
- **Mitigating Session Fixation**: Eliminates the risk of an attacker pre-setting or manipulating the session before authentication.

By following these practices, you protect your application from session fixation and provide more secure session management for your users.

### Updating cookies value
To update a cookie via HTTP, the server can send a Set-Cookie header with the existing cookie's name and a new value. For example:

<mark>Set-Cookie: id=new-value</mark>

When a server sends a `Set-Cookie` header with the same cookie name but a new value, it **updates the existing cookie** stored in the user's browser. This can be useful in various scenarios, such as when user preferences change or session data needs to be modified.

### How Cookie Updating Works:

- **Updating the Cookie**:
  When the server sends an HTTP response that includes a `Set-Cookie` header with the same cookie name but a different value, the browser automatically replaces the old cookie with the new one. Here's an example:

  ```http
  Set-Cookie: id=new-value
  ```

  In this case, the server updates the `id` cookie with the value `new-value`. If the browser previously had a cookie named `id` with a different value, the new value will overwrite the old one.

### Example Use Cases for Updating Cookies:

1. **User Preference Changes**:
   - If a user updates their preferences (e.g., changes language settings, theme preferences, or notification settings), the server can update the cookie to store the new preference.
   - Example: If a user changes their language setting from English to Spanish:
     ```http
     Set-Cookie: language=es
     ```
     The `language` cookie is updated to reflect the user's new choice.

2. **Session Updates**:
   - If session-related data needs to be updated (e.g., after the user logs in or extends their session), the server can update the session cookie.
   - Example: If the user extends their session by interacting with the website, the server could refresh the session token:
     ```http
     Set-Cookie: session_token=updated_session_token; Max-Age=3600
     ```
     This would extend the session cookie’s expiration time.

3. **Tracking Changes**:
   - Cookies can also be used to track user actions, like adding items to a shopping cart. If the user adds or removes items, the server can update a cookie that stores the cart information.
   - Example: If the user adds a new item to the cart, the server can send:
     ```http
     Set-Cookie: cart=updated_cart_data
     ```

4. **Security Purposes**:
   - If there are security changes (e.g., a user updates their password or enables multi-factor authentication), session cookies or authentication tokens might need to be updated to reflect the change.
   - Example: After a password change:
     ```http
     Set-Cookie: auth_token=new_secure_token; Secure; HttpOnly
     ```

### Overwriting a Cookie:
When updating a cookie, all properties of the cookie (such as `Path`, `Domain`, `Secure`, `HttpOnly`, and `SameSite`) need to be consistent with the original cookie if you want to overwrite it. If the attributes differ (e.g., different `Path` or `Domain`), the browser might create a new cookie instead of updating the existing one.

For example, the following header updates the cookie's value and specifies an expiration time:
```http
Set-Cookie: id=new-value; Expires=Wed, 21 Oct 2025 07:28:00 GMT; HttpOnly; Secure
```

If you omit `Expires` or `Max-Age`, the cookie will be a **session cookie** and will be deleted when the browser session ends.

### Client-Side Storage Mechanism:

As an alternative to using cookies, some applications prefer to store client-side data using the **Web Storage API**:
- **LocalStorage**: Stores data persistently in the browser even after the session ends (until explicitly deleted).
- **SessionStorage**: Stores data for the duration of the session (deleted when the session ends).

Example of setting data with `LocalStorage`:
```javascript
localStorage.setItem('language', 'es');  // Stores language preference
```

This can be used for **client-specific** data like preferences or non-sensitive information, while cookies are better suited for **server-side** purposes like sessions, authentication, and data that needs to be sent with every request to the server.

### Summary:
- **Updating cookies via `Set-Cookie`** allows the server to modify cookie values on the client when necessary (e.g., after a user updates preferences or authentication details).
- Make sure to keep attributes consistent when updating cookies to prevent unintended cookie duplication.
- For client-only storage needs, **Web Storage** (e.g., `localStorage`, `sessionStorage`) can be used instead of cookies, which are automatically sent with every HTTP request.

This mechanism helps ensure that the application can reflect changes in user data both server-side and client-side.