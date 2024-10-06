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
}
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
