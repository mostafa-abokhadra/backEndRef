### Oauth
- stands for Open authentication
- user 3rd parties services like google, facebook, github, etc..

### pros
- one less thing for us to worry about (authentication)
- one less thing for user to worry about
    - to form to fill in to signIn
    - don't have many different accounts to remember passwords for
    - just a few central identities like google or facebook that you can use to sign in anywhere

```bash
npm install passport
npm install passport-google-oidc
```

```js
// in routes/auth.js
const passport = require('passport');
const GoogleStrategy = require('passport-google-oidc');

```