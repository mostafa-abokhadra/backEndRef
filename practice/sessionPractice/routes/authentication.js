const express = require('express')
const router = express.Router()
const loginController = require('../controller/authentication/login')
const dashboardController = require('../controller/dashboard/dashboard')
const profileController = require('../controller/profile/profile')
const logoutController = require('../controller/authentication/logout')

router.get("/login", loginController.getLogin)
router.post("/login", loginController.postLogin)
router.get('/dashboard', dashboardController.displayDashboard)
router.get('/profile', profileController.displayProfile)
router.post('/logout', logoutController.logout)

module.exports = router