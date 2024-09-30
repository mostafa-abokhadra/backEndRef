function getLogin(req, res) {
    console.log(`i'm in ${__dirname}/${__filename}`)
    res.render('login')
}
function postLogin(req, res) {
    console.log(`i'm in ${__dirname}/${__filename}`)
    req.session.userId = 1
    req.session.isAuthenticated = true
    if (req.session.userId && req.session.isAuthenticated)
        res.redirect('dashboard')
}

module.exports = {
    getLogin,
    postLogin
}