const session = require("express-session")
module.exports = session({
    name: "firstCookie",
    secret: "myProjectSecretKey",
    resave: false,
    saveUninitialized: false,
    cookie: {
        secure: false,
        httpOnly: true,
        maxAge: 24 * 60 * 60 * 1000 // one day
    }
})
