function logout(req, res) {
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
}

module.exports = {
    logout
}