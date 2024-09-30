function displayDashboard(req, res) {
    console.log(`i'm in ${__dirname}/${__filename}`)
    if (req.session.isAuthenticated && req.session.userId)
        res.render('dashboard')
    else {
        res.send("unauthorized")
    }
}

module.exports = {
    displayDashboard
}