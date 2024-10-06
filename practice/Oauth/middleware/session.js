const express = require('express')
const session = require('express-session')

module.exports = session({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: false,
})