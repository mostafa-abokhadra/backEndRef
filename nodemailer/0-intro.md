### nodemailer
-  allows easy email sending.
```bash
npm i nodemailer
```
```js
const nodemailer = require('nodemailer');
const { OAuth2Client } = require('google-auth-library');

// Replace with your Gmail credentials
const clientId = 'YOUR_CLIENT_ID';
const clientSecret = 'YOUR_CLIENT_SECRET';
const refreshToken = 'YOUR_REFRESH_TOKEN';

// Create OAuth2 client
const oAuth2Client = new OAuth2Client(clientId, clientSecret);
oAuth2Client.setCredentials({ refresh_token: refreshToken });

// Create Nodemailer transporter
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    type: 'OAuth2',
    user: 'your_email@gmail.com',
    clientId,
    clientSecret,
    refreshToken,
    accessToken: oAuth2Client.getAccessToken(),
  },
});

// Function to send a reset password email
async function sendResetPasswordEmail(recipientEmail, resetToken) {
  const mailOptions = {
    from: 'your_email@gmail.com',
    to: recipientEmail,
    subject: 'Reset Your Password',
    text: `Please click on the following link to reset your password: ${resetToken}`,
    html: `<p>Please click on the following link to reset your password: <a href="${resetToken}">${resetToken}</a></p>`,
  };

  try {
    const info = await transporter.sendMail(mailOptions);
    console.log('Email sent: %s', info.messageId);
  } catch (error) {
    console.error('Error sending email:', error);
  }
}

// Example usage
sendResetPasswordEmail('recipient@example.com', 'your_reset_token');
```