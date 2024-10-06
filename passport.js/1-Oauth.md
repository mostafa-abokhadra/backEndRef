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