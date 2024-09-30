function displayProfile(req, res) {
    console.log(`i'm in ${__dirname}/${__filename}`)
    if (req.session.cookie) {
        console.log("cookie still")
        console.log(req.session.cookie)
    }
    if (req.session.userId && req.session.isAuthenticated)
        res.render('profile')
    else {
        res.send("not authorizzed")
    }
}

module.exports = {
    displayProfile
}