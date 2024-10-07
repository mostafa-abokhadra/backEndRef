### express-session-code
```bash
npm install express
npm install express-session
npm i ejs
```
```js
const session = require("express-session")
const session = require("express-session")
```
```js
const port = 3000 // process.env.PORT
server = express()
server.set('view engine', 'ejs')

// The part where you configure app.use(session({...})) only sets up the session middleware
// for your Express application but does not actually initialize a session for every user immediately.
// The session is only initialized (and a cookie is only sent to the client) when you set
// something on req.session, like req.session.user = username after successful authentication.
server.use(session({
    // store: redisStore({client: redisClient}),
    name: "firstCookie", // name of cookie instead of default "connect.sid", fiind in browser
    secret: "myProjectSecretKey", // use something complex
    resave: false,
    saveUninitialized: false, // don't start session untill adding a field to session object e:g req.session.userId = 1
    cookie: {
        secure: false,
        httpOnly: true,
        MaxAge: 60000
    }
}))

// you need these two lines to access req.body
server.use(express.json());  // To parse JSON bodies, to enable req.body
// Add the express.urlencoded() middleware to your Express app to parse the POST request body.
// This middleware is used to parse application/x-www-form-urlencoded data, which is the
// default form data type for HTML forms.
server.use(express.urlencoded({ extended: true }));

server.get("/", (req, res) => {
    if (req.session.isAuthenticated) {
        res.redirect('dashboard')
    } else {
        res.render("index")
    }
})

server.get("/login", (req, res) => {
  if (req.session.isAuthenticated) {
    res.redirect('/dashboard')
  }
  res.render('login')
})

server.post("/login", (req, res) => {
    // req.url // /login
    // req.method POST
    // req.headers
    // req.body // contains object of data sent with form in the format name: vlaue
    // req.query
    // req.cookies
        // const cookieParser = require('cookie-parser');
        // app.use(cookieParser());
    // req.ip // ip address of client
    // req.get(headerName) // retrieve a specific request header.
    // req.protocol // protocol used by the client (either http or https)
    // req.secure
    // req.path /login
    // req.hostname
    // req.originalUrl
    // res.end(String(req.session.userId)) // if you want to send numerical convert first to string
    req.session.userId = 12345
    req.session.isAuthenticated = true
    if (req.session.userId && req.session.isAuthenticated)
        res.redirect('dashboard')
})
server.get('/dashboard', (req, res) => {
    if (req.session.isAuthenticated && req.session.userId)
        res.render('dashboard')
    else {
        res.send("unauthorized")
    }
})
server.get('/profile', (req, res) => {
    if (req.session.userId && req.session.isAuthenticated)
        res.render('profile')
    else {
        res.send("not authorizzed")
    }
})
server.post('/logout', (req, res) => {
    console.log(req.url, req.method, req.body, req.session.isAuthenticated, req.session.userId)
    if (req.session.isAuthenticated) {
        req.session.destroy(err => {
            if (err) {
                return res.status(500).send("couldn't logout")
            }
            res.clearCookie('firstCookie')
            res.redirect('/')
        })
    } else {
        console.log("no session to logout")
    }
})
server.listen(port, () => {
    console.log("listening")
})

```