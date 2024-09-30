const express = require("express")
const AuthenticationRoute = require('./routes/authentication')
const homeRoute = require("./routes/home")
const session = require('./middleware/session')

const port = 3000 
server = express()
server.set('view engine', 'ejs')
server.use(session)
server.use(express.json());
server.use(express.urlencoded({ extended: true }));

server.use(homeRoute)
server.use(AuthenticationRoute)

server.listen(port, (err) => {
    console.log("errrrrrrrrroro" + err)
    if (err) {
        console.log("can't listen to port")
    }
    console.log("listening")
})