const express = require('express')
const router = express.Router()

router.get("/", (req, res) => {
    if (req.session.isAuthenticated) {
        console.log(req.session)
        res.redirect('dashboard')
    } else {
        res.render("index")
    }
})

module.exports = router