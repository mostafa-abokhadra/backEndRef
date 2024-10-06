require('dotenv').config()
const express = require("express")
const passport = require('passport')

const indexRouter = require('./routes/index')
const authRouter = require('./routes/auth')

const session = require("./middleware/session")

const server = express()

server.set('view engine', 'ejs')

server.use(session)
server.use(passport.authenticate('session'));

server.use('/', indexRouter)
server.use('/', authRouter)


server.listen(process.env.PORT, () => {
    console.log(`i'm listening on port ${process.env.PORT}`)
})