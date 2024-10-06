### Oauth
- stands for Open authentication
- user 3rd parties services like google, facebook, github, etc..

### pros
- one less thing for us to worry about (authentication)
- one less thing for user to worry about
    - to form to fill in to signIn
    - don't have many different accounts to remember passwords for
    - just a few central identities like google or facebook that you can use to sign in anywhere

### installation
```bash
npm install passport
npm install passport-google-oidc
```

### redirecting to google
```js
// in routes/auth.js
const passport = require('passport');
const GoogleStrategy = require('passport-google-oidc');
router.get('/login/federated/google', passport.authenticate('google'));
```
### registering app
- if you tried to run the code above, the app fails with an error indicating that the Google authentication strategy is unknown. That will be fixed by configuring the strategy. But first, the app needs to be registered with Google
- register the app with Google so that it can make use of Google's APIs.

#### steps
1. Go to the [Google Cloud Platform console](https://console.cloud.google.com/welcome/new?inv=1&invt=AbeCWQ).
2. From the projects list, select a project or create a new one.
3. Navigate to the [APIs & Services](https://console.cloud.google.com/projectselector2/apis/dashboard?inv=1&invt=AbeCWg&supportedpurview=project) page and select Credentials.
4. If you have an existing application, it will be listed under OAuth 2.0 Client IDs. Click Edit OAuth client to obtain the client ID and secret, and proceed to configure the strategy. Otherwise, continue.
5. If you have not already done so, configure the OAuth consent screen. Select External to make your application available to any user with a Google account. Complete the app registration process by entering the app name, support email, and developer contact information.
6. click Create Credentials, then select OAuth client ID.
7. Select Web application as Application type.
8. Click Add URI under Authorized Redirect URIs. Enter http://localhost:3000/
9. Click Create to create the OAuth client. The following screen will display your client ID and secret.
10. Proceed to configure the strategy.

### configure Passport
- configure Passport with the information obtained during registration.
- First, create a `.env` file to store the client ID and secret that were obtained from Google.
```bash
touch .env
cat .env
GOOGLE_CLIENT_ID=yourClientId
GOOGLE_CLIENT_SECRET=yourClientSecret
```
```js
// in routes/auth.js
passport.use(new GoogleStrategy({
  clientID: process.env['GOOGLE_CLIENT_ID'],
  clientSecret: process.env['GOOGLE_CLIENT_SECRET'],
  callbackURL: '/oauth2/redirect/google',
  //The URL that Google will redirect the user to after successful authentication.
  scope: [ 'profile' ] // The permissions requested from the user. In this case, only the "profile" scope is requested, which grants access to the user's basic profile information.
}, function verify(issuer, profile, cb) {
    // This function is the callback function that is called by the GoogleStrategy when authentication is successful.
          var user = {
            id: id,
            name: profile.displayName
          };
          return cb(null, user);
}))
```
**verify function It receives three arguments**

1. **issuer**: The issuer of the ID token (typically https://accounts.google.com).
2. **profile**: An object containing the user's profile information, including their ID, name, email, and other details.
3. **cb**: A callback function that should be called with the following arguments:
    - **err**: An error object if something went wrong.
    - **user**: The authenticated user object, or false if authentication failed.
    - **info**: Additional information about the authentication process (optional).
3. var user = { id: profile.id, name: profile.displayName };
    - This line creates a new object representing the authenticated user.
    - The id property is set to the user's Google ID, which is unique for each user.
    - The name property is set to the user's display name, which is the name they use on Google.
4. return cb(null, user);
    - This line calls the callback function with null as the error argument and the user object as the user argument.
    - This indicates that authentication was successful and the authenticated user is ready to be used in the application.

### adding session support to maintain state
When a user signs in to the app with Google, they are redirected to Google. Google takes care of authenticating the user and then redirects them back to the app. For security reasons, it is important that state is maintained and validated between these two redirects.

```js
var session = require('express-session');
app.use(express.static(path.join(__dirname, 'public')));
app.use(session({
  secret: 'keyboard cat',
  resave: false,
  saveUninitialized: false,
  store: new SQLiteStore({ db: 'sessions.db', dir: './var/db' })
}));
```
Now that the app has session support, the next step is to
### handle the redirect back from Google to the app.
- add a route that authenticates the user when Google redirects them back to the app.
```js
router.get('/oauth2/redirect/google', passport.authenticate('google', {
  successRedirect: '/',
  failureRedirect: '/login'
}));
```
if you tried to run all of the above code you will still get an error, the app fails with an error related to sessions. so Next, you will fix that error by configuring Passport to establish a sessoin
### configure passport to establish a session
- you'll establish a login session which will maintain the user's authenticated state as they navigate the app.
- add this line after session middleware configuration object in server.js file or whatever
```js
app.use(passport.authenticate('session'));
```
- Finally, configure Passport to persist user information in the login session
```js
// in routes/auth.js
passport.serializeUser(function(user, cb) {
  process.nextTick(function() {
    cb(null, { id: user.id, username: user.username, name: user.name });
  });
});

passport.deserializeUser(function(user, cb) {
  process.nextTick(function() {
    return cb(null, user);
  });
});
```
## Explanation of `passport.serializeUser` and `passport.deserializeUser` in Passport.js

These two functions are crucial for maintaining user sessions in Passport.js, a popular authentication middleware for Node.js applications. Here's a detailed breakdown of their roles:

**1. `passport.serializeUser(function(user, cb) {...})`**

This function is responsible for converting a user object into a format suitable for storing in the session. Sessions typically use cookies, which have size limitations. Therefore, `serializeUser` needs to select a minimal set of data that uniquely identifies the user.

* **Arguments:**
    - `user`: This is the user object typically obtained after successful authentication (e.g., through strategies like `LocalStrategy` or `GoogleStrategy`).
    - `cb`: This is a callback function with two arguments:
        - `err`: An error object if something went wrong during serialization.
        - `data`: The serialized user data that will be stored in the session.

* **Function Body:**
    - **`process.nextTick(function() {...})`:** This line schedules the inner function to be executed in the next event loop iteration. This is often used to ensure that any asynchronous operations within `serializeUser` are completed before returning the serialized data. 
    - **`cb(null, { id: user.id, username: user.username, name: user.name })`:** This line calls the callback function with `null` for the error (indicating success) and an object containing the serialized user data. Here, we're including `id`, `username`, and `name`. You can customize this to include only the essential information for user identification.

**2. `passport.deserializeUser(function(id, cb) {...})**

This function is responsible for retrieving the user object from the session data.

* **Arguments:**
    - `id`: This is the serialized user data that was previously stored in the session by `serializeUser`.
    - `cb`: This is a callback function with two arguments:
        - `err`: An error object if something went wrong during deserialization.
        - `user`: The deserialized user object, or `false` if the user could not be found.

* **Function Body:**
    - **`process.nextTick(function() {...})`:** Similar to `serializeUser`, this ensures any asynchronous operations within `deserializeUser` are completed before returning the user object.
    - **`return cb(null, user)`:** This line calls the callback function with `null` for the error and the retrieved user object. In a real application, you'd likely use the `id` to fetch the complete user information from your database (e.g., using `findById` on a user model) before passing it to the callback. However, the provided example assumes the user object is already available.

## How They Work Together

1. During login, after successful authentication, `serializeUser` is called to convert the user object into a minimal representation (e.g., `id`, `username`) and store it in the session.
2. When the user navigates through the application, subsequent requests include the session cookie with the serialized data.
3. Passport intercepts these requests and calls `deserializeUser` with the serialized data (`id` in this example).
4. You'd typically use the `id` to retrieve the complete user object from your database and pass it to the callback.
5. Passport then has access to the user object throughout the request and can use it for authorization checks (e.g., ensuring the user has access to the requested resource).

**Important Notes:**

* You should customize `serializeUser` to include only the essential user data needed for identification.
* Implement proper error handling in `deserializeUser` to handle cases where the user data can't be retrieved from the session.
* Consider using secure session storage mechanisms to protect user data.

I hope this explanation clarifies the roles of `passport.serializeUser` and `passport.deserializeUser` in Passport.js!

### logout
```js
router.post('/logout', function(req, res, next) {
  req.logout(function(err) {
    if (err) { return next(err); }
    res.redirect('/');
  });
});
```
This code snippet defines a route handler for logging out a user in a Node.js application using Passport.js. Let's break it down step by step:

**1. `router.post('/logout', function(req, res, next) { ... })`**

- `router`: This likely refers to an Express.js router object that maps incoming requests to specific functions (route handlers).
- `.post('/logout', ...)`: This defines a route handler for the POST request method at the `/logout` path. This means that when a POST request is sent to the `/logout` endpoint, this function will be executed.
- `req`: This is the request object that contains information about the incoming request, such as headers, body, and parameters.
- `res`: This is the response object that allows you to send a response back to the client.
- `next`: This is a callback function that can be used to pass control to the next middleware function in the chain.

**2. `req.logout(function(err) { ... })`**

- `req.logout()`: This is a function provided by Passport.js that is attached to the request object (`req`) after Passport has been initialized and configured. It's responsible for terminating the user's session.
- `function(err) { ... }`: This is a callback function that will be called by `req.logout()` after the logout process is complete.
    - `err`: This parameter holds any error that might have occurred during the logout process.

**3. `if (err) { return next(err); }`**

- This line checks if there was an error during logout (`err` is not `null`).
    - `return next(err);`: If there was an error, the code exits the current function and passes the error to the next middleware function in the chain using `next(err)`. This allows for centralized error handling in your application.

**4. `res.redirect('/');`**

- If there's no error (`err` is `null`), this line assumes successful logout and sends a redirect response to the client.
    - `res.redirect('/')`: This redirects the user's browser to the root path (`/`) of your application. You can customize this to redirect to any other desired location after logout.

**In summary,** this code snippet provides a route for users to log out of your application. When a user sends a POST request to `/logout`, Passport.js handles the session termination, and upon success, the user is redirected to the homepage (`/`). 

**Additional Notes:**

* Depending on your implementation, you might want to perform additional actions after logout, such as clearing any user-specific data from the session or client-side storage.
* You should also consider implementing security measures to prevent unauthorized logout requests.
