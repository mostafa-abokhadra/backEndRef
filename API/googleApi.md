#### steps
1. Go to the [Google Cloud Platform console](https://console.cloud.google.com/welcome/new?inv=1&invt=AbeCWQ).
2. From the projects list, select a project or create a new one.
3. Navigate to the [APIs & Services](https://console.cloud.google.com/projectselector2/apis/dashboard?inv=1&invt=AbeCWg&supportedpurview=project) page and select Credentials.
4. If you have an existing application, it will be listed under OAuth 2.0 Client IDs. Click Edit OAuth client to obtain the client ID and secret.
5. If you have not already done so, configure the OAuth consent screen. Select External to make your application available to any user with a Google account. Complete the app registration process by entering the app name, support email, and developer contact information.
6. click Create Credentials, then select OAuth client ID.
7. Select Web application as Application type.
8. Click Add URI under Authorized Redirect URIs. Enter http://localhost:3000/
9. Click Create to create the OAuth client. The following screen will display your client ID and secret.